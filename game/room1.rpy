
label room01:
    if room01_is_pass == False: 
        "problem room1"
        show puzzle1
        jump answer_roome01
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome01:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "golderequiem":
                $ room01_is_pass = True
                "pass"
                hide puzzle1
                jump main_map
            else :
                "it's not answer"
                jump answer_roome01
        "return":
            hide puzzle1
            jump main_map
    
