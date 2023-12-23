l = ["room0" ,"room1" 
     , "room2" , "room3" , "room4" , "room5" 
     , "room6" , "room7" , "room8" , "room9"
     , "final", "common_end", "true_end" , "cutscene"   
     ]

for i in range(len(l)):
    with open( l[i]+'.rpy' , encoding="utf-8") as f:
        f2 = open(  "./extract/"+ l[i] + ".rpy", "x" , encoding="utf-8")
        content = f.read()
        lines  = content.split("\n")
        countcat = 0
        countmary =0 
        for s in lines:

            if(len(s) <=1):
                print(s)
                f2.write(s+"\n")
                continue
            if("hide" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("play" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("show" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("stop" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("scene" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("if" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("else" in s ):
                f2.write(s+"\n")
                print(s)
                continue
            if("jump" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("$" in s):
                f2.write(s+"\n")
                print(s)
                continue
            if("\"" not in s):
                f2.write(s+"\n")
                print(s)
                continue
        
            if("cat"in s):
                x = "{0:0=3d}".format(countcat)
                #print(s + " mary_" + str(i) + "_" + str(x) +".mp3")
                print("    ##cat_"+str(i) + "_" + str(x) +".mp3")
                f2.write('    ##voice "audio/voice/'+l[i] +'/cat_'+str(i) + '_' + str(x) +'.mp3"'+'\n')
                f2.write(s+"\n")
                countcat = countcat+1
            elif("mary" in s):
                x = "{0:0=3d}".format(countmary)
                #print(s + " mary_" + str(i) + "_" + str(x) +".mp3")
                print("    ##mary_"+str(i) + "_" + str(x) +".mp3")
                print(s)
                f2.write('    ##voice "audio/voice/'+ l[i]+'/mary_'+str(i) + '_' + str(x) +'.mp3"'+'\n')
                f2.write(s+"\n")
                countmary = countmary+1

            else:
                f2.write(s+"\n")
                print(s)
        