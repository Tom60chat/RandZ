from http import HTTPStatus
import random
from flask import Flask, render_template

from zombie import Zombie

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello world", HTTPStatus.OK

@app.route('/zombie')
def zombie():
    title = 'Zombie'
    
    zombies = { Zombie(300, 310) }
    
    return render_template('zombie.jinja', title=title, zombies=zombies)

@app.route('/zombies/<nombre>')
def zombies(nombre):
    title = 'Zombies'
    
    zombies = { Zombie(random.randint(300, 1200), random.randint(310, 1100)) for i in range(int(nombre)) }
    
    return render_template('zombie.jinja', title=title, zombies=zombies)

