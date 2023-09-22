label room03:
    if room03_is_pass == False: 
        "problem room3"
        show puzzle2_1
        jump answer_roome03
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome03:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "h5+":
                "pass"
                hide puzzle2_1
                
                show puzzle2_2
                "puzzle"
                $ input_value = renpy.input("Answer?")
                if input_value == "Nf7#":
                    $ room03_is_pass = True
                    "pass"
                    hide puzzle2_2
                    jump main_map
                else:   
                    "it's not answer"
                    jump answer_roome03

            else :
                "it's not answer"
                jump answer_roome03
        "return":
            hide puzzle2_1
            jump main_map
    
