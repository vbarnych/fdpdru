from flask import jsonify, make_response

from ast import literal_eval

from models import Movie, Actor
from settings.constants import MOVIE_FIELDS
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        mov = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(mov)
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
            movie = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
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

    
    data = get_request_data()
    if 'name' in data.keys():
        try:
            new_record = Movie.create(**data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_movie = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
        return make_response(jsonify(new_movie), 200)
    else:
        err = 'No name specified'
        return make_response(jsonify(error=err), 400)


def update_movie():
    """
    Update movie record by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if Movie.query.filter_by(id=data['id']).first() == None:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if 'name' in data.keys():
            if Movie.query.filter_by(name=data['name']).first() != None:
                movie = Movie.query.filter_by(name=data['name']).first()
                err = {k: v for k, v in movie.__dict__.items() if k == 'id'}
                row_id = int(err['id'])

        for key in data.keys():
            if key not in MOVIE_FIELDS:
                err = 'fields does not exist in Movie table'
                return make_response(jsonify(error=err), 400)

        try:
            new_record = Movie.update(row_id, **data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_movie = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
        return make_response(jsonify(new_movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def delete_movie():
    """
    Delete movie by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
        index = Movie.delete(row_id)
        if index == 1:
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
    

def movie_add_relation():
    """
    Add actor to movie's cast
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if 'relation_id' in data.keys():
            try:
                rel_id = int(data['relation_id'])
            except:
                err = 'relation_id must be integer'
                return make_response(jsonify(error=err), 400)

            if Actor.query.filter_by(id=rel_id).first() != None:
                rel_obj = Actor.query.filter_by(id=rel_id).first()
            else:
                err = 'Record with such relation_id does not exist'
                return make_response(jsonify(error=err), 400)

            try:
                movie = Movie.add_relation(row_id, rel_obj)
            except:
                err = 'Record with such id does not exist'
                return make_response(jsonify(error=err), 400)

            rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
            rel_movie['Actor'] = str(movie.Actor)
            return make_response(jsonify(rel_movie), 200)

        else:
            err = 'No relation-id specified'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def movie_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        try:
            movie = Movie.clear_relations(row_id) # clear relations here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        rel_movie['Actor'] = str(movie.Actor)
        return make_response(jsonify(rel_movie), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)