import cv2
from matplotlib import pyplot as plt
import glob
import os
import csv
import numpy as np
import pandas as pd
import multiprocessing as mp
import clustering as cl
from skimage import io

__author__ = 'nrosetti94'
__main__ = 1

targetDir = "sampleimages\\"

def loadTagMap():
    tagsDict = []
    with open("Tagsmap.csv") as csvFile:
        tags = csv.reader(csvFile, delimiter=",")

        for row in tags:
            tagsDict.append([row[0],row[1:]])
    return tagsDict

def loadIds(start, end):
    imageIds = []
    with open("validTags.csv") as tagFile:
        tags = csv.reader(tagFile, delimiter=",")
        count = 0
        for line in tags:
            if count < start:
                continue
            if count > end:
                break

            imageIds.append(line[0])
            count += 1

    return imageIds


def loadImage(id):
    filename = targetDir + id + ".jpg"
    image = io.imread(filename)
    if image == None:
        return None
    if len(image.shape) == 3:
        return image
    return None


def getHistogram(image):
    #this should give just the Cr and Cb channels
    hist = cv2.calcHist([image], [0, 1, 2], None, [180, 256, 256], [0, 180, 0, 256, 0, 256])

    return hist
    """Y = cv2.calcHist(c1, [0], None, [256], [0, 256])
    Cr = cv2.calcHist(c2, [0], None, [256], [0, 256])
    Cb = cv2.calcHist(c3, [0], None, [256], [0, 256])

    return [Y, Cr, Cb]"""

def segmentImage(*args):
    id = args[0]

    print "Start id: " + str(id)

    image = loadImage(id)
    if not image == None:
        segmented, labels = cl.slic(image)
        io.imsave("segmented/" + str(id) + ".jpg", image)
        io.imsave("segmented/" + str(id) + "_segmented.jpg", segmented)

    print "Finish id: " + str(id)

def readImagePoints(id, pointList):
    image = loadImage(id)
    if not image == None:
        segmented, labels = cl.slic(image)
        segments = labels[0]
        n_clusters = labels[2]
        labels = labels[1]

        print labels[labels == 0]

def writeCompositeHistograms(tags, hist):
    histDict = {}

    count = 0
    for tag in tags:
        histDict[tag] = hist[count]
        count += 1

    np.savez('histogram',  **histDict)


def getTopTags():
    tagIds = loadTagMap()

    tagsCount = []
    tags = []
    for tag in tagIds:
        tags.append(tag[0])
        tagsCount.append(len(tag[1]))
    tagsDf = pd.DataFrame(tagsCount, index=tags)
    print tagsDf.rank(pct=True) > 0.99
    tagsDf = tagsDf[0][tagsDf[0].rank(pct=True) > 0.995]
    topTags = tagsDf.index.values
    print topTags
    tagsDict = {}

    for tag in tagIds:
        tagsDict[tag[0]] = tag[1]

    return topTags, tagsDict

def startSegment( imageIds):
    p = mp.Pool(1)

    p.map(segmentImage, imageIds)
    #writeCompositeHistograms(topTags, compositeHists)

def calcBackProject(image, tags, histograms):
    probability = {}

    cl.kmeans(image)

    for tag in tags:
        print tag
        result = cv2.calcBackProject([image], [0, 1, 2], histograms[tag], [0, 180, 0, 256, 0, 256], 1)

        probabilityValue = cv2.countNonZero(result)/float(image.shape[0] * image.shape[1])
        probability[tag] = probabilityValue

    return probability

def loadHistograms():
    hists = np.load('histogram.npz')

    tagsFile = open('topTags.txt', 'rU')
    tags = []
    for line in tagsFile:
        tags.append(line.rstrip())

    return tags, hists

def main():
    #readImagePoints('100346')
    imageIds = loadIds(0, 4000)
    startSegment(imageIds)

    #tags, histograms = loadHistograms()

if __name__ == '__main__':
    main()


"""
plt.imshow(tagsDict[tags[0][0]])
plt.show()

color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv2.calcHist([images[1]],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
"""