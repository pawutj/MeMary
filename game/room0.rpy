label intro:
    scene 
    "Just Intro"
    jump room0

label room0:
    "some text"
    "problem 0"
    show puzzle0
    jump answer_roome0



label answer_roome0:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "pathaway":
                "pass"
                hide puzzle0
                jump main_map
            else :
                "it's not answer"
                jump answer_roome0
    
