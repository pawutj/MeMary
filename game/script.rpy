# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# label config_value:
#     $ room01_is_pass = False



label start:
    $ room01_is_pass = False
    $ room02_is_pass = False
    $ room03_is_pass = False
    $ room04_is_pass = False
    $ room05_is_pass = False
    $ room06_is_pass = False
    $ room07_is_pass = False
    $ room08_is_pass = False
    $ room09_is_pass = False
    $ room10_is_pass = False
    $ room11_is_pass = False


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Start"

    jump room0

    # These display lines of dialogue.


    ""
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

 
    # This ends the game.

    return

label main_map:
    
    window hide
    show screen map_screen
    
    $ renpy.pause(hard=True)
    