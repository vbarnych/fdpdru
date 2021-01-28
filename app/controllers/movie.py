from flask import jsonify, make_response

from ast import literal_eval

from models import Actor, Movie
from settings.constants import MOVIE_FIELDS  # to make response pretty
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        act = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(act)
    return make_response(jsonify(movies), 200)


def get_movie_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Movie.query.filter_by(id=row_id).first()
        try:
            movie = {k: v for k, v in obj.__dict__.items() if k in MOVIE_FIELDS}
            print(movie)
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(movie), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def add_movie():
    """
    Add new movie
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    if 'year' in data.keys():
        try:
            year = int(data['year'])
        except:
            err = 'Year must be integer'
            return make_response(jsonify(error=err), 400)

    try:
        new_record = Movie.create(**data)
        new_movie = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
    except:
        err = "Invalid keys in dict for creating new movie"
        return make_response(jsonify(error=err), 400)

    return make_response(jsonify(new_movie), 200)

    ### END CODE HERE ###


def update_movie():
    """
    Update movie record by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

    keys = list(data.keys())
    keys.remove('id')
    for key in keys:
        if key == 'year':
            try:
                year = int(data['year'])
            except:
                err = 'Year must be integer'
                return make_response(jsonify(error=err), 400)
            continue
        elif key == 'name':
            continue
        elif key == 'genre':
            continue
        else:
            err = 'Wrong keys'
            return make_response(jsonify(error=err), 400)
            
    try:
        upd_record = Movie.update(row_id, **data)
        upd_movie = {k: v for k, v in upd_record.__dict__.items() if k in MOVIE_FIELDS}
        return make_response(jsonify(upd_movie), 200)
    except:
        err = 'Record with such id does not exist'
        return make_response(jsonify(error=err), 400)

    ### END CODE HERE ###


def delete_movie():
    """
    Delete movie by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        del_record = Movie.delete(row_id)
        if del_record:
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

    ### END CODE HERE ###


def movie_add_relation():
    """
    Add actor to movie's cast
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            row_id = int(data['id'])
            relation_id = int(data['relation_id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        actor = Actor.query.filter_by(id=relation_id).first()
        if actor is None:
            err = 'Record with such id for actor does not exist'
            return make_response(jsonify(error=err), 400)

        try:
            movie = Movie.add_relation(row_id, actor)
            rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
            rel_movie['cast'] = str(movie.cast)
        except:
            err = 'Record with such id for movie does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(rel_movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

    ### END CODE HERE ###


def movie_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        try:
            movie = Movie.clear_relations(row_id)
            rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
            rel_movie['cast'] = str(movie.cast)
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(rel_movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

    ### END CODE HERE ###
