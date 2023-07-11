#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Card, Deck

if __name__ == '__main__':
    engine = create_engine('sqlite:///collection.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # add delete

    fake = Faker()

    levels = ["Beginner", "Intermediate", "Advanced"]

    players = []
    for i in range(50):
        player = Player(
            first_name=fake.unique.name(),
            last_name=fake.unique.name(),
            level=random.choice(platforms)
        )

        session.add(player)
        session.commit()

        players.append(player)