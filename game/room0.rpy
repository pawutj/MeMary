label room0:
    "some text"
    "problem 0"
    jump answer_roome0



label answer_roome0:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "pathaway":
                "pass"
                jump main_map
            else :
                "it's not answer"
                jump answer_roome0
    
