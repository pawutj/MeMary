
label room2:
    "problem room2"
    show puzzle3
    "puzzle"
    jump answer_roome2
    return

label answer_roome2:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "oblivion":
                "pass"
                hide puzzle3
                jump main_map
            else :
                "it's not answer"
                jump answer_roome1
        "return":
            hide puzzle3
            jump main_map
    
