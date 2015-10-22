import os
import csv
import sqlite3 as sql

__author__ = 'SATYANARAYANAREDDY'
__main__ = 1
targetDir = "sampleimages\\"

#conn = sql.connect('autotags.db')

def createTagsTable():
    with open("trainingset/yfcc100m_autotags-v1", "r") as tags:
        for line in tags:
            tag = line.split('\t')

def generateTagMap():
    tags_dictionary = {}
    fi = open("validTags.csv")
    for each in fi:
        sep_values = each.split(",")
        image_id = sep_values[0]
        for i in range(1, len(sep_values)):
            tag = sep_values[i].split(":")[0]
            if tag not in tags_dictionary.keys():
                tags_dictionary[tag] = []
            tags_dictionary[tag].append(image_id)

    strinlist = []
    for each in tags_dictionary:
        strin = each
        for id in tags_dictionary[each]:
            if id != tags_dictionary[each][-1]:
                strin = strin + "," + id
            else:
                strin = strin+","+id+"\n"
        strinlist.append(strin)

    outfil = open("Tagsmap.csv", "w")
    strinlist.sort()
    for st in strinlist:
        outfil.write(st)

def findValidImageTags():
    print targetDir
    filepaths = []
    imageIds = []
    for subdir, dirs, files in os.walk(targetDir):
        for file in files:
            if(file.endswith('.jpg')):
                imageIds.append(file.rpartition('.')[0])
                filepaths.append(subdir + os.sep + file)

    idArray = imageIds

    count = 0
    index = 0
    idxs = []
    newIdList = []

    tagsDict = {}
    with open("trainingset/autotags-1", "rU") as tags:
        for line in tags:
            tag = line.split('\t')
            if(len(tag) == 2):
                tagsDict[tag[0]] = tag[1]

    for id in idArray:
        try:
            newIdList.append([id, tagsDict[id]])
        except:
            continue

    tagsDict.clear()
    with open("trainingset/autotags-2", "rU") as tags:
        for line in tags:
            tag = line.split('\t')
            if(len(tag) == 2):
                tagsDict[tag[0]] = tag[1]

    for id in idArray:
        try:
            newIdList.append([id, tagsDict[id]])
        except:
            continue

    tagsDict.clear()
    with open("trainingset/autotags-3", "rU") as tags:
        for line in tags:
            tag = line.split('\t')
            if(len(tag) == 2):
                tagsDict[tag[0]] = tag[1]

    for id in idArray:
        try:
            newIdList.append([id, tagsDict[id]])
        except:
            continue

    fileOut = open("validTags.csv", 'w')

    for i in range(len(newIdList)):
        fileOut.write(newIdList[i][0] + ',' + newIdList[i][1])

    fileOut.close()

def splitTags():
    tagsFile1 = open("trainingset/autotags-1", "w")
    tagsFile2 = open("trainingset/autotags-2", "w")
    tagsFile3 = open("trainingset/autotags-3", "w")

    tags = open("trainingset/yfcc100m_autotags-v1", "rU")
    count = 0
    while 1:
        count += 1
        line = tags.readline()
        if not line:
            break

        if(count < 35000000):
            tagsFile1.write(line)
        elif (count < 70000000):
            tagsFile2.write(line)
        else:
            tagsFile3.write(line)

    tagsFile1.close()
    tagsFile2.close()
    tagsFile3.close()

if __main__:
    splitTags()
    findValidImageTags()
    generateTagMap()
