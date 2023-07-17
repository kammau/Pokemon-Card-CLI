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
            self.main_menu(user)
        else:
            sign_up = input("Looks like your new here, do you want to sign up? (y/n) ")
            if sign_up == "y":
                self.sign_up()
            elif sign_up == "n":
                print("Ok, have a good day!")

    
    def sign_up(self):
        username = input("Please enter a username: ")
        level = input("Please specify a playing level (Beginner, Intermediate, Advanced): ")
        add_data(Player(level=level, username=username))

    def main_menu(self, user): #***COME BACK TO ADD UPDATE (crUd)***
        print(f"Welcome back {user}! Please select an option:")
        options = input('1) Look through collection \n'
            '2) Add new item to collection \n'
            '3) Remove an item from your collection \n')
        
        if options == "1":
            self.read_collection(user)
        elif options == "2":
            self.add_to_collection(user)
        elif options == "3":
            self.delete_from_collection(user)
        else:
            print("Please type a number!")
        
    def read_collection(self, user):
        user_id = [player.id for player in session.query(Player) if player.username == user]
        cards = [card.card_name for card in session.query(Card) if card.player_id in user_id]
        options = input("Would you like to search through your Cards (c) or Decks (d)?: ")
        if options == "c":
            print(cards)
            

    
    def add_to_collection(self, user):
        pass
    
    def delete_from_collection(self, user):
        pass

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/cards.db") # home base for the database
    session = Session(engine, future=True)
    PokemonCli()

