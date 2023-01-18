from os import listdir
from os.path import isfile, join
from collections import Counter
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm, linear_model, cluster
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.svm import OneClassSVM
from sklearn.metrics import roc_curve, roc_auc_score

if __name__ == '__main__':
    print('All essential libraries are available!')