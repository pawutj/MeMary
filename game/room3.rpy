label room03:
    $ _skipping = True
    scene room_s_1080 with dissolve
    stop music
    play music 哀愁漂うホラー的な


    if room03_is_pass == False: 
        show cat normal with dissolve
        yume "หมากรุก?"
        "สิ่งที่ปรากฏต่อหน้าเราคือกระดานสีขาวดำที่แสนคุ้นเคย"
        "เป็นไปได้ไหมนะที่เราเคยเล่นมันบ่อยๆ"
    
        cat normal "ฉันจะลองดูว่าเธอแก้มันได้เร็วแค่ไหน"
        "เจ้าแมวส้มท้าทายเราพร้อมกับส่งเสียงหัวเราะเล็กๆ"
        "ไม่รู้ว่าทำไม แต่รู้สึกว่าต้องไขปริศนาให้ได้"
        "ไม่งั้นคงไม่สบายใจแน่ๆ"
        hide cat

        show puzzle2_1
        jump answer_roome03
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome03:
    menu:
        "ตอบคำถาม":
            "ถ้าอยากเดิน Rook ไป A2 ให้ตอบว่า Ra2 นะ \nถ้า King ให้บอก K \nถ้า Pawn คือไม่ต้องระบุอะไรนะ ระบุช่องที่จะเดินได้เลย"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "ra6":
                cat "เชิงหนาใช้ได้นะเนี่ย"
                show puzzle2_2 with dissolve
                hide puzzle2_1
                ".."
                show puzzle2_3 with dissolve
                hide puzzle2_2
                cat "เดินยังไงต่อดีล่ะ"
                $ input_value = renpy.input("Answer?")
                if prepare(input_value) == "rxa7#":
                    yume "Check Mate"
                    $ room03_is_pass = True
                    "สีขาวกลืนกินทุกอย่าง ภาพในอดีตปรากฏขึ้นต่อหน้า"
                    hide puzzle2_3
                    jump after_room_3
                if prepare(input_value) == "ra7":
                    cat "ลืมบอกว่า Check Mate รึเปล่า? Rxa7#"
                    hide puzzle2_3
                    show puzzle2_1 with dissolve
                    jump answer_roome03
                cat "เกือบจะชนะแล้วแท้ๆ ลองใหม่ดีไหม?"
                hide puzzle2_3
                show puzzle2_1 with dissolve
                jump answer_roome03
            if prepare(input_value) == "ra2":
                cat "เค้าแค่ยกตัวอย่าง"
                jump answer_roome03

            if prepare(input_value) == "ra7":
                cat "ลืมบอกว่ารุกรึเปล่า Rxa7+"
                jump answer_roome03
            if prepare(input_value) == "rxa7":
                cat "ลืมบอกว่ารุกรึเปล่า Rxa7+"
                jump answer_roome03
            if prepare(input_value) == "rxa7+":
                cat "หมากนี้เล่นต่อน่าจะแพ้นะ"
                jump answer_roome03
            if prepare(input_value) == "b7":
                cat "ลืมบอกว่ารุกรึเปล่า xB7"
                jump answer_roome03
            if prepare(input_value) == "bx7":
                cat "แบบนี้เกมส์น่าจะเสมอนะ"
                jump answer_roome03
            
            cat "ไม่ได้คล้ายเลยเธอ"
            jump answer_roome03
        "ใบ้หน่อยสิ":
            cat "คุ้นๆ Paul Morphy's problem บ้างไหม"
            jump answer_roome03
        "กลับห้องโถง":
            hide puzzle2_1
            jump main_map
    


