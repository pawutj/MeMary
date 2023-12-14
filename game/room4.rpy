
label room04:
    $ _skipping = True
    scene gyokuza_s_1080 with dissolve
    stop music
    play music 不穏

    if room04_is_pass == False:
        
        "เข้ามาข้างในห้องก็เจอกับกระดานดำที่เขียนโจทย์คณิตศาสตร์โชว์หรา"
        "Sin cos นี่มันอะไรกันนะ?"
        "คุ้นๆเหมือนเคยเรียนแต่ลืมไปแล้ว"
        show cat normal with dissolve
    ##voice "audio/voice/room4/cat_4_000.mp3"
        cat normal "ตรีโกณมิติจ้ะ"
        yume "แมวคิดเลขเป็นด้วยเหรอ!?"
    ##voice "audio/voice/room4/cat_4_001.mp3"
        cat ah "ง่ายขนาดแมวยังทำได้ คนทำไม่ได้ก็ไม่รู้จะว่าไงดีอ่ะ"
        
        yume "หยามกันขนาดนี้นี่จะท้าทายกันใช่ไหม?"
    ##voice "audio/voice/room4/cat_4_002.mp3"
        cat smile "จะเรียกว่าท้าทายได้ต้องดูก่อนจ้ะว่าผู้ท้าชิงฉลาดพอไหม?"
        "ทั้งๆที่เราไม่มีร่างกาย แต่ทำไมถึงรู้สึกเหมือนมีเส้นเลือดปูดขึ้นข้างหัวกันนะ?"
        "ชักอยากเอาเจ้าแมวส้มมาเช็ดกระดานแล้วสิ"
    ##voice "audio/voice/room4/cat_4_003.mp3"
        cat normal "ปริศนาข้อนี้ง่ายขนาดแมวยังทำได้ โชคดีนะจ้ะ"
        "เจ้าแมวส้มว่าแล้วก็ล้มตัวลงนอนกลิ้งกับพื้น"
        "แมวทำได้ คนก็ต้องทำได้"
        "ให้มันรู้ไปว่าคนไม่มีวันแพ้แมว!"
        hide cat
        show puzzle4
        jump answer_roome04
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome04:
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "easierthanyouthink":
    ##voice "audio/voice/room4/cat_4_004.mp3"
                cat  "ง่ายกว่าที่เธอคิดใช่ไหม?"
                $ room04_is_pass = True
                "หลังจากตอบคำถามได้ สีขาวก็ปกคลุมการมองเห็นของเรา"
                hide puzzle4
                jump after_room_4

            if prepare(input_value) == "passwordiseasierthanyouthink":
    ##voice "audio/voice/room4/cat_4_005.mp3"
                cat "ทำไมถึงอ่านตามกระดานอย่างนั้นล่ะ"
                jump answer_roome04
            
            if prepare(input_value) == "iseasierthanyouthink":
    ##voice "audio/voice/room4/cat_4_006.mp3"
                cat "แปลกๆอยู่นะ มันน่าจะเป็นคณิตศาสตร์รึเปล่า"
                jump answer_roome04
            if prepare(input_value) == "0":
    ##voice "audio/voice/room4/cat_4_007.mp3"
                cat "ไม่ใช่ว่าเจออะไรก็ตอบ 0 ก่อนสิ"
                jump answer_roome04
            if prepare(input_value) == "1":
    ##voice "audio/voice/room4/cat_4_008.mp3"
                cat "ฉันว่าเธอน่าจะบวกเลขผิดนะ"
                jump answer_roome04
            if prepare(input_value) == "2":
    ##voice "audio/voice/room4/cat_4_009.mp3"
                cat "เธอไปหาคำตอบมาจริงๆหรอเนี่ย แต่เสียใจด้วยจ้ะ"
                jump answer_roome04
            else :
    ##voice "audio/voice/room4/cat_4_010.mp3"
                cat "ผิดจ้า"
                jump answer_roome04
        "ใบ้หน่อยสิ":
    ##voice "audio/voice/room4/cat_4_011.mp3"
            cat "X^3 + Y^3 = (X+Y) * (X^2 - XY + Y^2)  
            \nเห็นไหมล่ะ? Easier Than You Think"
            jump answer_roome04
        "return":
            hide puzzle4
            jump main_map
    
