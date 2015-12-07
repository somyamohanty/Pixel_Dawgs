import cv2
from matplotlib import pyplot as plt
import glob
import os
import csv
import numpy as np
import pandas as pd
import multiprocessing as mp
import clustering as cl
import json
from featureVec import generateFeatureVectors
from skimage import io
from dbprocessor import getTaggedImages

from functools import partial

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

def getPossibleTags():
    possibleTags = []
    with open("tagslist.txt") as tagsFile:
        tags = csv.reader(tagsFile)
        for row in tags:
            possibleTags.append(row)

    return possibleTags

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

def getTaggedSegments(id, taggedPoints, possibleTags):

    li = ['tag1c', 'tag2c', 'tag3c', 'tag4c', 'tag5c', 'tag6c', 'tag7c', 'tag8c', 'tag9c', 'tag10c']
    li2 = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10']

    possibleTagsDict = {}
    for tag in possibleTags:
        possibleTagsDict[tag[0]] = []

    print "Processing id: " + id
    for i in range(len(li)):
        newPoints = []
        for point in taggedPoints[id][li[i]]:
            newPoints.append(point.split(':'))

        taggedPoints[id][li[i]] = newPoints

    image = loadImage(id)
    if not image == None:
        segmented, labels = cl.slic(image)
        labelledSegments = labels[0]
        labels = labels[1]
        n_clusters = labels[2]

    for i in range(len(li)):
        for point in taggedPoints[id][li[i]]:
            print point
            for segment in labelledSegments:
                #add list of pixels to corresponding tag
                try:
                    if len(point) == 2:
                        if point[0] != '' and point[1] != '':
                            if segment[int(point[1])][int(point[0])] and taggedPoints[id][li2[i]] != 'None':
                                possibleTagsDict[taggedPoints[id][li2[i]].replace('"', '')].append(image[segment])
                except:
                    continue
    return possibleTagsDict

def readImagePoints():
    li = ['tag1c', 'tag2c', 'tag3c', 'tag4c', 'tag5c', 'tag6c', 'tag7c', 'tag8c', 'tag9c', 'tag10c']
    li2 = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10']
    ids, taggedPointsList = getTaggedImages()
    possibleTagsList = getPossibleTags()

    p = mp.Pool(6)

    tagDicts = p.map_async(partial(getTaggedSegments, possibleTags=possibleTagsList, taggedPoints=taggedPointsList), ids)

    possibleTagsDict = {}
    for tag in possibleTagsList:
        possibleTagsDict[tag[0]] = []

    for dict in tagDicts.get():
        for key in dict:
            for value in dict[key]:
                possibleTagsDict[key].append(value)

    featureVectors = generateFeatureVectors(possibleTagsList, possibleTagsDict)

    with open("featureVectors.txt", 'w') as outFile:
        outFile.write(json.dumps(featureVectors))

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
    readImagePoints()
    #imageIds = loadIds(0, 4000)
    #startSegment(imageIds)

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