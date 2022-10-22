def generate_endpoint(app_type: int) -> str:
    """Convert app_type value to resource endpoint"""
    assert isinstance(app_type, int), "Application type should be integer"
    if app_type == 0:
        return "cache"

    if app_type == 1:
        return "database"

    if app_type == 2:
        return "webapp"
