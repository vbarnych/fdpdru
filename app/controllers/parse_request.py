from flask import request


def get_request_data():
    """
    Get keys & values from request (Note that this method should parse requests with content type "application/x-www-form-urlencoded")
    """
    if request.is_json:
        data = request.json
    else:
        data = request.form.to_dict()
    return data