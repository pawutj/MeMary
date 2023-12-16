
label room01:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 哀愁漂うホラー的な

    if room01_is_pass == False: 
        show cat normal with dissolve
    ##voice "audio/voice/room1/cat_1_000.mp3"
        cat_th normal "พร้อมสำหรับโจทย์ข้อต่อไปหรือยังล่ะ?" with dissolve
        th "เรามองรูปจำนวนมากบนกระดานที่ดูไม่เกี่ยวกันเลย"
        th "นี่คือโจทย์สินะ" 
        th "คนที่คิดโจทย์แบบนี้ต้องเป็นคนประหลาดแค่ไหนกัน?"
        hide cat
        show puzzle1
        jump answer_roome01
        
    else :
        th "this room has nothing"
        jump main_map 




label answer_roome01:
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "golderequiem" or prepare(input_value) == "goldexperiencerequiem" :
                th "ถูกต้องแล้ว"
                scene white with dissolve
                $ room01_is_pass = True

                th "สีขาวกลืนทิวทัศน์ตรงหน้าเราอีกครั้ง"
                th "ภาพความทรงจำต่อไปจะเป็นอะไรกันนะ?"
                hide puzzle1
                jump after_room_1
            if prepare(input_value) == "golde" or prepare(input_value) == "goldexperience":
    ##voice "audio/voice/room1/cat_1_001.mp3"
                cat_th "ไปปักลูกศรมาก่อน"
                jump answer_roome01
            if prepare(input_value) == "requiem":
    ##voice "audio/voice/room1/cat_1_002.mp3"
                cat_th "ชื่อเต็มสิ"
                jump answer_roome01
            if prepare(input_value) == "jojo":
    ##voice "audio/voice/room1/cat_1_003.mp3"
                cat_th "ภาคไหนหล่ะ"
                jump answer_roome01
            if prepare(input_value) == "stand":
    ##voice "audio/voice/room1/cat_1_004.mp3"
                cat_th "ฉันชอบ Star Platinum นะ"
                jump answer_roome01
            if prepare(input_value) == "5" or prepare(input_value) == "goldenwind":
    ##voice "audio/voice/room1/cat_1_005.mp3"
                cat_th "ชื่อแสตนด์สิ"
                jump answer_roome01

    ##voice "audio/voice/room1/cat_1_006.mp3"
            cat_th "ผิดจ้า"
            jump answer_roome01
        "ใบ้หน่อยสิ":
    ##voice "audio/voice/room1/cat_1_007.mp3"
            cat_th "โซเดียม เอเลี่ยน โพเดี้ยม อันต่อไปคืออะไรนะ คล้ายๆกับ Stanxd JXJX ซักอย่างเลย ลอง Scan QRCode ดูหน่อยดีไหมนะ"
            jump answer_roome01
        "กลับห้องรวม":
            hide puzzle1
            jump main_map

label after_room_1:
    stop music
    play music 星が輝く冬
    scene fb1 with dissolve
    ##voice "audio/voice/room1/mary_1_000.mp3"
    mary0_th "เธอรู้จักสแตxด์หรือเปล่าล่ะ?"
    yume_th "หา?"
    ##voice "audio/voice/room1/mary_1_001.mp3"
    mary0_th "ตอบคำถามฉันมาสิ"
    yume_th "ก็รู้จักแหละว่ามันมาจากอนิเมะ แต่เธอไม่ต้องถามแบบทำหน้าเข้มๆก็ได้นะ"
    ##voice "audio/voice/room1/mary_1_002.mp3"
    mary0_th "ว่ากันว่า ผู้ใช้สแตxด์จะดึงดูดผู้ใช้สแตxด์ด้วยกัน"
    yume_th "...เหรอ"
    ##voice "audio/voice/room1/mary_1_003.mp3"
    mary0_th "ใช่แล้ว ฉันน่ะ...เป็นผู้ใช้สแตนด์ยังไงล่ะ!!!"
    yume_th "............."
    ##voice "audio/voice/room1/mary_1_004.mp3"
    mary0_th "เออะ...ไม่ขำเหรอ..."
    yume_th "เฮ้อ ปัญญาอ่อน"
    ##voice "audio/voice/room1/mary_1_005.mp3"
    mary0_th "ใจร้าย เค้าแค่ล้อเล่นเอง"
    yume_th "วันหลังหัดเล่นมุกให้เก่งกว่านี้หน่อยนะ แบบนี้แค่หัวเราะเป็นมารยาทยังทำไม่ลงเลย"
    ##voice "audio/voice/room1/mary_1_006.mp3"
    mary0_th "อย่าล้อเค้า!"
    yume_th "ก็ได้ๆ ฮะๆๆๆ"
    th "ความทรงจำปิดด้วยเสียงหัวเราะของเรา"
    th "ก่อนที่ภาพตรงหน้าจะจมลงสู่ความมืด"
    scene black with dissolve
    stop music
    play music 哀愁漂うホラー的な
    scene library_s_1080 with dissolve 

    th "เราตื่นขึ้นพร้อมกับหัวเราะน้อยๆ"
    th "ความทรงจำที่ไร้สาระแต่ชวนให้อบอุ่นใจทำให้เราอดยิ้มออกมาไม่ได้"
    show cat normal 
    ##voice "audio/voice/room1/cat_1_008.mp3"
    cat_th normal "เธอเห็นอะไรเหรอ?" 
    yume_th "เรื่องตลกน่ะ"
    th "เราตอบเจ้าแมวส้มสั้นๆ"
    th "ก่อนที่เราจะมุ่งหน้าไปยังประตูต่อไป"

    hide cat
    jump cutscene_main


    

