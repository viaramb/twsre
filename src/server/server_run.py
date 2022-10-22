from api.storage_box import endpoint
import flask

app = flask.Flask(__name__)
app.config.from_pyfile('api/config.py')


@app.route('/api/v1/cache', methods=['GET'])
def cache():
    return endpoint('Cache')


@app.route('/api/v1/webapp', methods=['GET'])
def webapp():
    return endpoint('Webapp')


@app.route('/api/v1/database', methods=['GET'])
def database():
    return endpoint('Database')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')  # Change IP to 0.0.0.0 for a Docker Container.
