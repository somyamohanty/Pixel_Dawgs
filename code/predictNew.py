__author__ = 'SHREYA'

# File that does the actual prediction
from sklearn import svm
from sklearn.externals import joblib

def predictNew(featureVector):
    clf = joblib.load('./fittedModels/fittedModel.pkl')
    probs = []
    for feature in featureVector:
        probs.append(zip(clf.classes_, clf.predict_proba(feature)[0]))

    count = 0
    probThresh = []
    for probabilities in probs:
        count += 1
        for prob in probabilities:
            if prob[1] > 0.2:
                probThresh.append(prob)

    tagDict = {}
    for cl in clf.classes_ :
        tagDict[cl] = []

    for prob in probThresh:
        tagDict[prob[0]].append(prob[1])

    for tag in tagDict:
        if len(tagDict[tag]):
            tagDict[tag] = [sum(tagDict[tag])/len(tagDict[tag])]

    """for tag in tagDict:
        if len(tagDict[tag]):
            if tagDict[tag][0] > 0.3:
                print tag, tagDict[tag]
    """
    topList = []
    for key in tagDict:
        for value in tagDict[key]:
            topList.append([key,value])

    topList.sort(key=lambda topList:topList[1], reverse = True)
    print topList[0:5]

