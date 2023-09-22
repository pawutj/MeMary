
label room06:
    if room06_is_pass == False: 
        "problem room6"
        show puzzle6
        jump answer_roome06
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome06:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "spider_lily":
                $ room06_is_pass = True
                "pass"
                hide puzzle6
                jump main_map
            else :
                "it's not answer"
                jump answer_roome06
        "return":
            hide puzzle6
            jump main_map
    