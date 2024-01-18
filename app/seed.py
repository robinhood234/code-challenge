from app import app
from models import db, Hero, Power, HeroPower
from random import randint, choice
from faker import Faker

fake = Faker()


def seed_powers():
    print("🦸‍♀️ Seeding powers...")
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]
    powers = [Power(**power) for power in powers_data]
    db.session.add_all(powers)
    db.session.commit()

def seed_heroes():
    print("🦸‍♀️ Seeding heroes...")
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]
    heroes = [Hero(**hero) for hero in heroes_data]
    db.session.add_all(heroes)
    db.session.commit()

def add_powers_to_heroes():
    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()
    powers = Power.query.all()

    for hero in heroes:
        for _ in range(randint(1, 3)):
            selected_power = choice(powers)
            strength = choice(strengths)

            hero_power = HeroPower(hero=hero, power=selected_power, strength=strength)
            db.session.add(hero_power)

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_powers()
        seed_heroes()
        add_powers_to_heroes()