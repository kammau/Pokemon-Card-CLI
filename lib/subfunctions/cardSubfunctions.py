from db.models import Player, Card, Deck

def commit_card(session, info):
    session.add(info)
    session.commit()

def add_new_card(session, user):
    card_name_in = input("What is your new cards name?: ")
    pokemon_type_in = input("What is the card type?: ")
    hp_in = input("What is the cards hp level?: ")
    
    commit_card(session, Card(card_name=card_name_in, pokemon_type=pokemon_type_in, hp=hp_in, player_id=user[0]))

    print("Your new card has been sucessfully added!")
    get_to_main(user)

def update_card(session, user):
    card_id = input("What is the Card ID of the card you would like to update?: ")
    choice = input("What would you like to change/update on this card?: \n"
    "(n) Card Name \n"
    "(t) Card Type \n"
    "(hp) Card HP \n")

    if choice == "n":
        new_name = input("What would you like to change the cards name to?: ")
        print(session.query(Card).get(card_id).card_name)

        # commit_card(session, session.query(Card).get(user))



def remove_card(session, user):
    pass