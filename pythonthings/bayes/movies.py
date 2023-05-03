import numpy as np
from collections import defaultdict
from pathlib import Path
from sklearn.model_selection import train_test_split as sklearn_train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

# _data_path = '..datasets/movielens/ratings.csv'
_n_users = 6040
_n_movies = 37060

_base_path = Path(__file__).parent.parent
_data_path = _base_path / "./datasets/movielens/ratings.csv"


class MovieRating():
    """
    A class to produce movie recs from the movielens dataset
    """

    def __init__(self, n_users, n_movies, datapath):
        """
        instantiates the class
        """
        self.data_path = datapath
        self._n_users = n_users
        self._n_movies = n_movies


    def load_rating_data(self, data_path, n_users, n_movies):
        """
        Loads rating data from file and returns the number of ratings for
        each movie and movie_id index mapping

        @param data_path:   path to the rating data 
        @param  n_users:    number of users
        @param n_movies:    number of movies with ratings
        
        @return:            - rating data in the numpy array of [user,movie]
                            - movie_n_rating, {movie_id: number of ratings}
                            - movie_id_mapping, {movie_id: column index in rating data}
        """

        data = np.zeros([n_users,n_movies], dtype=np.float32)
        movie_id_mapping = {}
        movie_n_rating = defaultdict(int)
        with data_path.open() as file: # open(data_path, 'r') as file:
            for line in file.readlines()[1:]:
                user_id, movie_id, rating, _ = line.split(",")
                user_id = int(user_id) - 1
                
                if movie_id not in movie_id_mapping:
                    movie_id_mapping[movie_id] = len(movie_id_mapping)

                rating = float(rating)
                data[user_id, movie_id_mapping[movie_id]] = rating
                if rating > 0:
                    movie_n_rating[movie_id] += 1
                
        return data, movie_n_rating, movie_id_mapping

    def display_distribution(self, data):
        """
        Displays the distribution of the given data
        """
        values, counts = np.unique(data, return_counts=True)
        for value, count in zip(values, counts):
            print(f'number of rating {int(value)}: {count}')


mr = MovieRating(_n_users, _n_movies, _data_path)
data, movie_n_rating, movie_id_mapping = mr.load_rating_data(_data_path, _n_users, _n_movies)
mr.display_distribution(data)

movie_id_most, n_rating_most = sorted(movie_n_rating.items(), 
    key = lambda d: d[1], reverse=True)[0]
print(f'Movie ID {movie_id_most} has {n_rating_most} ratings.')



X_raw = np.delete(data, movie_id_mapping[movie_id_most], axis=1)
Y_raw = data[:, movie_id_mapping[movie_id_most]]
X = X_raw[Y_raw > 0]
Y = Y_raw[Y_raw > 0]
print(f'shape of X: {X.shape}')
print(f'shape of Y: {Y.shape}')

mr.display_distribution(Y)

recommend = 3
Y[Y < recommend] = 0
Y[Y > recommend] = 1
n_pos = (Y == 1).sum()
n_neg = (Y == 0).sum()
print(f'{n_pos} positive samples and {n_neg} samples')

# from sklearn.model_selection import train_test_split
sklearn_train_test_split
X_train, X_test, Y_train, Y_test = sklearn_train_test_split(X,Y,test_size=0.2, random_state=42)

print(len(Y_train), len(Y_test))


clf = MultinomialNB(alpha=1.0, fit_prior=True)
clf.fit(X_train, Y_train)

prediction_prob = clf.predict_proba(X_test)
print(prediction_prob[0:10])

prediction = clf.predict(X_test)
print(prediction[:10])


accuracy = clf.score(X_test, Y_test)
print(f'the accuracy is: {accuracy * 100: 0.1f}%')

print(confusion_matrix(Y_test, prediction, labels=[0, 1]))