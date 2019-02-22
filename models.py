"""Models file, starting with Pet."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text, 
                        nullable=True)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer,
                    nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

