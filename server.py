"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
ADJECTIVES = ['green', 'large', 'smelly', 'moist', 'squishy']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
    Click <a href= "/hello"> here</a> to go hello!


    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <div id="complement">
          <form action="/greet">
            Fill out this form for a complement:
            <br>What's your name? <input type="text" name="person">
            <select name="compliment">
              <option value="kind">Kind</option>
              <option value="smart">Smart</option>
              <option value="spunky">Spunky</option>
            </select>
            <input type="submit" value="Submit">
          </form>
        </div>

        <div id="diss">
         <form action="/diss">
          Fill out this form for a diss:
          <br>What's your name? <input type="text" name="person">
          <select name="diss">
            <option value="ugly">Ugly</option>
            <option value="mean">Mean</option>
            <option value=" lint licker"> Lint Licker</option>
          </select>
        </div>
          <br>
          <div id="color">
            What is your favorite color? <br>
            <input type="radio" name="fav_color" value="green">Green<br>
            <input type="radio" name="fav_color" value="pink"> Pink <br>
            <input type="radio" name="fav_color" value="blue"> Blue <br>
            <input type="radio" name="fav_color" value="red"> Red <br>
            <input type="radio" name="fav_color" value="purple"> Purple <br>
          </div>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment_choice = request.args.get("compliment")

    #compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment_choice)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    diss_choice = request.args.get("diss")
    adjective = choice(ADJECTIVES)
    color = request.args.get("fav_color")

    #compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're a {adjective} {diss}! But I know that {color}
        is your favorite color!! >:)
      </body>
    </html>
    """.format(player=player, adjective=adjective, diss=diss_choice, color=color)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
