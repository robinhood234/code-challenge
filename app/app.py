#!/usr/bin/env python3
from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
import os
# from flask_restful import Api, Resource

from models import db, Hero, Power, HeroPower

file_path = os.path.abspath(os.getcwd()) + '/db/app.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)

db.init_app(app)
# api = API(app)
@app.route('/heroes', methods = ['GET'])
def get_heroes():

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = next((hero for hero in heroes if hero["id"] == hero_id), None)
    if hero is None:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero)

if __name__ == '__main__':
    app.run(port=5555)