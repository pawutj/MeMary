



screen map_screen:
    add "map/map.png"  # Replace with the path to your map image.

    

    imagebutton auto "map/room01_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("room01")]

    imagebutton auto "map/room02_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("room02")]

    imagebutton auto "map/room03_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("room03")]
    
    if room01_is_pass  or room02_is_pass or room03_is_pass :
        imagebutton auto "map/room04_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("room04")]
    else :
        imagebutton:
            idle "map/room04_disable.png"

    if room01_is_pass or room02_is_pass or room03_is_pass :        
        imagebutton auto "map/room05_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("room05")]
    else :
        imagebutton:
            idle "map/room05_disable.png"


                
    if room01_is_pass or room02_is_pass or  room03_is_pass :    
        imagebutton auto "map/room06_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("room06")]
    else : 
        imagebutton : 
            idle "map/room06_disable.png"

    if room04_is_pass and room05_is_pass and room06_is_pass:    
        imagebutton auto "map/room07_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("room07")]
    else :
        imagebutton : 
            idle "map/room07_disable.png"

    if room04_is_pass and room05_is_pass and room06_is_pass: 
        imagebutton auto "map/room08_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("room08")]
    else:
        imagebutton : 
            idle "map/room08_disable.png"

    
    if room07_is_pass and room08_is_pass: 
        imagebutton auto "map/room09_%s.png":
            focus_mask True
            action [Hide("map_screen"),Jump("room09")]
    else:
        imagebutton : 
            idle "map/room09_disable.png"

        

        

        
        
        