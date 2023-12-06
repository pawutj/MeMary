
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
        cat normal "ตรีโกณมิติจ้ะ"
        yume "แมวคิดเลขเป็นด้วยเหรอ!?"
        cat ah "ง่ายขนาดแมวยังทำได้ คนทำไม่ได้ก็ไม่รู้จะว่าไงดีอ่ะ"
        
        yume "หยามกันขนาดนี้นี่จะท้าทายกันใช่ไหม?"
        cat smile "จะเรียกว่าท้าทายได้ต้องดูก่อนจ้ะว่าผู้ท้าชิงฉลาดพอไหม?"
        "ทั้งๆที่เราไม่มีร่างกาย แต่ทำไมถึงรู้สึกเหมือนมีเส้นเลือดปูดขึ้นข้างหัวกันนะ?"
        "ชักอยากเอาเจ้าแมวส้มมาเช็ดกระดานแล้วสิ"
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
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "easierthanyouthink":
                $ room04_is_pass = True
                "หลังจากตอบคำถามได้ สีขาวก็ปกคลุมการมองเห็นของเรา"
                hide puzzle4
                jump after_room_4
            else :
                "it's not answer"
                jump answer_roome04
        "ใบ้หน่อยสิ":
            "โจทย์ก็บอกว่าอยู่ว่า Easier Than You Think"
            jump answer_roome04
        "return":
            hide puzzle4
            jump main_map
    
label after_room_4:
    scene fb2_1 with dissolve
    stop music
    play music 星が輝く冬

    yume "เธอรู้ว่าฉันสอบเลขไม่ผ่าน ใจคอยังจะให้ตอบปริศนาเลขอีกเหรอ?"
    mary0 "ตรีโกณมิติที่แมวก็ยังทำได้จ้ะ เธอเป็นคนอย่าเพิ่งยอมแพ้สิจ้ะ"
    yume "โจทย์มันเขียนมามึนๆงี้จะให้ทำยังไง?"
    mary0 "....."
    yume "แล้วข้างล่างที่เขียนว่า ‘ง่ายกว่าที่คิด’ นี่มันอะไรกัน?"
    mary0 "....."
    yume "อย่าเงียบเป็นเป่าสากสิ ใบ้ฉันหน่อย!" 
    mary0 "Password is easier than you think จ้ะ"
    yume "What?"
    mary0 "Password is easier than you think จ้ะ"
    yume "ฉันไม่ได้บอกให้เธออ่านซ้ำ ฉันบอกให้เธอใบ้ฉัน"
    mary0 "คำใบ้บางคำเท่ากับการเฉลยแล้วจ้ะ"
    yume "หา?"
    mary0 "คิดดูดีๆสิจ้ะ ถ้าฉันรู้ว่าเธอไม่เก่งเลข ฉันจะใจร้ายขนาดเอาปริศนาเลขมาให้เธอทำไหม?"
    yume "คิด"
    mary0 "....."
    yume "เธอดูเหมือนพวกที่จะหัวเราะเยาะเพื่อนทุกครั้งที่ตัวเองฉลาดกว่าน่ะ"
    mary0 "ใจร้าย!"
    yume "ทีนี้ช่วยใบ้ฉันให้ชัดกว่านี้ที ฉันขอล่ะ"
    mary0 "ไม่มีชัดกว่านี้แล้วจ้ะ"
    yume "จริงรึ?"
    mary0 "จริงอ่ะดิ"
    yume "........."
    "เราพูดไม่ออก สุดท้ายเราก็ได้แต่นั่งจิ้มกระดาษทายปริศนาของคนตรงหน้า"
    "น่าเจ็บใจจริงๆ"

    scene gyokuza_s_1080 with dissolve
    yume "เฮ้อ..."
    "ปริศนาเลขบ้าอะไรกัน? ตรีโกณมิติบ้าอะไรกัน?"
    "นี่มันโจทย์กวนประสาทชัดๆ!"
    show cat normal
    cat normal "ในที่สุดก็ไขปริศนาได้ แต่ก็ยังตอบช้ากว่าแมวนะจ้ะ"
    "ถ้าเรายังมีใบหน้าอยู่ เราคงเบิกตาโพลงใส่แมวส้มไปแล้ว"
    yume "คำตอบมันบอกกันโต้งๆเลยนี่ แล้วจะมีโจทย์ข้างบนทำไม?"
    cat normal "เพื่อขายขำจ้ะ"
    yume "......" 
    cat normal "ทำไมเธอเข้าใกล้ฉันขนาดนั้นล่ะจ้ะ?"
    yume "จะยกแกไปเช็ดกระดาน หมั่นไส้"
    cat normal "ใจร้ายกับแมวชะมัด!"
    "เจ้าแมวส้มรีบวิ่งหนีจากเรา เราจึงวิ่งตามมัน"
    "...สู่ประตูต่อไป..."

    hide cat
    jump main_map