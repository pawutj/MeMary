label room03:
    $ _skipping = True
    scene room_s_1080 with dissolve
    stop music
    play music 哀愁漂うホラー的な


    if room03_is_pass == False: 
        show cat normal with dissolve
        yume_th "หมากรุก?"
        th "สิ่งที่ปรากฏต่อหน้าเราคือกระดานสีขาวดำที่แสนคุ้นเคย"
        th "เป็นไปได้ไหมนะที่เราเคยเล่นมันบ่อยๆ"
    
    ##voice "audio/voice/room3/cat_3_000.mp3"
        cat_th normal "ฉันจะลองดูว่าเธอแก้มันได้เร็วแค่ไหน"
        th "เจ้าแมวส้มท้าทายเราพร้อมกับส่งเสียงหัวเราะเล็กๆ"
        th "ไม่รู้ว่าทำไม แต่รู้สึกว่าต้องไขปริศนาให้ได้"
        th "ไม่งั้นคงไม่สบายใจแน่ๆ"
        hide cat

        show puzzle2_1
        jump answer_roome03
        
    else :
        th "this room has nothing"
        jump main_map 

label answer_roome03:
    menu:
        "ตอบคำถาม":
            th "ถ้าอยากเดิน Rook ไป A2 ให้ตอบว่า Ra2 นะ \nถ้า King ให้บอก K \nถ้า Pawn คือไม่ต้องระบุอะไรนะ ระบุช่องที่จะเดินได้เลย"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "ra6":
    ##voice "audio/voice/room3/cat_3_001.mp3"
                cat_th "เชิงหนาใช้ได้นะเนี่ย"
                show puzzle2_2 with dissolve
                hide puzzle2_1
                ".."
                show puzzle2_3 with dissolve
                hide puzzle2_2
    ##voice "audio/voice/room3/cat_3_002.mp3"
                cat_th "เดินยังไงต่อดีล่ะ"
                $ input_value = renpy.input("Answer?")
                if prepare(input_value) == "rxa7#":
                    yume "Check Mate"
                    $ room03_is_pass = True
                    th "สีขาวกลืนกินทุกอย่าง ภาพในอดีตปรากฏขึ้นต่อหน้า"
                    hide puzzle2_3
                    jump after_room_3
                if prepare(input_value) == "ra7":
    ##voice "audio/voice/room3/cat_3_003.mp3"
                    cat_th "ลืมบอกว่า Check Mate รึเปล่า? Rxa7#"
                    hide puzzle2_3
                    show puzzle2_1 with dissolve
                    jump answer_roome03
    ##voice "audio/voice/room3/cat_3_004.mp3"
                cat_th "เกือบจะชนะแล้วแท้ๆ ลองใหม่ดีไหม?"
                hide puzzle2_3
                show puzzle2_1 with dissolve
                jump answer_roome03
            if prepare(input_value) == "ra2":
    ##voice "audio/voice/room3/cat_3_005.mp3"
                cat_th "เค้าแค่ยกตัวอย่าง"
                jump answer_roome03

            if prepare(input_value) == "ra7":
    ##voice "audio/voice/room3/cat_3_006.mp3"
                cat_th "ลืมบอกว่ารุกรึเปล่า Rxa7+"
                jump answer_roome03
            if prepare(input_value) == "rxa7":
    ##voice "audio/voice/room3/cat_3_007.mp3"
                cat_th "ลืมบอกว่ารุกรึเปล่า Rxa7+"
                jump answer_roome03
            if prepare(input_value) == "rxa7+":
    ##voice "audio/voice/room3/cat_3_008.mp3"
                cat_th "หมากนี้เล่นต่อน่าจะแพ้นะ"
                jump answer_roome03
            if prepare(input_value) == "b7":
    ##voice "audio/voice/room3/cat_3_009.mp3"
                cat_th "ลืมบอกว่ารุกรึเปล่า xB7"
                jump answer_roome03
            if prepare(input_value) == "bx7":
    ##voice "audio/voice/room3/cat_3_010.mp3"
                cat_th "แบบนี้เกมส์น่าจะเสมอนะ"
                jump answer_roome03
            
    ##voice "audio/voice/room3/cat_3_011.mp3"
            cat_th "ไม่ได้คล้ายเลยเธอ"
            jump answer_roome03
        "ใบ้หน่อยสิ":
    ##voice "audio/voice/room3/cat_3_012.mp3"
            cat_th "คุ้นๆ Paul Morphy's problem บ้างไหม"
            jump answer_roome03
        "กลับห้องโถง":
            hide puzzle2_1
            jump main_map
    


