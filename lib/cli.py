#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Player, Card, Deck

from subfunctions.cardSubfunctions import (add_new_card, update_card, remove_card)

def add_data(info):
    session.add(info)
    session.commit()

class PokemonCli:
    def __init__(self):
        # self.player = [player for player in session.query(Player)]
        # self.card = [card for card in session.query(Card)]
        # self.deck = [deck for deck in session.query(Deck)]
        self.login()

    def login(self):
        user = input("Please enter your username: ")
        usernames = [name.username for name in session.query(Player)]
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
        options = input('1) Look through card collection \n'
            '2) Look through Deck collection \n'
            '3) Quit program \n')
        
        if options == "1":
            self.card_collection(user)
        elif options == "2":
            self.deck_collection(user)
        elif options == "3":
            print(f"Have a good day {user}!")
        else:
            print("Please type a number!")
        
    def card_collection(self, user):
        user_id = [player.id for player in session.query(Player) if player.username == user]
        cards = [card for card in session.query(Card) if card.player_id in user_id]
        print(f"Here are all the cards in you collection {user}: \n")
        for card in cards:
            print(f"Card ID: {card.id} \n"
            f"Card Name: {card.card_name} \n"
            f"HP: {card.hp} \n"
            f"Set: {card.set_name} \n")
        options = input("What would you like to do next?: \n"
            "(u) Update a card \n"
            "(r) Remove a card \n"
            "(a) Add a card \n"
            "(m) Go to main menu \n")
        
        if options == "a":
            # add_new_card()
            print(user)
            

    
    def deck_collection(self, user):
        user_id = [player.id for player in session.query(Player) if player.username == user]
        decks = [deck for deck in session.query(Deck) if deck.player_id in user_id]
        print(f"Here are all the decks in your collection {user}: \n")
        for deck in decks:
            print(f"Deck ID: {deck.id} \n"
            f"Deck Name: {deck.deck_name} \n")
    
    def edit_profile(self, user):
        pass

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/cards.db") # home base for the database
    session = Session(engine, future=True)
    PokemonCli()

