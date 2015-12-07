import cv2
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import skimage
import skimage.segmentation as seg
import skimage.color as skcol
import skimage.filters as filt
from skimage.util import img_as_float, img_as_ubyte
from scipy import ndimage as ndi
from scipy import stats
import sklearn.cluster as skcl
import sklearn.decomposition as decomp
from numpy import float64
from sklearn.preprocessing import normalize

__author__ = 'nrosetti94'

def kmeans(image):
    K = 5
    Z = image.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)
    ret,label,center = cv2.kmeans(Z, K, None, criteria, 30, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((image.shape))
    cv2.imshow('res2',res2)
    cv2.waitKey(0)

def slic(image):
    try:
        numSegments = int(image.shape[0]*image.shape[1]/312)
        imageCopy = img_as_float(image)
        sobel = filt.sobel(skcol.rgb2gray(image))
        segments = seg.slic(imageCopy, numSegments, sigma=1, convert2lab=True, enforce_connectivity=False, slic_zero=False)

        medianTuples = []
        edgeResponse = []
        for i in range(numSegments):
            if imageCopy[segments == i].shape[0] > 0:
                medianTuples.append([np.nanmedian(imageCopy[segments == i][:,0]), np.nanmedian(imageCopy[segments == i][:,1]), np.nanmedian(imageCopy[segments == i][:,2])])
                edgeResponse.append(np.nanmean(sobel[segments == i]))
        medianTuples = np.array(medianTuples)
        edgeResponse = np.array(edgeResponse)
        cv2.normalize(medianTuples, medianTuples, 0, 255, cv2.NORM_MINMAX)
        cv2.normalize(edgeResponse, edgeResponse, 0, 20, cv2.NORM_MINMAX)
        medianTuples = medianTuples.tolist()
        for i in range(len(medianTuples)):
            medianTuples[i].append(edgeResponse[i])

        db = skcl.DBSCAN(eps = 6, min_samples=4).fit(medianTuples)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

        #create list of segments for each label
        labelledSegments = []
        for i in range(n_clusters_):
            segment = np.zeros(segments.shape, dtype=bool)
            for j in range(labels.shape[0]):
                if labels[j] == i:
                    segment[segments == j] = True
            labelledSegments.append(segment)

        colorList = []
        for i in range(n_clusters_):
            col = (np.nanmean(imageCopy[labelledSegments[i]][:,0]), np.nanmean(imageCopy[labelledSegments[i]][:,1]), np.nanmean(imageCopy[labelledSegments[i]][:,2]))
            #col = np.random.rand(3,)
            imageCopy[labelledSegments[i]] = col
            colorList.append(col)


        for i in range(numSegments):
            try:
                if(labels[i] == -1):
                    imageCopy[segments == i] = (0, 0, 0)
            except:
                continue
        print
        #imageCopy = seg.mark_boundaries(image, segments)
        colorList.append((0,0,0))
        """for i in range(len(medianTuples)):
           ax.scatter(medianTuples[i][0], medianTuples[i][1], medianTuples[i][2], c = colorList[labels[i]], s = 20)
        #ax.imshow(imageCopy)
        #plt.axis("off")
        fig3 = plt.figure("Layered")
        ax3 = fig3.add_subplot(111)
        ax3.imshow(imageCopy)
        fig2 = plt.figure("Raw Image")
        ax2 = fig2.add_subplot(1,1,1)
        ax2.imshow(image)
        plt.show()"""
        return imageCopy, [labelledSegments, labels, n_clusters_]
    except:
        return image

