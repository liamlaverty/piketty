from collections import defaultdict
from naivebayessettings import NaiveBayesSettings


class NaiveBayes: 
    """
    A class which implements Naive Bayes
    """


    def get_label_indices(self, labels): 
        """
        Group samples based on thier labels and return indeces

        @param labels:      list of labels
        @return:            dict, {class1: [indices], class2: [indices]}
        """

        label_indices = defaultdict(list)

        for index, label in enumerate(labels):
            label_indices[label].append(index)
        
        return label_indices


    def get_prior(self, label_indices):
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


    def get_likelihood(self, features, label_indices, smoothing = 1):
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


    def get_posterior(self, X, prior, likelihood):
        """
        Compute posterior of testing samples, based on prior and likelihood

        @param X:           testing samples
        @param prior:       dictionary, with class label as its key, and the prior as the value
        @param likelihood:  dictionary with class label as its key, and conditional probability vector as its value

        @return:            dictionary with class label as its key, and posterior as its value
        """

        posteriors = []
        for x in X:
            # posterior is proportional to prior * likelihood
            posterior = prior.copy()
            for label, likelihood_label in likelihood.items():
                for index, bool_value in enumerate(x):
                    if (bool_value):
                        posterior[label] *= likelihood_label[index] 
                    else: 
                        posterior[label] *= (1 - likelihood_label[index])
            
            #normalize so that the results sum up to 1
            sum_posterior = sum(posterior.values())
            for label in posterior:
                if posterior[label] == float('inf'):
                    posterior[label] = 1.0
                else:
                    posterior[label] /= sum_posterior
            
            posteriors.append(posterior.copy())
        
        return posteriors



nb = NaiveBayes()
naivebayessettings = NaiveBayesSettings()



label_indices = nb.get_label_indices(naivebayessettings.Y_train)
print('label_indices:\n', label_indices)

prior = nb.get_prior(label_indices)
print('prior:\n', prior)



smoothing = 1
likelihood = nb.get_likelihood(naivebayessettings.X_train, label_indices, smoothing)
print('Likelihood (smoothing={}):{}'.format(smoothing, likelihood))


posterior = nb.get_posterior(naivebayessettings.X_test, prior, likelihood)
print('Posterior:\n {}'.format(posterior))