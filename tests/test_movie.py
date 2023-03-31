import pytest
from viewing_party.movie import Movie

def test_movie_object_instance():
    # Arrange/Act
    movie = Movie("Jaws", "Horror", 4)
    
    # Assert
    assert movie.title == "Jaws"
    assert movie.genre == "Horror"
    assert movie.rating == 4