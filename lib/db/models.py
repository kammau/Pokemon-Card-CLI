from sqlalchemy import ForeignKey, Column, Integer, String, MetaData #
from sqlalchemy.orm import relationship, backref #
from sqlalchemy.ext.declarative import declarative_base #

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    level = Column(String())

    cards = relationship("Card", backref=backref('player'))
    decks = relationship("Deck", backref=backref('player'))

    def __repr__(self):
        return f'Player(id={self.id}, ' + \
            f'name={self.username}'

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer(), primary_key=True)
    card_name = Column(String())
    pokemon_type = Column(String())
    hp = Column(Integer())
    player_id = Column(Integer(), ForeignKey("players.id"))

    def __repr__(self):
        return f'Card(id={self.id}, ' + \
            f'card_name={self.card_name}, ' + \
            f'pokemon_type={self.pokemon_type}, ' + \
            f'hp={self.hp})'
        
class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer(), primary_key=True)
    deck_name = Column(String())
    set_name=Column(String())
    player_id = Column(Integer(), ForeignKey("players.id"))

    def __repr__(self):
        return f'Deck(id={self.id}, ' + \
            f'name={self.deck_name}'

