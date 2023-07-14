#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Player, Card, Deck

class PokemonCli:
    def __init__(self):
        self.player = [player for player in session.query(Player)]
        self.card = [card for card in session.query(Card)]
        self.deck = [deck for deck in session.query(Deck)]
        self.login()

    def login(self):
        user = input("Please Enter Your Username: ")
        if user in self.player:
            print(f"Welcome Back {user}")
            self.main_menu()
        else:
            sign_up = input("Looks like your new here, do you want to sign up? (Y/N)")

    def main_menu(self):
        pass

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/cards.db") # home base for the database
    session = Session(engine, future=True)
    PokemonCli()
