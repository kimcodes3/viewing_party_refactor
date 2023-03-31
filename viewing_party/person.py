from viewing_party.movie import Movie

class Person:
    def __init__(self, name, friends, watch_list):
        self.name = name
        self.friends = friends
        self.watch_list = watch_list
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_movie_to_watchlist(self, movie):
        if movie not in self.watch_list:
            self.watch_list.append(movie)
    
