from sqlalchemy import ForeignKey, Column, Integer, String, Metadata #
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
    name = Column(String)
    # add more

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    set_name = Column(String())
    hp = Column(Integer())

    def __repr__(self):
        return f'Card(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'set_name={self.set_name}, ' + \
            f'hp={self.hp})'
        

