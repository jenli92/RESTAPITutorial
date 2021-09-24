#https://code.visualstudio.com/docs/python/tutorial-flask#_refactor-the-project-to-support-further-development
#set up flask. *second Flask is case senstive
from flask import Flask
app = Flask(__name__)

from flask import jsonify
from flask import request

#connect to database
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


#object relational mapper
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

#make a simple route (endpoint), and give it a path
@app.route('/')
def index():
    return 'Hello!'

#GET all the drinks
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks": output}

#GET a specific drink
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    #need to import jsonify from flask
    return jsonify({"name": drink.name, "description": drink.description})

#POST(Add) a drink
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

#DELETE a drink
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "Drink not found."}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Drink deleted successfully!"}

