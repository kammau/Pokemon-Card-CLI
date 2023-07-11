#!/usr/bin/env python3

from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Card, Deck

if __name__ == '__main__':
    
