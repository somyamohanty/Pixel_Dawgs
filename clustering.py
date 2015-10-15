import cv2
from matplotlib import pyplot as plt
import numpy as np
import skimage
import skimage.segmentation as seg
import skimage.color as skcol
from skimage.util import img_as_float
from scipy import ndimage as ndi
from scipy import stats
import sklearn.cluster as skcl
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
    numSegments = 300
    imageCopy = img_as_float(image)
    segments = seg.slic(imageCopy, numSegments, 5, 2, 1, convert2lab=True, enforce_connectivity=True)
    fig = plt.figure("Superpixels -- %d segments" % (numSegments))
    ax = fig.add_subplot(1, 1, 1)
    medianTuples = []
    for i in range(numSegments):
        if imageCopy[segments == i].shape[0] > 0:
            medianTuples.append([np.nanmedian(imageCopy[segments == i][:,1]), np.nanmedian(imageCopy[segments == i][:,2])])

    print medianTuples
    medianTuples = np.array(medianTuples)
    cv2.normalize(medianTuples, medianTuples, 0, 255, cv2.NORM_MINMAX)
    db = skcl.DBSCAN(eps = 8).fit(medianTuples)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    print labels
    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    col = []
    for cluster in range(n_clusters_):
        col.append(np.random.rand(3,))
    for i in range(numSegments):
        try:
            if(labels[i] == -1):
                imageCopy[segments == i] = (0,0,0)
            else:
                imageCopy[segments == i] = col[labels[i]]
        except:
            print "some empty segments"
    print n_clusters_

    col.append((0,0,0))
    #for i in range(medianTuples.shape[0]):
    #   ax.scatter(medianTuples[i, 0], medianTuples[i, 1], c = col[labels[i]], s = 40, cmap=plt.cm.Paired)
    ax.imshow(imageCopy)
    plt.axis("off")
    fig2 = plt.figure("Raw Image")
    ax2 = fig2.add_subplot(1,1,1)
    ax2.imshow(image)
    plt.show()