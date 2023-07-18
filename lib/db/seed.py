#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Card, Deck

if __name__ == '__main__':
    engine = create_engine('sqlite:///cards.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    # Delete records:
    session.query(Player).delete()
    session.query(Card).delete()
    session.query(Deck).delete()

    levels = ["Beginner", "Intermediate", "Advanced"]
    pokemon_types = ["Fire", "Steel", "Flying", "Grass", "Electric", "Dragon"]

    players = []
    for i in range(50):
        player = Player(
            username=fake.user_name(),
            level=random.choice(levels)
        )

        session.add(player)
        session.commit()

        players.append(player)

    cards = []
    for i in range(50):
        card = Card(
            card_name=fake.unique.name(), #maybe add specific list for name?
            pokemon_type=random.choice(pokemon_types),
            hp=fake.unique.random_int(min=1, max=120),
            player_id=fake.random_int(min=1, max=50)
        )

        session.add(card)
        session.commit()

        cards.append(card)

    decks = []
    for i in range(50):
        deck = Deck(
            deck_name=fake.unique.name(),
            player_id=fake.random_int(min=1, max=50)
        )

        session.add(deck)
        session.commit()

        decks.append(deck)
    
    session.close()