from flask import request


def get_request_data():
    """
    Get keys & values from request (Note that this method should parse requests with content type "application/x-www-form-urlencoded")
    """
    
    if request.form.to_dict() == {}:
        data = request.args.to_dict()
    elif request.args.to_dict() == {}:
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

    print("data.keys()")
    print(request.args.to_dict().keys())
  
    print("name in data.keys()")
    print("name" in request.args.to_dict().keys())

    print("request.is_json")
    print(request.is_json)

    return data
