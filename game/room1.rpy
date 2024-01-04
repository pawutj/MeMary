
label room01:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 哀愁漂うホラー的な

    if room01_is_pass == False: 
        play sound "audio/sfx/indoor-footsteps-6385.mp3" volume 1
        show cat normal with dissolve
        voice "audio/voice/room1/cat_1_000.mp3"
        cat_th normal "พร้อมสำหรับโจทย์ข้อต่อไปหรือยังล่ะ?" with dissolve
        cat_en normal "Ready for the next challenge?" with dissolve
        
        th "เรามองรูปจำนวนมากบนกระดานที่ดูไม่เกี่ยวกันเลย"
        en "I gaze at the many unrelated images on the board."
        
        th "นี่คือโจทย์สินะ" 
        en "This is the challenge."
        
        th "คนที่คิดโจทย์แบบนี้ต้องเป็นคนประหลาดแค่ไหนกัน?"
        en "Whoever came up with this must be quite peculiar."
        hide cat
        show puzzle1
        jump answer_room1
        
    else :
        th "this room has nothing"
        jump main_map 




label answer_room1:
    menu:
        "Answer":
            $ input_value = renpy.input("Answer?")

            if checkThai(input_value) :
                th "ปริศนาเขาตอบภาษาอังกฤษกัน"
                en "The answer is in English"
                jump answer_room1

            if prepare(input_value) == "golderequiem" or prepare(input_value) == "goldexperiencerequiem" :
                play sound "audio/sfx/correct-6033.mp3" volume 1
                th "ถูกต้องแล้ว"
                en "That's correct."
                scene white with dissolve
                $ room01_is_pass = True

                th "สีขาวกลืนทิวทัศน์ตรงหน้าเราอีกครั้ง"
                en "The white engulfs the scenery in front of me again."

                th "ภาพความทรงจำต่อไปจะเป็นอะไรกันนะ?"
                en "What will the next memory flashback be?"
                hide puzzle1
                jump after_room_1
            if prepare(input_value) == "golde" or prepare(input_value) == "goldexperience":
    ##voice "audio/voice/room1/cat_1_001.mp3"
                cat_th "ไปปักลูกศรมาก่อน"
                cat_en "Go get the arrow first."
                jump answer_room1
            if prepare(input_value) == "requiem":
    ##voice "audio/voice/room1/cat_1_002.mp3"
                cat_th "ชื่อเต็มสิ"
                cat_en "Say the full name."
                jump answer_room1
            if prepare(input_value) == "jojo":
    ##voice "audio/voice/room1/cat_1_003.mp3"
                cat_th "ภาคไหนหล่ะ"
                cat_en "Which part is it?"
                jump answer_room1
            if prepare(input_value) == "stand":
    ##voice "audio/voice/room1/cat_1_004.mp3"
                cat_th "ฉันชอบ Star Platinum นะ"
                cat_en "I like Star Platinum."
                jump answer_room1
            if prepare(input_value) == "5" or prepare(input_value) == "goldenwind":
    ##voice "audio/voice/room1/cat_1_005.mp3"
                cat_th "ชื่อแสตนด์สิ"
                cat_en "The name of the Stand."
                jump answer_room1

    ##voice "audio/voice/room1/cat_1_006.mp3"
            cat_th "ผิดจ้า"
            cat_en "Wrong."
            jump answer_room1
        "Hint Me":
    ##voice "audio/voice/room1/cat_1_007.mp3"
            cat_th "โซเดียม เอเลี่ยน โพเดี้ยม อันต่อไปคืออะไรนะ คล้ายๆกับ Stanxd JXJX ซักอย่างเลย ลอง Scan QRCode ดูหน่อยดีไหมนะ"
            jump answer_room1

        "Hint Me More" :
            ""
            menu : 
                "Try Answer":
                    jump answer_room1
                "Skip Answer":
                    hide puzzle1
                    $ room01_is_pass = True
                    jump after_room_1
                
        "Return to Hall":
            hide puzzle1
            jump main_map


