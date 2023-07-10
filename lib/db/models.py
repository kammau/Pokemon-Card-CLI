from sqlalchemy import ForeignKey, Column, Integer, String, Metadata #
from sqlalchemy.orm import relationship, backref #
from sqlalchemy.ext.declarative import declarative_base #

# metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Player(Base):
    