label after_room_3:
    stop music
    play music 星が輝く冬
    scene fb1 with dissolve
    
    yume_th "ฉันมองเห็นแล้ว"
    ##voice "audio/voice/room3/mary_3_000.mp3"
    mary0_th "เห็นอะไรเหรอจ้ะ?"
    yume_th  "เส้นทางสู่ชัยชนะของฉัน"
    ##voice "audio/voice/room3/mary_3_001.mp3"
    mary0_th  "รุกฆาตจ้ะ"
    yume_th  "เฮ้ย!"
    ##voice "audio/voice/room3/mary_3_002.mp3"
    mary0_th  "มัวแต่ดูหมากตัวเอง แล้วไม่ดูหมากศัตรูก็แบบนี้แหละจ้ะ"
    yume_th  "ไม่จริงน่า แพ้อีกแล้ว!"
    ##voice "audio/voice/room3/mary_3_003.mp3"
    mary0_th  "แข่งกัน 30 ครั้ง เธอชนะฉัน 3 ครั้ง แค่นี้ก็สุดยอดมากแล้วนะ"
    yume_th  "3 ครั้งที่ชนะนั่น เธอดันเล่นไปหมากรุกไปดูหนังไปอีกต่างหาก โอย..."
    ##voice "audio/voice/room3/mary_3_004.mp3"
    mary0_th  "อย่าคิดมากสิจ้ะ ฉันก็แค่เก่งกว่าเธอมากๆๆๆเท่านั้นเอง"
    yume_th  "ไม่ต้องย้ำคำว่า ‘มาก’ หลายๆครั้งก็ได้น่า"
    ##voice "audio/voice/room3/mary_3_005.mp3"
    mary0_th  "ฉันรอวันที่เธอจะชนะฉันอีกนะจ้ะ"
    yume_th  "ฉันจะลองดู"
    ##voice "audio/voice/room3/mary_3_006.mp3"
    mary0_th  "สงสัยคงต้องเลือกหนังสักเรื่องล่วงหน้าก่อน อืม...เอาเรื่องนี้ดีไหมนะ?"
    yume_th  "เธอกะออมมือเต็มที่เลยนี่หว่า!"
    ##voice "audio/voice/room3/mary_3_007.mp3"
    mary0_th  "ถ้าเธอแพ้จนหมดใจ ฉันจะเล่นกับใครล่ะจ้ะ?"
    yume_th  "วันหลังฉันไปพาแมวที่บ้านมาเล่นแทนฉัน"
    ##voice "audio/voice/room3/mary_3_008.mp3"
    mary0_th  "เล่นหมากรุกกับแมวนี่เล่นกับตัวเองยังสนุกกว่าเลยจ้ะ"
    yume_th  "เธอเล่นกับตัวเองมันจะได้อะไร?"
    ##voice "audio/voice/room3/mary_3_009.mp3"
    mary0_th  "ถ้าเราเก่งจนอยู่ในจุดที่ชนะได้ทุกคน ก็มีแค่ตัวฉันเองเท่านั้นล่ะจ้ะที่ชนะตัวเองได้"
    yume_th  "ประโยคเพ้อฝันอย่างกับหลุดมาจากการ์ตูนต่อสู้"
    ##voice "audio/voice/room3/mary_3_010.mp3"
    mary0_th  "เธอแพ้คนเพ้อฝันบ่อยๆจะนับเป็นตัวอะไรกันล่ะจ้ะ?"
    yume_th  "ด่ากันขนาดนี้ ลากไปตบกลางสี่แยกยังใจดีกว่านะ"
    ##voice "audio/voice/room3/mary_3_011.mp3"
    mary0_th  "ไม่ได้ว่าจ้ะ แค่พูดตามความจริง"
    yume_th  "ยอมไม่ได้แล้ว มาแข่งกันอีกรอบสิ!"
    ##voice "audio/voice/room3/mary_3_012.mp3"
    mary0_th  "ขอเลือกหนังก่อนเล่นตาต่อไปสักนาทีหนึ่งนะ"
    yume_th  "อย่าออมมือกับฉันสิ!"
    "เสียงโวยวายของเราสิ้นสุดลง ภาพก็กลับมามืดดำ"

    scene room_s_1080 with dissolve
    play music 哀愁漂うホラー的な
    th "เราเริ่มจำได้แล้ว"
    th "เรามีใครสักคนหนึ่งที่สำคัญกับเรามากๆ เธอคนนั้นเล่นหมากรุกกับเราประจำ"
    yume_th "....."
    th "ทั้งๆที่สำคัญขนาดนั้น แต่ทำไมเราถึงนึกหน้าของคนคนนั้นไม่ออกนะ"
    th "ทำไมกัน?"
    show cat normal
    ##voice "audio/voice/room3/cat_3_013.mp3"
    cat_th normal "ยินดีด้วยที่ชนะเป็นครั้งที่สี่แล้วนะ"
    yume_th "หา?"

    ##voice "audio/voice/room3/cat_3_014.mp3"
    cat_th normal "ไม่มีอะไรหรอก ไปห้องต่อไปกันเถอะ"
    th "เจ้าแมวส้มยิ้มให้เราบางๆก่อนจะเดินนำหน้าเรา เราเดินตามมันเพราะไม่มีทางเลือกอื่นใด"
    th "หนทางที่จะรู้ความจริง มีแต่แก้ปริศนาเท่านั้น"
    th "สู่ประตูบานต่อไป..."

    hide cat
    jump cutscene_main
