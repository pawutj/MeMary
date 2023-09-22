
label room05:
    if room05_is_pass == False: 
        "problem room5"
        show puzzle5
        jump answer_roome05
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome05:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "spring_is_in_the_air":
                $ room05_is_pass = True
                "pass"
                hide puzzle5
                jump main_map
            else :
                "it's not answer"
                jump answer_roome05
        "return":
            hide puzzle5
            jump main_map
    