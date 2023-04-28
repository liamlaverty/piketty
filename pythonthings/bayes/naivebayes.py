import numpy as np
from collections import defaultdict


X_train = np.array([
    [0,1,1],
    [0,0,1],
    [0,0,0],
    [1,1,0]
])

Y_train = ['Y','N','Y','Y']
X_test = np.array([[1, 1, 0]])



def get_label_indices(labels): 
    """
    Group samples based on thier labels and return indeces

    @param labels:      list of labels
    @return:            dict, {class1: [indices], class2: [indices]}
    """

    label_indices = defaultdict(list)

    for index, label in enumerate(labels):
        label_indices[label].append(index)
    
    return label_indices


def get_prior(label_indices):
    """
    Compute prior based on training samples

    @param label_indices:   grouped sample indices by class
    @return:                dictionary, with class label as `key`, prior as the `value`
    """

    prior = { label: len(indices) for label, indices in label_indices.items()}
    total_count = sum(prior.values())
    
    for label in prior:
        prior[label] /= total_count
    
    return prior


def get_likelihood(features, label_indices, smoothing = 1):
    """
    Compute the likelihood based on training samples

    @param features :       matrix of features
    @param label_indices:   grouped sample indices by class
    @param smoothing:       integer, additive smoothing parameter
    @return:                dictionary
    """

    likelihood = {}
    for label, indices in label_indices.items():
        likelihood[label] = features[indices, :].sum(axis=0) + smoothing
        total_count = len(indices)
        likelihood[label] = likelihood[label] / (total_count + 2 * smoothing)

    return likelihood



label_indices = get_label_indices(Y_train)
print('label_indices:\n', label_indices)

prior = get_prior(label_indices)
print('prior:\n', prior)



for i in range(3):
    smoothing = i
    likelihood = get_likelihood(X_train, label_indices, smoothing)
    print('Likelihood (smoothing={}):{}'.format(smoothing, likelihood))


