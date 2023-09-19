



screen map_screen:
    add "map/map.png"  # Replace with the path to your map image.
    
    imagebutton auto "map/room1_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("room1")]

    imagebutton auto "map/room2_%s.png":
        focus_mask True
        action [Hide("map_screen"),Jump("room2")]
        