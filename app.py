from flask import Flask, render_template, redirect
# , flash
from flask_wtf import FlaskForm
from flask_debugtoolbar import DebugToolbarExtension
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional
from models import Pet, connect_db, db

app = Flask(__name__)

app.config["SECRET_KEY"] = "abc123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

# creating and validating a FlaskForm class to load the add pet HTML form
class AddPetForm(FlaskForm):
    """" Form for Adding pets to the pets data table"""
    name = StringField("Pet's name: ",
                       validators=[InputRequired()])
    species = StringField("What species of Pet? ",
                          validators=[InputRequired()])
    photo_url = StringField("Photo URL: ")
    age = IntegerField("How old is the pet? ",
                       validators=[InputRequired()])
    notes = StringField("Notes: ")
    available = BooleanField("Is this pet available for adoption? ")
    # ,
                            #  validators=[InputRequired()])


@app.route('/')
def show_homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods=['GET', 'POST'])    
def add_pet_form():
    # creating the form instance
    form = AddPetForm()
    
    # validating if its GET or POST
    if form.validate_on_submit():
        
        pet = Pet(  name = form.name.data,
                    species = form.species.data,
                    photo_url = form.photo_url.data or None,
                    age = form.age.data,
                    notes = form.notes.data or None,
                    available = form.available.data)
        db.session.add(pet)
        db.session.commit()    
        return redirect('/')   

    else:
        return render_template("addpet.html", form = form)    

