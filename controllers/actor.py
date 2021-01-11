from flask import jsonify, make_response

from datetime import datetime as dt
from ast import literal_eval

from models import Actor, Movie
from settings.constants import ACTOR_FIELDS     # to make response pretty
from .parse_request import get_request_data


def get_all_actors():
    """
    Get list of all records
    """  
    all_actors = Actor.query.all()
    actors = []
    for actor in all_actors:
        act = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        actors.append(act)
    return make_response(jsonify(actors), 200) 

  
def get_actor_by_id():
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

        obj = Actor.query.filter_by(id=row_id).first()
        try:
            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400) 

        return make_response(jsonify(actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400) 


def add_actor():
    """
    Add new actor
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    if 'name'in data.keys():
        try:
            new_record = Actor.create(**data)
        except:
            err = "Incorrect data format"
            return make_response(jsonify(error=err), 400)

        new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}
        return make_response(jsonify(new_actor), 200)

    else :
        err = 'No name specified'
        return make_response(jsonify(error=err), 400)

    


def update_actor():
    """
    Update actor record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if Actor.query.filter_by(id=data['id']).first() == None:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if 'name' in data.keys():
            if Actor.query.filter_by(name=data['name']).first() != None:
                actor = Actor.query.filter_by(name=data['name']).first()
                err = {k: v for k, v in actor.__dict__.items() if k == 'id'}
                row_id = int(err['id'])

        for key in data.keys():
            if key not in ACTOR_FIELDS:
                err = 'fields does not exist in Actor table'
                return make_response(jsonify(error=err), 400)

        try:
            new_record = Actor.update(row_id, **data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}
        return make_response(jsonify(new_actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)



def delete_actor():
    """
    Delete actor by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
        index = Actor.delete(row_id)
        if index == 1:
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def actor_add_relation():
    """
    Add a movie to actor's filmography
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

            if Movie.query.filter_by(id=rel_id).first() != None:
                rel_obj = Movie.query.filter_by(id=rel_id).first()
            else:
                err = 'Record with such relation_id does not exist'
                return make_response(jsonify(error=err), 400)

            try:
                actor = Actor.add_relation(row_id, rel_obj)
            except:
                err = 'Record with such id does not exist'
                return make_response(jsonify(error=err), 400)

            rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
            rel_actor['Movie'] = str(actor.Movie)
            return make_response(jsonify(rel_actor), 200)

        else:
            err = 'No relation-id specified'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def actor_clear_relations():
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
            actor = Actor.clear_relations(row_id) # clear relations here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        rel_actor['Movie'] = str(actor.Movie)
        return make_response(jsonify(rel_actor), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
