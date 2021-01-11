from flask import Flask, request
from flask import current_app as app

from controllers.actor import *
from controllers.movie import *


@app.route('/api/actors', methods=['GET'])
def actors():
    """
    Get all actors in db
    """
    return get_all_actors()


@app.route('/api/movies', methods=['GET'])
def movies():
    """
    Get all movies in db
    """
    return get_all_movies()


@app.route('/api/actor', methods=['GET', 'POST', 'PUT', 'DELETE'])
def actor():
    """
    Manipulate with the actors records, methods
    """

    if request.method == 'GET':
        return get_actor_by_id()

    elif request.method == 'POST':
        return add_actor()

    elif request.method == 'PUT':
        return update_actor()

    elif request.method == 'DELETE':
        return delete_actor()


@app.route('/api/movie', methods=['GET', 'POST', 'PUT', 'DELETE'])
def movie():
    """
    Manipulate with the movies records, methods
    """

    if request.method == 'GET':
        return get_movie_by_id()

    elif request.method == 'POST':
        return add_movie()

    elif request.method == 'PUT':
        return update_movie()

    elif request.method == 'DELETE':
        return delete_movie()  


@app.route('/api/actor-relations', methods=['PUT', 'DELETE'])
def actor_relations():

    """
    Manipulate with actor's relations, methods:
    """
    if request.method == 'PUT':
        return actor_add_relation()
    elif request.method == 'DELETE':
        return actor_clear_relations()


@app.route('/api/movie-relations', methods=['PUT', 'DELETE'])
def movie_relations():

    """
    Manipulate with movie's relations, methods:
    """
    if request.method == 'PUT':
        return movie_add_relation()
    elif request.method == 'DELETE':
        return movie_clear_relations()