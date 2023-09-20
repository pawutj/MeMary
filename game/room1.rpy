
label room1:
    "problem room1"
    show puzzle1
    jump answer_roome1
    return

label answer_roome1:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "golderequiem":
                "pass"
                hide puzzle1
                jump main_map
            else :
                "it's not answer"
                jump answer_roome1
        "return":
            hide puzzle1
            jump main_map
    
