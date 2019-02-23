from flask_wtf import FlaskForm
from flask_wtf.html5 import URLField
from wtforms import StringField, FloatField, IntegerField, BooleanField, RadioField
from wtforms.validators import InputRequired, Optional, url, NumberRange


class AddPetForm(FlaskForm):
    """" Form for Adding pets to the pets data table"""
    name = StringField("Pet's name: ",
                       validators=[InputRequired()])
    species = RadioField("What species of Pet? ",
                         validators=[InputRequired()],
                         choices=[('cat', 'Cat'),
                                  ('dog', 'Dog'),
                                  ('porcupine', 'Porcupine')])
    photo_url = URLField("Photo URL: ",
                         validators=[url(), Optional(strip_whitespace=True)])
    age = IntegerField("How old is the pet? ",
                       validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes: ")
    available = BooleanField("Is this pet available for adoption? ")
 

class EditPetForm(FlaskForm):
    '''Form for editing pet data from pets table'''
    photo_url = URLField("Photo URL: ",
                         validators=[url(), Optional(strip_whitespace=True)])
    notes = StringField("Notes: ")
    available = BooleanField("Is this pet available for adoption? ")