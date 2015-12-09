__author__ = 'SHREYA'

# Loads the feature vectors performs a fit and predict on it, and saves it to disk
from sklearn import svm
import json
from sklearn.externals import joblib

def fitModel():
    featureVectorFile = open('refinedFeatureVectors.json')
    featureVectors = featureVectorFile.read()
    featureVectors = json.loads(featureVectors)
    X, y = [], []
    for tag in featureVectors:
        flag = True
        for vector in featureVectors[tag]:
            if type(vector) is list:
                X.append(vector)
                y.append(tag)
            elif flag:
                print tag
                flag = False
    clf = svm.SVC(gamma=0.001, C=100., probability=True)
    clf.fit(X, y)
    print joblib.dump(clf, './fittedModels/fittedModel.pkl')
    featureVectorFile.close()

fitModel()
