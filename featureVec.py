__author__ = 'nrosetti94'

import numpy as np

def generateFeatureVectors(possibleTags, possibleTagsDict):
    featureVectors = {}
    for tag in possibleTags:
        featureVectors[tag[0]] = []
        combinedSegments = None
        count = 0
        for segment in possibleTagsDict[tag[0]]:
            featureVectors[tag[0]].append((np.mean(segment, axis=0).tolist() + np.std(segment, axis=0).tolist()))
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