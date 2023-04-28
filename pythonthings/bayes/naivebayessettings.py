import numpy as np

class NaiveBayesSettings:
    """
    a class to contain static settings for the 
    naive bayes lessons
    """
    X_train = np.array([
        [0,1,1],
        [0,0,1],
        [0,0,0],
        [1,1,0]
    ])

    Y_train = ['Y','N','Y','Y']
    X_test = np.array([[1, 1, 0]])