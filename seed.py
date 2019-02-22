"""Seed file to make sample data for pets db."""

from models import Pet
from app import app, db, connect_db

# Create all tables
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add users
alan = Pet(name='Alan', species='dog', photo_url='/static/alan.jpg', age=12, notes="", available=True)  
joel = Pet(name='Joel', species='dog', photo_url='/static/joel.jpg', age=2, notes="Here is some notes", available=False)  
jane = Pet(name='Jane', species='dog', photo_url='/static/jane.jpg', age=1, notes="", available=True)  
sara = Pet(name='Sara', species='dog', photo_url='/static/Sara.jpg', age=5, notes="No notes", available=False)  
ethan = Pet(name='Ethan', species='dog', photo_url='/static/dog.jpg', age=10, notes="argh notes", available=True)  

# Add new objects to session, so they'll persist
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)
db.session.add(sara)
db.session.add(ethan)

db.session.commit()