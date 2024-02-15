from flask import Flask, request, render_template
from stories import *
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def choose_story():
    """Choose between different prompts for madlibs."""
    
    return render_template("choose_story.html", stories=stories.values())

@app.route('/questions')
def questions():
    """Input answers for the madlibs story."""

    # Retrieve the story from the dictionary based on code of chosen story
    story_code = request.args["story_code"]
    story = stories[story_code]

    return render_template("questions.html", story_code=story_code, questions=story.words, title=story.title)

@app.route('/story')
def print_madlibs():
    """Display the story created based on the user's answers."""

    # Retrieve the story from the dictionary based on code of chosen story
    story_code = request.args["story_code"]
    story = stories[story_code]

    # Fill in the blanks of the story with built-in "generate" method of Story
    completed_madlibs = story.generate(request.args)
    return render_template("madlibs_story.html", template=completed_madlibs)