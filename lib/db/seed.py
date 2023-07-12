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
    fake = Faker()

    # Delete records:
    session.query(Player).delete()
    session.query(Card).delete()
    session.query(Deck).delete()

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

    cards = []
    for i in range(50):
        card = Card(
            name=fake.unique.name(), #maybe add specific list for name?
            set_name=fake.unique.name(),
            hp=fake.unique.random_int(min=1, max=120)
        )

        session.add(card)
        session.commit()

        cards.append(card)

    decks = []
    for i in range(50):
        deck = Deck(
            
        )