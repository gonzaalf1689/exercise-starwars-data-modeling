import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hairColor = Column(String(250), nullable=True)
    eyeColor = Column(String(250), nullable=True)
    skinColor = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    birthYear = Column(String(250), nullable=True)
    homeworld = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)

class UserFavoritesCharacters(Base):
    __tablename__='user_favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    diameter = Column(Integer, nullable=True)
    rotationPeriod = Column(Integer, nullable=True)
    orbitalPeriod = Column(Integer, nullable=True)
    gravity = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surfaceWater = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)

class UserFavoritePlanets(Base):
    __tablename__='user_favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

#class Address(Base):
#    __tablename__ ='address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
