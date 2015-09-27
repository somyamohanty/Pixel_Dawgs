import os
import csv
import sqlite3 as sql

__author__ = 'SATYANARAYANAREDDY'
__main__ = 1
targetDir = "C:\Users\\nrosetti94\Documents\Flickr\sampleimages\\"

#conn = sql.connect('autotags.db')

def createTagsTable():
    with open("C:/Users/nrosetti94/Desktop/yfcc100m_autotags-v1", "r") as tags:
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

if __main__:
    findValidImageTags()
    generateTagMap()