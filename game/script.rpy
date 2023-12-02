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
image sky_cloudy = im.Scale("bg/sky_cloudy.png",1920,1080)
image classroom_sunset = im.Scale("bg/classroom_evening02.jpg",1920,1080)
image classroom_morning = im.Scale("bg/classroom_morning.png",1920,1080)
image sky_morning = im.Scale("bg/sky_morning.png",1920,1080)
image nightsky = im.Scale("bg/nightsky.png",1920,1080)

image puzzle0 :
    "puzzle/puzzle0.png"
    zoom 0.6
    yalign 0.4



image puzzle3 :
    "puzzle/puzzle3.png"
    zoom 0.6
    yalign 0.4

image puzzle4 :
    "puzzle/puzzle4.png"
    zoom 0.6
    yalign 0.4

image puzzle5 :
    "puzzle/puzzle5.png"
    zoom 0.6
    yalign 0.4


image puzzle6 :
    "puzzle/puzzle6.png"
    zoom 0.6
    yalign 0.4


image puzzle7 :
    "puzzle/puzzle7.png"
    zoom 0.6
    yalign 0.4


image puzzle8 :
    "puzzle/puzzle8.png"
    zoom 0.6
    yalign 0.4

image puzzle2_1:
    "puzzle/puzzle2_1_new.png"
    zoom 0.3
    yalign 0.4

image puzzle2_2:
    "puzzle/puzzle2_2_new.png"
    zoom 0.3
    yalign 0.4

image puzzle2_3:
    "puzzle/puzzle2_3_new.png"
    zoom 0.3
    yalign 0.4






image hospital =im.Scale("bg/hospital.png",1920,1080)
image road = im.Scale("bg/road.jpg",1920,1080)

image kitchen03 = im.Scale("bg/kitchen03.png",1920,1080)

image fb1 = im.Scale("cg/fb1.png",1920,1080)
image fb2_1 = im.Scale("cg/fb2_1.png",1920,1080)
image fb2_2 = im.Scale("cg/fb2_2.png",1920,1080)
image fb2_3 = im.Scale("cg/fb2_3.png",1920,1080)

image fb3_1 = im.Scale("cg/fb3_1.png",1920,1080)
image fb3_2 = im.Scale("cg/fb3_2.png",1920,1080)
image fb3_3 = im.Scale("cg/fb3_3.png",1920,1080)
image fb3_4 = im.Scale("cg/fb3_4.png",1920,1080)
image fb3_5 = im.Scale("cg/fb3_5.png",1920,1080)
image fb3_6 = im.Scale("cg/fb3_6.png",1920,1080)
image cg3 = im.Scale("cg/cg3.png",1920,1080)


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
    $ renpy.config.skipping = False
    $ _skipping = False
    window hide
    show screen map_screen with dissolve
    
    $ renpy.pause(hard=True)
    
    