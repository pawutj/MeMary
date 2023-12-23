#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

l = ["room0" ,"room1" 
     , "room2" , "room3" , "room4" , "room5" 
     , "room6" , "room7" , "room8" , "room9"
     , "final", "common_end", "true_end" , "cutscene"   
     ]

for i in range(len(l)):
    with open( l[i]+'.rpy' , encoding="utf-8") as f:
        f2 = open(  "./extract/"+"cat_"+l[i]+".txt", "x" , encoding="utf-8")
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
            if("if" in s):
                continue
            if("else" in s ):
                continue
            if("jump" in s):
                continue
            if("$" in s):
                continue
            if("\"" not in s):
                continue
        
            if("cat" in s):
                x = "{0:0=3d}".format(count)
                #print(s + " mary_" + str(i) + "_" + str(x) +".mp3")
                f2.write(s + " cat_" + str(i) + "_" + str(x) +".mp3"+"\n")
                count = count+1
            else:
                f2.write(s +"\n")
        