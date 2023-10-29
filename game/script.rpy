# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define yume = Character("เรา",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define cat0 = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define cat = Character("แมว", image ="cat" ,color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
# label config_value:
#     $ room01_is_pass = False

define mary0 = Character("???",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define mary = Character("แมรี่",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
define father = Character("พ่อของแมรี่",color="#F0F8FF", who_outlines=[(2,"#000000")], what_outlines=[(2,"#000000")])
image moonlight3 = im.Scale("bg/moonlight3.png",1920,1080)

style default:
    line_spacing 10
init python:
    def prepare(s):
        return s.lower().replace(" ", "").replace("_","")
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

    jump intro

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
    