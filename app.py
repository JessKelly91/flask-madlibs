from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask (__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def ask_story():
    """Show list of stories to choose from."""
    return render_template("select-story.html", stories = stories.values())

@app.route('/form')
def generate_story_form():
    """Generate form to ask for words"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("form.html", story_id = story_id, title = story.title, prompts=prompts)

@app.route('/story')
def create_story():
    """Creates story based on submited story form and show result"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)
