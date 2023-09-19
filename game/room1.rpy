
label room1:
    "problem room1"
    jump answer_roome1
    return

label answer_roome1:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "pathaway":
                "pass"
                jump main_map
            else :
                "it's not answer"
                jump answer_roome1
        "return":
            jump main_map
    
