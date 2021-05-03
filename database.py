"""
Attribution:

    1. Player rotation was adapted from this video tutorial by Web Dev Junkie: https: // www.youtube.com/watch?v = _WJSH7NxtRc. Made adjustments to it so that the player's gun pointed to the mouse.

    2. Code to move a canvas element from its current position to a target position was borrowed from a html5gamedevs forum post reply written by a user called "Exca".
    Available from: https: // www.html5gamedevs.com/topic/36416-bullet-go-on-mouse-position/
    This was used for getting bullets to move towards where the player and enemies are aiming and for the enemy "chase" behaviour.
    The code for actually creating enemies and bullets and managing them was all written by me.
    I also wrote code to ensure the bullets originated from the barrell of the player's gun. The extent of these modifications are discussed in comments below.

    3. Borrowed code from an article written by Pranchal Katiyar to find out if a user was running the game on a Window's machine. Available from: https: // www.geeksforgeeks.org/detect-the-operating-system-of-user-using-javascript/
    4. Media query code for seeing if a user's screen was below a given width was borrowed from W3Schools. Available from: https: // www.w3schools.com/howto/howto_js_media_queries.asp

    Both 3 and 4 were adapted to be used in conjuction with each other to detect if the user was on a machine that might experience a mouse position bug.
    If the user was running Windows and the screen was also below a certain width then the javascript offsets their recorded mouse position to account for the bug.

    5. Player and enemy art was made by Riley Gombart and is licensed under Creative Commons Attribution 3.0.
    Art available from: https: // opengameart.org/content/animated-top-down-survivor-player
    License available from: https: // creativecommons.org/licenses/by/3.0/

    6. The enemy art was made greyscale using the Grayscale Image Online tool. Available from: https: // pinetools.com/grayscale-image

    7. Background music is "Ascent to the Station" by TeknoAXE and is a royalty free piece of music. Available from: http: // teknoaxe.com/Home.php

    8. All sound effects were generated by me using the online tool jsfxr. Availbale from: https: // sfxr.me/

    9. Font used is Ubuntu by Dalton Maag. Available from: https: // fonts.google.com/specimen/Ubuntu

    10. All other HTML, CSS, Javascript, Python and art was written/made by me. I made the tileset in an online tool called Piskel. Available from: https: // www.piskelapp.com/

"""

"""
Things to note:

    1. The game is very difficult to play with a track pad so I'd recommend using a mouse.

    2. Having the tab zoomed in or out messes up the mouse positioning. Please ensure that your zoom settings are set to their default(i.e. 100 % or 1.0) to avoid issues.

    3. There are issues with running the game in Chrome on laptop's running Windows, the details of which are in comments below.
    I implemented a fix but the game runs much better on laptop's running Linux and on Windows Desktops.
    I'd recommend playing it on such a machine for the optimum experience.

    4. The controls are W to go up, S to go down, A to go left, and D to go right. (Or alternatively UP, DOWN LEFT, RIGHT arrow keys)
"""

from flask import g
import os
import sqlite3
DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE,
                               detect_types=sqlite3.PARSE_DECLTYPES
                               )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
