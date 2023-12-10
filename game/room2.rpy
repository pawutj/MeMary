
label room02:
    $ _skipping = True
    scene library_n_1080 with dissolve
    stop music
    play music 不穏

    
    if room02_is_pass == False: 

        show cat normal with dissolve

        yume "อักษรรูน?"
        cat normal "รู้จักด้วยงั้นเหรอ ถ้างั้นก็ค่อยง่ายหน่อย"
        yume "....."
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
                cat "ลองเทียบอักษรดูสิ"
                hide puzzle3
                jump answer_roome02
            if prepare(input_value) == "obliion":
                cat "คำมันแปลกๆอยู่นะ ลองๆเติมอะไรให้มันอ่านออกมั้ย"
                hide puzzle3
                jump answer_roome02
            else :
                cat "ผิดจ้า"
                jump answer_roome02
        "ใบ้หน่อยสิ":
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
    mary0 "มันคืออักษรรูนจ้ะ"
    yume "อ่านไม่เห็นออกเลย มันมีไว้ทำอะไรรึ?"
    mary0 "มันเป็นอักษรโบราณของคนยุโรปน่ะ ฉันเห็นว่ามันเท่ดีเลยจะเอามาทำปริศนาทายเธอ"
    yume "ปริศนาอีกแล้วเหรอ?"
    mary0 "ใช่สิ ของน่าสนใจแบบนี้จะหลุดรอดได้ยังไง"
    yume "เธอสนใจ แต่ฉันไม่สนใจน่ะสิ"
    mary0 "อย่างน้อยๆก็แกล้งทำเป็นสนใจในฐานะที่เราสนิทกันเถอะน้า--"
    yume "....."
    mary0 "นะๆๆๆ"
    yume "สนใจก็ได้"
    mary0 "เย้! ในที่สุดก็มีเพื่อนไว้กวนประสา...เอ้ย ไว้เล่นด้วยแล้ว"
    yume "เมื่อกี้ฉันไม่ได้หูแว่วใช่ไหม?"
    mary0 "ไม่มี๊ไม่มี"
    yume "ยิ้มน่าสงสัยชะมัด"
    mary0 "ฮะๆๆ เดี๋ยวฉันจะสอนอ่านอักษรพวกนี้ให้นะ" 
    yume "ลองสักตั้งก็ได้ ไหนๆก็ไม่มีอะไรทำอยู่แล้ว"
    mary0 "ไม่มีอะไรทำ? แสดงว่าทำการบ้านเสร็จหมดแล้วเหรอ?"
    yume "ใช่"
    mary0 "ทำเร็วมาก สุดยอดเลยจ้า"
    yume "ขอบคุณที่ชม..."
    mary0 "ขอลอกหน่อยสิจ้ะ"
    yume "เอาความรู้สึกดีๆฉันคืนมาเลยนะ"
    
    scene library_n_1080 with dissolve
    show cat normal

    "เรากลับมาที่ห้องเดิมแล้ว"
    "เราเข้าใจอักษรพวกนี้เพราะเคยมีใครบางคนสอนเรา"
    "...เหมือนลืมบางอย่างที่สำคัญมากๆเลย..."
    cat normal "พยายามนึกให้ออกตอนนี้ยังเร็วไปนะ"
    yume "....."
    cat ah "ประตูยังมีอีกหลายบาน เธอต้องมุ่งหน้าต่อไป"
    "เจ้าแมวส้มเดินนำหน้าเราประมาณสองช่วงตัวคน เราจึงค่อยๆเดินตามมัน"
    "...สู่ประตูต่อไป..."
    hide cat
    jump cutscene_main