__author__ = 'SHREYA'

# File that does the actual prediction
from sklearn import svm
from sklearn.externals import joblib

def predictNew(featureVector):
    clf = joblib.load('./fittedModels/fittedModel.pkl')
    print clf.predict(featureVector)