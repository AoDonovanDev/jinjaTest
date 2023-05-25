from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "!1IcedCoffee"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/newstory')
def new_story():
    story_text = story.generate(request.args)
    return render_template('story.html', this_story = story_text)

@app.route('/form')
def form():
    return render_template('form.html')