from flask import request


def get_request_data():
    """
    Get keys & values from request (Note that this method should parse requests with content type "application/x-www-form-urlencoded")
    """
    data = 0
    if request.is_json:
        data = request.json
    else:
        data = request.form.to_dict()

    print("request")
    print(request)

    print("request.json")
    print(request.json)

    print("request.form")
    print(request.form)

    print("request.form.to_dict()")
    print(request.form.to_dict())

    print("request.args.to_dict()")
    print(request.args.to_dict())
    return request.args.to_dict()
