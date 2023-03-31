import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie

def test_create_person():
    # Arrange / Act
    kendall = Person("Kendall", ["Nancy"])

    # Assert
    assert isinstance(kendall, Person)

def test_person_name_is_set_correctly():
    # Arrange / Act
    nancy = Person("Nancy", ["Kendall"])
    danica = Person("Danica", ["Ping"])

    # Assert
    assert nancy.name == "Nancy"
    assert danica.name == "Danica"

def test_person_friends_list_is_set_correctly():
    # Arrange / Act
    ana = Person("Ana", ["Ariel"])

    # Assert
    assert ana.friends == ["Ariel"]

def test_friend_added_to_person():
    # Arrange
    laura = Person("Laura", ["Sage"])

    # Act
    laura.add_friend("Elizabeth")

    # Assert
    assert laura.friends == ["Sage", "Elizabeth"]

def test_no_duplicate_friends_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"])

    # Act
    moyo.add_friend("Sarah")

    # Assert
    assert moyo.friends == ["Sarah"]

def test_append_new_movie():
    #Arrange
    kimberly = Person("Kimberly", ["Ana"], [])

    film = Movie("Juno", "Drama", 3.5)


    #Act
    kimberly.add_movie_to_watchlist(film)

    #Assert
    assert kimberly.watch_list == [film]
    assert len(kimberly.watch_list) == 1

def test_append_duplicate_movie():
    #Arrange
    kimberly = Person("Kimberly", ["Ana"], [])
    film = Movie("Juno", "Drama", 3.5)

    #Act
    kimberly.add_movie_to_watchlist(film)
    kimberly.add_movie_to_watchlist(film)

    #Assert
    assert kimberly.watch_list == [film]
    assert len(kimberly.watch_list) == 1