import requests
import logging
import urllib3
from requests.exceptions import HTTPError

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_data(url: str) -> requests.get:
    assert isinstance(url, str), "URL should be a string"
    try:
        response = requests.get(url=url,
                                headers={'content-type': 'application/json; charset=utf-8'},
                                verify=False)
        response.raise_for_status()
    except HTTPError as err:
        logging.exception(f"Connection failure {err}")
        raise err
    else:
        return response


if __name__ == '__main__':
    r = get_data("https://127.0.0.1:5000/api/v1/cache")
    if r.status_code == 200:
        print(r.json())
    else:
        print('try again')
