
label room01:

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

        show puzzle1
        jump answer_roome01
        
    else :
        "this room has nothing"
        jump main_map 




label answer_roome01:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "golderequiem":
                $ room01_is_pass = True
                "สีขาวกลืนทิวทัศน์ตรงหน้าเราอีกครั้ง"
                "ภาพความทรงจำต่อไปจะเป็นอะไรกันนะ?"
                hide puzzle1
                jump after_room_1
            else :
                "it's not answer"
                jump answer_roome01
        "return":
            hide puzzle1
            jump main_map

label after_room_1:
    stop music
    play music 星が輝く冬
    scene flashback
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


    
