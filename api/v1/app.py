#!/usr/bin/python3
""" flask """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
host = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
port = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else 5000


@app.teardown_appcontext
def teardown_db(self):
    """ teardown """
    storage.close()


@app.errorhandler(404)
def page_not_found_e(e):
    """ Error message """
    return (jsonify({"error": "Not found"})), 404

if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
