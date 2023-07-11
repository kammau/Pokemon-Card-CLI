#!/usr/bin/env python3

from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Card, Deck

if __name__ == '__main__':
    engine = create_engine('sqlite:///collection.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # add delete

    fake = Faker()

    players = []
    for i in range(50):
        player = Player(
            name=fake.unique.name()
        )

        session.add(player)
        session.commit()

        players.append(player)