from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
from petapi import get_random_pet
from forms import EditPetForm, AddPetForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "abc123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

# creating and validating a FlaskForm class to load the add pet HTML form


@app.route('/')
def show_homepage():
    '''homepage'''
    pets = Pet.query.all()
    random_pet = get_random_pet()
    return render_template('home.html', pets=pets, random_pet=random_pet)


@app.route('/add', methods=['GET', 'POST'])    
def add_pet_form():
    '''render and process add pet form'''
    form = AddPetForm()
    
    # validating if its GET or POST
    if form.validate_on_submit():
        
        pet = Pet(  name = form.name.data,
                    species = form.species.data,
                    photo_url = form.photo_url.data or None,
                    age = form.age.data or None,
                    notes = form.notes.data or None,
                    available = form.available.data)
        db.session.add(pet)
        db.session.commit()    
        return redirect('/')   

    else:
        return render_template("addpet.html", form=form)


@app.route('/<int:pet_id_number>', methods=['GET', 'POST'])
def edit_pet_form(pet_id_number):
    '''render and process edit pet information; display pet info'''
    
    pet = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        
        pet.photo_url = form.photo_url.data or None
        pet.notes = form.notes.data or None
        pet.available = form.available.data
        
        db.session.commit()    
        return redirect('/')   

    else:
        return render_template("display_edit_pet.html", form=form, pet=pet)
