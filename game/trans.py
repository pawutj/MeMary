en = []
th = []
with open( "./trans/0_eng.txt" , encoding="utf-8") as f:
    content = f.read()
    lines  = content.split("\n")

    for s in lines:
        _s =s
        if(s.strip() == ""):
            continue
        if( ":" in s):
            _s = s.split(":")[1].strip()
        print(_s)
        en += [_s]

with open( "./trans/0_th.txt" , encoding="utf-8") as f:
    content = f.read()
    lines  = content.split("\n")

    for s in lines:
        _s =s
        if(s.strip() == ""):
            continue
        if( ":" in s):
            _s = s.split(":")[1].strip()
        print(_s)
        th += [_s]
    print(len(th))
