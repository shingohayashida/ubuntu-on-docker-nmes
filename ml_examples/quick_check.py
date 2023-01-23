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
    dat=np.array([[0,1,2,3,4], [0,1,2,3,4]])
    plt.scatter(x=dat[0], y=dat[1], label='test')
    plt.legend()
    plt.show()
    print('All essential libraries are available!')
