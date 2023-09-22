
label room02:
    if room02_is_pass == False: 
        "problem room2"
        show puzzle3
        jump answer_roome02
        
    else :
        "this room has nothing"
        jump main_map 
label answer_roome02:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "oblivion":
                $ room02_is_pass = True
                "pass"
                hide puzzle3
                jump main_map
            else :
                "it's not answer"
                jump answer_roome02
        "return":
            hide puzzle3
            jump main_map
    