label after_room_4:
    scene fb2_1 with dissolve
    stop music
    play music 星が輝く冬

    yume "เธอรู้ว่าฉันสอบเลขไม่ผ่าน ใจคอยังจะให้ตอบปริศนาเลขอีกเหรอ?"
    ##voice "audio/voice/room4/mary_4_000.mp3"
    mary0 "ตรีโกณมิติที่แมวก็ยังทำได้จ้ะ เธอเป็นคนอย่าเพิ่งยอมแพ้สิจ้ะ"
    yume "โจทย์มันเขียนมามึนๆงี้จะให้ทำยังไง?"
    ##voice "audio/voice/room4/mary_4_001.mp3"
    mary0 "....."
    yume "แล้วข้างล่างที่เขียนว่า ‘ง่ายกว่าที่คิด’ นี่มันอะไรกัน?"
    ##voice "audio/voice/room4/mary_4_002.mp3"
    mary0 "....."
    yume "อย่าเงียบเป็นเป่าสากสิ ใบ้ฉันหน่อย!" 
    ##voice "audio/voice/room4/mary_4_003.mp3"
    mary0 "Password is easier than you think จ้ะ"
    yume "What?"
    ##voice "audio/voice/room4/mary_4_004.mp3"
    mary0 "Password is easier than you think จ้ะ"
    yume "ฉันไม่ได้บอกให้เธออ่านซ้ำ ฉันบอกให้เธอใบ้ฉัน"
    ##voice "audio/voice/room4/mary_4_005.mp3"
    mary0 "คำใบ้บางคำเท่ากับการเฉลยแล้วจ้ะ"
    yume "หา?"
    ##voice "audio/voice/room4/mary_4_006.mp3"
    mary0 "คิดดูดีๆสิจ้ะ ถ้าฉันรู้ว่าเธอไม่เก่งเลข ฉันจะใจร้ายขนาดเอาปริศนาเลขมาให้เธอทำไหม?"
    yume "คิด"
    ##voice "audio/voice/room4/mary_4_007.mp3"
    mary0 "....."
    yume "เธอดูเหมือนพวกที่จะหัวเราะเยาะเพื่อนทุกครั้งที่ตัวเองฉลาดกว่าน่ะ"
    ##voice "audio/voice/room4/mary_4_008.mp3"
    mary0 "ใจร้าย!"
    yume "ทีนี้ช่วยใบ้ฉันให้ชัดกว่านี้ที ฉันขอล่ะ"
    ##voice "audio/voice/room4/mary_4_009.mp3"
    mary0 "ไม่มีชัดกว่านี้แล้วจ้ะ"
    yume "จริงรึ?"
    ##voice "audio/voice/room4/mary_4_010.mp3"
    mary0 "จริงอ่ะดิ"
    yume "........."
    "เราพูดไม่ออก สุดท้ายเราก็ได้แต่นั่งจิ้มกระดาษทายปริศนาของคนตรงหน้า"
    "น่าเจ็บใจจริงๆ"

    scene gyokuza_s_1080 with dissolve
    yume "เฮ้อ..."
    "ปริศนาเลขบ้าอะไรกัน? ตรีโกณมิติบ้าอะไรกัน?"
    "นี่มันโจทย์กวนประสาทชัดๆ!"
    show cat normal
    ##voice "audio/voice/room4/cat_4_012.mp3"
    cat normal "ในที่สุดก็ไขปริศนาได้ แต่ก็ยังตอบช้ากว่าแมวนะจ้ะ"
    "ถ้าเรายังมีใบหน้าอยู่ เราคงเบิกตาโพลงใส่แมวส้มไปแล้ว"
    yume "คำตอบมันบอกกันโต้งๆเลยนี่ แล้วจะมีโจทย์ข้างบนทำไม?"
    ##voice "audio/voice/room4/cat_4_013.mp3"
    cat normal "เพื่อขายขำจ้ะ"
    yume "......" 
    ##voice "audio/voice/room4/cat_4_014.mp3"
    cat normal "ทำไมเธอเข้าใกล้ฉันขนาดนั้นล่ะจ้ะ?"
    yume "จะยกแกไปเช็ดกระดาน หมั่นไส้"
    ##voice "audio/voice/room4/cat_4_015.mp3"
    cat normal "ใจร้ายกับแมวชะมัด!"
    "เจ้าแมวส้มรีบวิ่งหนีจากเรา เราจึงวิ่งตามมัน"
    "...สู่ประตูต่อไป..."

    hide cat
    jump cutscene_main
