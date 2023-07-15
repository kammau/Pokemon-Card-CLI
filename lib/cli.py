#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Player, Card, Deck

def add_data(info):
    session.add(info)
    session.commit()

class PokemonCli:
    def __init__(self):
        self.player = [player for player in session.query(Player)]
        self.card = [card for card in session.query(Card)]
        self.deck = [deck for deck in session.query(Deck)]
        self.login()

    def login(self):
        user = input("Please enter your username: ") #decide between username and name!
        usernames = [name.username for name in self.player]
        if user in usernames:
            print(f"Welcome back {user}!")
            self.main_menu()
        else:
            sign_up = input("Looks like your new here, do you want to sign up? (y/n) ")
            if sign_up == "y":
                self.sign_up()
            elif sign_up == "n":
                print("Ok, have a good day!")
        # for player in self.player:
        #     if user == player.username:
        #         print(f"Welcome back {user}!")
        #         self.main_menu()
        #     else:
        #         sign_up = input("Looks like your new here, do you want to sign up? (y/n) ")
        #         if sign_up == "y":
        #             self.sign_up()
        #         elif sign_up == "n":
        #             print("Ok, have a good day!")

    
    def sign_up(self):
        username = input("Please enter a username: ")
        level = input("Please specify a playing level (Beginner, Intermediate, Advanced): ")
        add_data(Player(level=level, username=username))

    def main_menu(self):
        print("What you wanna do?")

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/cards.db") # home base for the database
    session = Session(engine, future=True)
    PokemonCli()

