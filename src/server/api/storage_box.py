import random
from .server_helper import (generate_random_vars,
                            generate_version_nums)
from flask import jsonify


def endpoint(app_type) -> dict:
    assert isinstance(app_type, str), "Type Error, need a string"
    request, error_count, success_count = generate_random_vars()
    app_number = random.randrange(0, 3)
    app_name = f'{app_type}{app_number}'
    version = generate_version_nums(app_type)
    app_dict = {"application": app_name,
                "version": version,
                "requests_count": request,
                "error_count": error_count,
                "success_count": success_count}
    response = jsonify(app_dict)
    return response
