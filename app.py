#!/usr/bin/env python3

import os
import json
from datetime import datetime

import slacker
from config import config

from flask import (Flask, make_response, render_template, flash, redirect,
                   request, url_for)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource, Api


api_path = "/api/v1/"
DEBUG = True


def create_app(config_name=None):

    # flask
    app = Flask(__name__)
    app.config.from_object(config)

    # flask-sqlalchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # database
    db = SQLAlchemy(app)
    db.init_app(app)

    return app

app = create_app()
db = SQLAlchemy(app)


# flask-restful
api = Api(app)

# allow cross-origin resource sharing:
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

import models, serializers

# Set routes
@app.route('/')
def index():
    return render_template(
        "index.html")

class HeartBeatView(Resource):
    def get(self, id=None):
        if not id:
            heartbeats = models.HeartBeat.query.all()
        else:
            heartbeats = [db.session.query(models.HeartBeat).get(id)]
        return serializers.HeartBeatSerializer(heartbeats, many=True).data

    def put(self):
        id = 1
        dt = datetime.utcnow()
        heartbeat = [db.session.query(models.HeartBeat).get(id)]
        if not heartbeat:
            heartbeat = models.HeartBeat(id=id, timestamp=dt)
        else:
            heartbeat = heartbeat[0]
            heartbeat.timestamp = dt
        db.session.add(heartbeat)
        db.session.commit()
        return "ok", 201

    def delete(self, id):
        try:
            heartbeat = db.session.query(models.HeartBeat).get(id)
            db.session.delete(heartbeat)
            db.session.commit()
            return "No Content", 204
        except Exception:
            return "Error Deleting " + id, 500


api.add_resource(HeartBeatView, api_path + 'heartbeat',
                 api_path + 'heartbeat/<string:id>', strict_slashes=False)


if __name__ == "__main__":
    app.run(debug=DEBUG)
