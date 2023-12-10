
label room01:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 哀愁漂うホラー的な

    if room01_is_pass == False: 
        "problem room1"
        show cat normal with dissolve

        cat normal "พร้อมสำหรับโจทย์ข้อต่อไปหรือยังล่ะ?" with dissolve
        "เรามองรูปจำนวนมากบนกระดานที่ดูไม่เกี่ยวกันเลย"
        "นี่คือโจทย์สินะ" 
        "คนที่คิดโจทย์แบบนี้ต้องเป็นคนประหลาดแค่ไหนกัน?"
        hide cat
        show puzzle1
        jump answer_roome01
        
    else :
        "this room has nothing"
        jump main_map 




label answer_roome01:
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "golderequiem" or prepare(input_value) == "goldexperiencerequiem" :
                "ถูกต้องแล้ว"
                scene white with dissolve
                $ room01_is_pass = True

                "สีขาวกลืนทิวทัศน์ตรงหน้าเราอีกครั้ง"
                "ภาพความทรงจำต่อไปจะเป็นอะไรกันนะ?"
                hide puzzle1
                jump after_room_1
            if prepare(input_value) == "golde" or prepare(input_value) == "goldexperience":
                cat "ไปปักลูกศรมาก่อน"
                jump answer_roome01
            if prepare(input_value) == "requiem":
                cat "ชื่อเต็มสิ"
                jump answer_roome01
            if prepare(input_value) == "jojo":
                cat "ภาคไหนหล่ะ"
                jump answer_roome01
            if prepare(input_value) == "stand":
                cat "ฉันชอบ Star Platinum นะ"
                jump answer_roome01
            if prepare(input_value) == "5" or prepare(input_value) == "goldenwind":
                cat "ชื่อแสตนด์สิ"
                jump answer_roome01

            cat "ผิดจ้า"
            jump answer_roome01
        "ใบ้หน่อยสิ":
            cat "โซเดียม เอเลี่ยน โพเดี้ยม อันต่อไปคืออะไรนะ คล้ายๆกับ Stanxd JXJX ซักอย่างเลย ลอง Scan QRCode ดูหน่อยดีไหมนะ"
            jump answer_roome01
        "กลับห้องรวม":
            hide puzzle1
            jump main_map

label after_room_1:
    stop music
    play music 星が輝く冬
    scene fb1 with dissolve
    mary0 "เธอรู้จักสแตxด์หรือเปล่าล่ะ?"
    yume "หา?"
    mary0 "ตอบคำถามฉันมาสิ"
    yume "ก็รู้จักแหละว่ามันมาจากอนิเมะ แต่เธอไม่ต้องถามแบบทำหน้าเข้มๆก็ได้นะ"
    mary0 "ว่ากันว่า ผู้ใช้สแตxด์จะดึงดูดผู้ใช้สแตxด์ด้วยกัน"
    yume "...เหรอ"
    mary0 "ใช่แล้ว ฉันน่ะ...เป็นผู้ใช้สแตนด์ยังไงล่ะ!!!"
    yume "............."
    mary0 "เออะ...ไม่ขำเหรอ..."
    yume "เฮ้อ ปัญญาอ่อน"
    mary0 "ใจร้าย เค้าแค่ล้อเล่นเอง"
    yume "วันหลังหัดเล่นมุกให้เก่งกว่านี้หน่อยนะ แบบนี้แค่หัวเราะเป็นมารยาทยังทำไม่ลงเลย"
    mary0 "อย่าล้อเค้า!"
    yume "ก็ได้ๆ ฮะๆๆๆ"
    "ความทรงจำปิดด้วยเสียงหัวเราะของเรา"
    "ก่อนที่ภาพตรงหน้าจะจมลงสู่ความมืด"
    scene black with dissolve
    stop music
    play music 哀愁漂うホラー的な
    scene library_s_1080 with dissolve 

    "เราตื่นขึ้นพร้อมกับหัวเราะน้อยๆ"
    "ความทรงจำที่ไร้สาระแต่ชวนให้อบอุ่นใจทำให้เราอดยิ้มออกมาไม่ได้"
    show cat normal 
    cat normal "เธอเห็นอะไรเหรอ?" 
    yume "เรื่องตลกน่ะ"
    "เราตอบเจ้าแมวส้มสั้นๆ"
    "ก่อนที่เราจะมุ่งหน้าไปยังประตูต่อไป"

    hide cat 
    jump main_map


    