label after_room_3:
    stop music
    play music 星が輝く冬
    scene fb1 with dissolve
    
    yume "ฉันมองเห็นแล้ว"
    mary0 "เห็นอะไรเหรอจ้ะ?"
    yume  "เส้นทางสู่ชัยชนะของฉัน"
    mary0  "รุกฆาตจ้ะ"
    yume  "เฮ้ย!"
    mary0  "มัวแต่ดูหมากตัวเอง แล้วไม่ดูหมากศัตรูก็แบบนี้แหละจ้ะ"
    yume  "ไม่จริงน่า แพ้อีกแล้ว!"
    mary0  "แข่งกัน 30 ครั้ง เธอชนะฉัน 3 ครั้ง แค่นี้ก็สุดยอดมากแล้วนะ"
    yume  "3 ครั้งที่ชนะนั่น เธอดันเล่นไปหมากรุกไปดูหนังไปอีกต่างหาก โอย..."
    mary0  "อย่าคิดมากสิจ้ะ ฉันก็แค่เก่งกว่าเธอมากๆๆๆเท่านั้นเอง"
    yume  "ไม่ต้องย้ำคำว่า ‘มาก’ หลายๆครั้งก็ได้น่า"
    mary0  "ฉันรอวันที่เธอจะชนะฉันอีกนะจ้ะ"
    yume  "ฉันจะลองดู"
    mary0  "สงสัยคงต้องเลือกหนังสักเรื่องล่วงหน้าก่อน อืม...เอาเรื่องนี้ดีไหมนะ?"
    yume  "เธอกะออมมือเต็มที่เลยนี่หว่า!"
    mary0  "ถ้าเธอแพ้จนหมดใจ ฉันจะเล่นกับใครล่ะจ้ะ?"
    yume  "วันหลังฉันไปพาแมวที่บ้านมาเล่นแทนฉัน"
    mary0  "เล่นหมากรุกกับแมวนี่เล่นกับตัวเองยังสนุกกว่าเลยจ้ะ"
    yume  "เธอเล่นกับตัวเองมันจะได้อะไร?"
    mary0  "ถ้าเราเก่งจนอยู่ในจุดที่ชนะได้ทุกคน ก็มีแค่ตัวฉันเองเท่านั้นล่ะจ้ะที่ชนะตัวเองได้"
    yume  "ประโยคเพ้อฝันอย่างกับหลุดมาจากการ์ตูนต่อสู้"
    mary0  "เธอแพ้คนเพ้อฝันบ่อยๆจะนับเป็นตัวอะไรกันล่ะจ้ะ?"
    yume  "ด่ากันขนาดนี้ ลากไปตบกลางสี่แยกยังใจดีกว่านะ"
    mary0  "ไม่ได้ว่าจ้ะ แค่พูดตามความจริง"
    yume  "ยอมไม่ได้แล้ว มาแข่งกันอีกรอบสิ!"
    mary0  "ขอเลือกหนังก่อนเล่นตาต่อไปสักนาทีหนึ่งนะ"
    yume  "อย่าออมมือกับฉันสิ!"
    "เสียงโวยวายของเราสิ้นสุดลง ภาพก็กลับมามืดดำ"

    scene room_s_1080 with dissolve
    play music 哀愁漂うホラー的な
    "เราเริ่มจำได้แล้ว"
    "เรามีใครสักคนหนึ่งที่สำคัญกับเรามากๆ เธอคนนั้นเล่นหมากรุกกับเราประจำ"
    yume "....."
    "ทั้งๆที่สำคัญขนาดนั้น แต่ทำไมเราถึงนึกหน้าของคนคนนั้นไม่ออกนะ"
    "ทำไมกัน?"
    show cat normal
    cat normal "ยินดีด้วยที่ชนะเป็นครั้งที่สี่แล้วนะ"
    yume "หา?"

    cat normal "ไม่มีอะไรหรอก ไปห้องต่อไปกันเถอะ"
    "เจ้าแมวส้มยิ้มให้เราบางๆก่อนจะเดินนำหน้าเรา เราเดินตามมันเพราะไม่มีทางเลือกอื่นใด"
    "หนทางที่จะรู้ความจริง มีแต่แก้ปริศนาเท่านั้น"
    "สู่ประตูบานต่อไป..."

    hide cat
    jump main_map