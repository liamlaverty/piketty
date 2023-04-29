import numpy as np
from collections import defaultdict
_data_path = '/workspaces/piketty/pythonthings/datasets/movielens/ratings.csv'
_n_users = 6040
_n_movies = 37060

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
        with open(data_path, 'r') as file:
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