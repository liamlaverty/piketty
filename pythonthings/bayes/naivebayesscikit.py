from sklearn.naive_bayes import BernoulliNB
from naivebayessettings import NaiveBayesSettings

settings = NaiveBayesSettings()
clf = BernoulliNB(alpha=1.0, fit_prior=True)
clf.fit(settings.X_train, settings.Y_train)

pred_prob = clf.predict_proba(settings.X_test)
print('pred_prob:\n', pred_prob)