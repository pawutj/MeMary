
label room02:
    $ _skipping = True
    scene library_n_1080 with dissolve
    stop music
    play music 不穏

    
    if room02_is_pass == False: 

        show cat normal with dissolve
        "น่าแปลก"
        "ทั้งๆที่เราไม่ควรจะมีความทรงจำเหลืออยู่ แต่ทำไมเราถึงรู้จักอักษรพวกนี้ได้"
        "...เป็นไปได้หรือเปล่าว่าตัวตนของเราค่อยๆกลับมาระหว่างการไขปริศนา..."
        "ถ้าเป็นอย่างนั้น เราก็คงต้องตอบคำถามข้อนี้ให้ได้"
        hide cat

        
        jump answer_roome02
        
    else :
        "this room has nothing"
        jump main_map 
label answer_roome02:
    show puzzle3 with dissolve
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "oblivion":
                $ room02_is_pass = True
                "สีขาวกลืนกินทุกอย่างอีกครั้ง ภาพความทรงจำอันลางเรือนปรากฏขึ้น"
                hide puzzle3
                jump after_room_2

            if prepare(input_value) == "rune":
    ##voice "audio/voice/room2/cat_2_000.mp3"
                cat "ลองเทียบอักษรดูสิ"
                hide puzzle3
                jump answer_roome02
            if prepare(input_value) == "obliion":
    ##voice "audio/voice/room2/cat_2_001.mp3"
                cat "คำมันแปลกๆอยู่นะ ลองๆเติมอะไรให้มันอ่านออกมั้ย"
                hide puzzle3
                jump answer_roome02
            else :
    ##voice "audio/voice/room2/cat_2_002.mp3"
                cat "ผิดจ้า"
                jump answer_roome02
        "ใบ้หน่อยสิ":
    ##voice "audio/voice/room2/cat_2_003.mp3"
            cat "ดูถ้าจะคล้ายๆกับ อักษรรูน นะ ดูเหมือนจะเทียบอักษรเป็นภาษาอังกฤษได้อยู่นะ"
            jump answer_roome02
        "กลับห้องรวม":
            hide puzzle3
            jump main_map
    

label after_room_2:
    stop music
    play music up_to_you
    scene fb1 with dissolve
    yume "อักษรหน้าตาประหลาดพวกนี้คืออะไร?"
    ##voice "audio/voice/room2/mary_2_000.mp3"
    mary0 "มันคืออักษรรูนจ้ะ"
    yume "อ่านไม่เห็นออกเลย มันมีไว้ทำอะไรรึ?"
    ##voice "audio/voice/room2/mary_2_001.mp3"
    mary0 "มันเป็นอักษรโบราณของคนยุโรปน่ะ ฉันเห็นว่ามันเท่ดีเลยจะเอามาทำปริศนาทายเธอ"
    yume "ปริศนาอีกแล้วเหรอ?"
    ##voice "audio/voice/room2/mary_2_002.mp3"
    mary0 "ใช่สิ ของน่าสนใจแบบนี้จะหลุดรอดได้ยังไง"
    yume "เธอสนใจ แต่ฉันไม่สนใจน่ะสิ"
    ##voice "audio/voice/room2/mary_2_003.mp3"
    mary0 "อย่างน้อยๆก็แกล้งทำเป็นสนใจในฐานะที่เราสนิทกันเถอะน้า--"
    yume "....."
    ##voice "audio/voice/room2/mary_2_004.mp3"
    mary0 "นะๆๆๆ"
    yume "สนใจก็ได้"
    ##voice "audio/voice/room2/mary_2_005.mp3"
    mary0 "เย้! ในที่สุดก็มีเพื่อนไว้กวนประสา...เอ้ย ไว้เล่นด้วยแล้ว"
    yume "เมื่อกี้ฉันไม่ได้หูแว่วใช่ไหม?"
    ##voice "audio/voice/room2/mary_2_006.mp3"
    mary0 "ไม่มี๊ ไม่มี"
    yume "ยิ้มน่าสงสัยชะมัด"
    ##voice "audio/voice/room2/mary_2_007.mp3"
    mary0 "ฮะๆๆ เดี๋ยวฉันจะสอนอ่านอักษรพวกนี้ให้นะ" 
    yume "ลองสักตั้งก็ได้ ไหนๆก็ไม่มีอะไรทำอยู่แล้ว"
    ##voice "audio/voice/room2/mary_2_008.mp3"
    mary0 "ไม่มีอะไรทำ? แสดงว่าทำการบ้านเสร็จหมดแล้วเหรอ?"
    yume "ใช่"
    ##voice "audio/voice/room2/mary_2_009.mp3"
    mary0 "ทำเร็วมาก สุดยอดเลยจ้า"
    yume "ขอบคุณที่ชม..."
    ##voice "audio/voice/room2/mary_2_010.mp3"
    mary0 "ขอลอกหน่อยสิจ้ะ"
    yume "เอาความรู้สึกดีๆฉันคืนมาเลยนะ"
    
    scene library_n_1080 with dissolve
    show cat normal

    "เรากลับมาที่ห้องเดิมแล้ว"
    "เราเข้าใจอักษรพวกนี้เพราะเคยมีใครบางคนสอนเรา"
    "...เหมือนลืมบางอย่างที่สำคัญมากๆเลย..."
    ##voice "audio/voice/room2/cat_2_004.mp3"
    cat normal "พยายามนึกให้ออกตอนนี้ยังเร็วไปนะ"
    yume "....."
    ##voice "audio/voice/room2/cat_2_005.mp3"
    cat ah "ประตูยังมีอีกหลายบาน เธอต้องมุ่งหน้าต่อไป"
    "เจ้าแมวส้มเดินนำหน้าเราประมาณสองช่วงตัวคน เราจึงค่อยๆเดินตามมัน"
    "...สู่ประตูต่อไป..."
    hide cat
    jump cutscene_main