label after_room_1:
    stop music
    play music 星が輝く冬
    scene fb1 with dissolve
    voice "audio/voice/room1/mary_1_000.mp3"
    mary0_th "เธอรู้จักสแตxด์หรือเปล่าล่ะ?"
    mary0_en "Do you know about Stands?"

    yume_th "หา?"
    yume_en "Huh?"
    voice "audio/voice/room1/mary_1_001.mp3"
    mary0_th "ตอบคำถามฉันมาสิ"
    mary0_en "Just answer my question."
    
    yume_th "ก็รู้จักแหละว่ามันมาจากอนิเมะ แต่เธอไม่ต้องถามแบบทำหน้าเข้มๆก็ได้นะ"
    yume_en "I know they're from an anime, but you don't have to ask with such a stern face."

    voice "audio/voice/room1/mary_1_002.mp3"
    mary0_th "ว่ากันว่า ผู้ใช้สแตxด์จะดึงดูดผู้ใช้สแตxด์ด้วยกัน"
    mary0_en "It's said that Stand users attract other Stand users"
    
    yume_th "...เหรอ"
    yume_en "...Really?"
    
    voice "audio/voice/room1/mary_1_003.mp3"
    mary0_th "ใช่แล้ว ฉันน่ะ...เป็นผู้ใช้สแตนด์ยังไงล่ะ!!!"
    mary0_en "Yes, I am... a Stand user!!!"

    yume_th "............."
    yume_en "............."
    
    voice "audio/voice/room1/mary_1_004.mp3"
    mary0_th "เออะ...ไม่ขำเหรอ..."
    mary0_en "Uh... not funny?"

    yume_th "เฮ้อ ปัญญาอ่อน"
    yume_en "Sigh, so silly."
    
    voice "audio/voice/room1/mary_1_005.mp3"
    mary0_th "ใจร้าย เค้าแค่ล้อเล่นเอง"
    mary0_en "That's mean. I was just joking."

    yume_th "วันหลังหัดเล่นมุกให้เก่งกว่านี้หน่อยนะ แบบนี้แค่หัวเราะเป็นมารยาทยังทำไม่ลงเลย"
    yume_en "Next time, try to make a better joke. I can't even give you a courtesy laugh for that one."

    voice "audio/voice/room1/mary_1_006.mp3"
    mary0_th "อย่าล้อเค้า!"
    mary0_en "Don't tease me!"

    yume_th "ก็ได้ๆ ฮะๆๆๆ"
    yume_en "Alright, alright. Ha ha ha."

    th "ความทรงจำปิดด้วยเสียงหัวเราะของเรา"
    en "The memory ends with my laughter."

    th "ก่อนที่ภาพตรงหน้าจะจมลงสู่ความมืด"
    en "Before the scene before me plunges into darkness."
    scene black with dissolve
    stop music
    play music 哀愁漂うホラー的な
    scene library_s_1080 with dissolve 

    th "เราตื่นขึ้นพร้อมกับหัวเราะน้อยๆ"
    en "I wake up with a soft chuckle."

    th "ความทรงจำที่ไร้สาระแต่ชวนให้อบอุ่นใจทำให้เราอดยิ้มออกมาไม่ได้"
    en "This silly but heartwarming memory makes me smile involuntarily."
    
    show cat normal 
    voice "audio/voice/room1/cat_1_008.mp3"
    cat_th normal "เธอเห็นอะไรเหรอ?"    
    cat_en normal "What did you see?"

    yume_th "เรื่องตลกน่ะ"
    yume_en "A funny story."

    th "เราตอบเจ้าแมวส้มสั้นๆ"
    en "I give the orange cat a brief answer."

    th "ก่อนที่เราจะมุ่งหน้าไปยังประตูต่อไป"
    en "Before heading towards the next door."

    hide cat
    jump cutscene_main


    

