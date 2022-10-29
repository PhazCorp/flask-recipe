import json
from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['DEBUG'] = True

# Connect to mariadb database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_recipe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Difine Recipe model table
@dataclass
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
    server_default=func.now())

    def __repr__(self):
        return f'<Recipe> {self.title}'

# Routes
@app.route('/api/recipes')
def index():
    recipes = Recipe.query.all()

    return jsonify(recipes)

app.run()
