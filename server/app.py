# server/app.py

from flask import Flask
from flask_migrate import Migrate
from models import db, Pet




# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

# create a new pet in the database
pet1 = Pet(name="Fido", species="Dog")
db.session.add(pet1)
db.session.commit()

# retrieve all pets from the database
pets = Pet.query.all()

Pet.query.filter(Pet.species == 'Cat').all()
Pet.query.filter_by(id=1).first()

#update and commit
pet1.name = "Fido the mighty"
db.session.commit()

# delete and commit
db.session.delete(pet1)
db.session.commit()

#delete all rows
Pet.query.delete()
db.session.commit()

#exit
exit()


if __name__ == '__main__':
    app.run(port=5555, debug=True)
