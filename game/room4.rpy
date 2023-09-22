
label room04:
    if room04_is_pass == False: 
        "problem room4"
        show puzzle4
        jump answer_roome04
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome04:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "easier than you think":
                $ room04_is_pass = True
                "pass"
                hide puzzle4
                jump main_map
            else :
                "it's not answer"
                jump answer_roome04
        "return":
            hide puzzle4
            jump main_map
    
