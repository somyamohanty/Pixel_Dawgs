import cv2
from matplotlib import pyplot as plt
import glob
import os
import csv
import numpy as np
import pandas as pd

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
    print tagsDf
    topTags = tagsDf.index.values
    tagsDict = {}

    for tag in tagIds:
        tagsDict[tag[0]] = tag[1]

    #createCompositeHistogram(tagsDict[topTags[0]])


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