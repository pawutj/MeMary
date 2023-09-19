# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
label label1:
    "some text"
    jump start
    return

label label2:
    "some text"
    jump start
    return

screen map_screen:
    add "map/map.png"  # Replace with the path to your map image.
    
    imagebutton auto "map/room1_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("label1")]

    imagebutton auto "map/room2_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("label2")]
        




label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show eileen happy

    


    "Start"

    # These display lines of dialogue.
    window hide
    show screen map_screen
    $ renpy.pause(hard=True)

    ""
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

 
    # This ends the game.

    return
