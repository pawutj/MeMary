
label room08:
    if room08_is_pass == False: 
        "problem room8"
        show puzzle8
        jump answer_roome08
    
    else :
        "this room has nothing"
        jump main_map 

label answer_roome08:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "ruSsElL":
                $ room08_is_pass = True
                "pass"
                hide puzzle8
                jump main_map
            else :
                "it's not answer"
                jump answer_roome08
        "return":
            hide puzzle8
            jump main_map
    