__author__ = 'SHREYA'
# Gets rid of tags without any feature vectors, filters out erroneous data, and generates a new file of feature vectors with valid tags
import json

def load_json():
    featureVectorFile = open('featureVectors.txt')
    outputFile = open('refinedFeatureVectors.json', 'w+')
    featureVectors = featureVectorFile.read()
    featureVectors = json.loads(featureVectors)
    refinedData = {}
    for tag in featureVectors:
        print tag
        if featureVectors[tag] != []:
            refinedData[tag] = featureVectors[tag]

    json.dump(refinedData, outputFile)
    featureVectorFile.close()
    outputFile.close()

load_json()