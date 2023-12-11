#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

l = ["room0" ,"room1" 
     , "room2" , "room3" , "room4" , "room5" 
     , "room6" , "room7" , "room8" , "room9"
     , "final", "common_end", "true_end"  
     ]

with open( l[0]+'.rpy' , encoding="utf-8") as f:
    content = f.read()
    lines  = content.split("\n")
    count = 0
    for s in lines:


        if(len(s) <=1):
            continue
        if("hide" in s):
            continue
        if("play" in s):
            continue
        if("show" in s):
            continue
        if("stop" in s):
            continue
        if("scene" in s):
            continue
    
        if("cat" in s):
            x = "{0:0=3d}".format(count)
            print(s + " cat_0_"+x+".mp3")
            count = count+1