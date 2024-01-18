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
@app.route('/heroes', methods=['GET'])
def get_heroes():
    db = get_db()
    heroes = db.execute('SELECT * FROM heroes').fetchall()
    heroes = [dict(hero) for hero in heroes]
    return jsonify(heroes)

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    db = get_db()
    hero = db.execute('SELECT * FROM heroes WHERE id = ?', (hero_id,)).fetchone()
    if hero is None:
        return jsonify({"error": "Hero not found"}), 404
    hero = dict(hero)
    powers = db.execute('SELECT * FROM powers WHERE hero_id = ?', (hero_id,)).fetchall()
    powers = [dict(power) for power in powers]
    hero['powers'] = powers
    return jsonify(hero)

@app.route('/powers', methods=['GET'])
def get_powers():
    db = get_db()
    powers = db.execute('SELECT * FROM powers').fetchall()
    powers = [dict(power) for power in powers]
    return jsonify(powers)

@app.route('/powers/<int:power_id>', methods=['GET', 'PATCH'])
def get_or_update_power(power_id):
    db = get_db()
    power = db.execute('SELECT * FROM powers WHERE id = ?', (power_id,)).fetchone()
    if power is None:
        return jsonify({"error": "Power not found"}), 404
    power = dict(power)
    if request.method == 'PATCH':
        data = request.get_json()
        if 'description' not in data:
            return jsonify({"error": "Invalid request"}), 400
        db.execute('UPDATE powers SET description = ? WHERE id = ?', (data['description'], power_id))
        db.commit()
        power['description'] = data['description']
    return jsonify(power)

if __name__ == '__main__':
    app.run(port=5555)