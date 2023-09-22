
label room07:
    if room07_is_pass == False: 
        "problem room7"
        show puzzle7
        jump answer_roome07
    
    else :
        "this room has nothing"
        jump main_map 

label answer_roome07:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "orion":
                $ room07_is_pass = True
                "pass"
                hide puzzle7
                jump main_map
            else :
                "it's not answer"
                jump answer_roome07
        "return":
            hide puzzle7
            jump main_map
    