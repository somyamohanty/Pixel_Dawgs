__author__ = 'nrosetti94'

import numpy as np
from sklearn.decomposition import PCA

def generateFeatureVectors(possibleTags, possibleTagsDict, possibleTagsDictSobel):
    featureVectors = {}
    binVals = []

    for tag in possibleTags:
        featureVectors[tag[0]] = []
        combinedSegments = None
        count = 0
        for i in range(0, len(possibleTagsDict[tag[0]])):

            segment = possibleTagsDict[tag[0]][i]


            featureVectors[tag[0]].append((np.median(segment, axis=0).tolist() + np.std(segment, axis=0).tolist()))
            if count == 0:
                combinedSegments = np.array(segment)
            else:
                combinedSegments = np.append(combinedSegments, np.array(segment), axis=0)
            count += 1
        if combinedSegments != None:
            possibleTagsDict[tag[0]] = combinedSegments
            #features = [np.mean(combinedSegments, axis=0), np.std(combinedSegments, axis=0)]
            #print tag[0] + str(features)
            #featureVectors[tag[0]] = [np.mean(combinedSegments)]
        print tag[0] + " " + str(featureVectors[tag[0]])

    return featureVectors

def getImageFeatureVectors(segments, sobels):
    featureVectors = []
    binVals = []

    for i in range(0, len(segments)):
        sobel = sobels[i]
        segment = segments[i]

        #featureVectors.append(np.array(fit).tolist()  + [sobel])
        featureVectors.append((np.median(segment, axis=0).tolist() + np.std(segment, axis=0).tolist()))

    return featureVectors