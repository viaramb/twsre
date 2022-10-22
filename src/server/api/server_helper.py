import random


def generate_random_vars() -> (int, int, int):
    """Generate random values to emulate real life data"""
    request = random.randrange(5194800000, 5194800999)
    error_count = random.randrange(0, 5000)
    success_count = request - error_count
    return request, error_count, success_count


def generate_version_nums(server_type) -> str:
    """Build version based on x.x.x format"""
    assert isinstance(server_type, str), "Server type should be string"
    major_ver = random.randrange(0, 2)
    mid_ver = random.randrange(0, 3)
    if server_type == 'Cache':
        minor_ver = random.randrange(1, 4)
    else:
        minor_ver = random.randrange(0, 3)
    version = f'{major_ver}.{mid_ver}.{minor_ver}'
    return version


def get_server_type(app_type) -> str:
    """Convert app_type value to resource name or type"""
    assert isinstance(app_type, int), "Application type should be integer"
    if app_type == 0:
        return "Cache"

    if app_type == 1:
        return "Database"

    if app_type == 2:
        return "Webapp"
