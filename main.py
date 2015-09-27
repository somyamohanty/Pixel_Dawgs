import cv2
from matplotlib import pyplot as plt
import glob
import os
import csv
import numpy as np
import pandas as pd

__author__ = 'nrosetti94'
__main__ = 1

targetDir = "C:\Users\\nrosetti94\Documents\Flickr\sampleimages\\"

def findValidImageTags():
    print targetDir
    filepaths = []
    imageIds = []
    for subdir, dirs, files in os.walk(targetDir):
        for file in files:
            if(file.endswith('.jpg')):
                imageIds.append(file.rpartition('.')[0])
                filepaths.append(subdir + os.sep + file)

    """images = [(cv2.imread(filepath)) for filepath in filepaths]

    for i in range(0, len(images)):
        if len(images[i].shape) == 3:
            images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)

    imageIds = [imageIds]
    imageIds = [list(x) for x in zip(*imageIds)]"""

    tagsFile = open("C:/Users/nrosetti94/Desktop/yfcc100m_autotags-v1", "r")

    idArray = imageIds
    print idArray

    count = 0
    index = 0
    idxs = []
    newIdList = []
    with open("C:/Users/nrosetti94/Desktop/yfcc100m_autotags-v1", "r") as tags:
        for line in tags:
            tag = line.split('\t')
            if tag[0] in idArray:
                idx = idArray.index(tag[0])
                newIdList.append([imageIds[idx], tag[1].strip('\n')])
                idxs.append(idx)
                print count
                count += 1

    fileOut = open("validTags.csv", 'w')

    for i in range(len(newIdList)):
        fileOut.write(newIdList[i][0] + ',' + newIdList[i][1] + '\n')

    fileOut.close()

def loadTagMap():
    tagsDict = []
    with open("Tagsmap.csv") as csvFile:
        tags = csv.reader(csvFile, delimiter=",")
        for row in tags:
            tagsDict.append([row[0],row[1:]])
    return tagsDict

def loadImage(id):
    filename = targetDir + id + ".jpg"
    print filename
    return cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2YCR_CB)

def createCompositeHistogram(imageIds):
    images = []
    for id in imageIds:
        images.append(loadImage(id))

    plt.imshow(images[0])
    plt.show()

    color = ('y','r','b')
    for i,col in enumerate(color):
        histr = cv2.calcHist([images[0]],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

def main():
    tagIds = loadTagMap()

    tagsCount = []
    tags = []
    for tag in tagIds:
        tags.append(tag[0])
        tagsCount.append(len(tag[1]))
    tagsDf = pd.DataFrame(tagsCount, index=tags)
    tagsDf = tagsDf[0][tagsDf[0] > 40]

    topTags = tagsDf.index.values
    tagsDict = {}

    for tag in tagIds:
        tagsDict[tag[0]] = tag[1]

    createCompositeHistogram(tagsDict[topTags[0]])


if __main__:
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