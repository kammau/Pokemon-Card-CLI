from db.models import Deck, Player
from sqlalchemy import delete

def add_new_deck(session, user, menu):
    username = session.query(Player).get(user)

    deck_name_in = input("What is the name of the new deck you would like to add?: ")
    deck_set_in = input("What is the set this deck belongs to?: ")

    session.add(Deck(deck_name=deck_name_in, set_name=deck_set_in, player_id=user[0]))
    session.commit()

    print("\nYour new deck has been added to your collection!")
    menu(username.username)

def remove_deck(session, user, menu):
    username = session.query(Player).get(user)

    deck_id = input("What is the Deck ID of the deck you would like to remove?: ")
    deck_to_del = session.query(Deck).get(deck_id)

    session.delete(deck_to_del)
    session.commit()

    print(f"Deck {deck_id} has been sucessfully removed from your collection.")
    menu(username.username)

def update_deck(session, user, menu):
    username = session.query(Player).get(user)

    deck_id = input("What is the Deck ID of the deck you would like to update?: ")
    deck_info = session.query(Deck).get(deck_id)

    options = input(f"What would you like to update on Deck {deck_id}?: \n"
    "(n) Update Deck Name\n"
    "(s) Update Deck Set\n")

    if options == "n":
        new_name = input("What would like to rename this deck?: ")
        deck_info.deck_name = new_name
        session.commit()

        print(f"Your deck has now been renamed to {new_name}!")

    elif options == "s":
        new_setn = input("What would you like to change this decks set to?: ")
        deck_info.set_name = new_setn
        session.commit()

        print(f"Your decks set has been changed to {new_setn}!")
    
    else:
        print("Please type in a valid character...")
        update_deck(session, user)
        
    menu(username.username)
