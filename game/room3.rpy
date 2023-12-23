label room03:
    $ _skipping = True
    scene room_s_1080 with dissolve
    stop music
    play music 哀愁漂うホラー的な


    if room03_is_pass == False: 
        show cat normal with dissolve
        yume_th "หมากรุก?"
        yume_en "Chess?"
        
        th "สิ่งที่ปรากฏต่อหน้าเราคือกระดานสีขาวดำที่แสนคุ้นเคย"
        en "What appeared before us was a familiar black and white chessboard." 
        
        th "เป็นไปได้ไหมนะที่เราเคยเล่นมันบ่อยๆ"
        en "Is it possible that I used to play it frequently?"
        
        voice "audio/voice/room3/cat_3_000.mp3"
        cat_th normal "ฉันจะลองดูว่าเธอแก้มันได้เร็วแค่ไหน"
        cat_en normal "Let's see how fast you can solve this."

        th "เจ้าแมวส้มท้าทายเราพร้อมกับส่งเสียงหัวเราะเล็กๆ"
        en "The orange cat challenged me with a small laugh."

        th "ไม่รู้ว่าทำไม แต่รู้สึกว่าต้องไขปริศนาให้ได้"
        en "I don't know why, but I felt compelled to solve this mystery"
        
        th "ไม่งั้นคงไม่สบายใจแน่ๆ"
        en "or else I would not be at ease."
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
            en "If you want to move the Rook to A2, say 'Ra2'. \nFor the King, just say 'K'. \nFor a Pawn, you don't need to specify anything, just mention the square to move to."
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "ra6":
    ##voice "audio/voice/room3/cat_3_001.mp3"
                
                cat_th "เชิงหนาใช้ได้นะเนี่ย"
                cat_en "Bold moves can work."
                show puzzle2_2 with dissolve
                hide puzzle2_1
                ".."
                show puzzle2_3 with dissolve
                hide puzzle2_2
    ##voice "audio/voice/room3/cat_3_002.mp3"
                cat_th "เดินยังไงต่อดีล่ะ"
                cat_en "What should be the next move?"
                $ input_value = renpy.input("Answer?")
                if prepare(input_value) == "rxa7#" or prepare(input_value) == "ra7#":
                    play sound "audio/sfx/correct-6033.mp3" volume 1
                    yume_th "Check Mate"
                    yume_en "Check Mate"
                    $ room03_is_pass = True
                    th "สีขาวกลืนกินทุกอย่าง ภาพในอดีตปรากฏขึ้นต่อหน้า"
                    en "White engulfs everything once again, and a vague memory surfaces."
                    hide puzzle2_3
                    jump after_room_3
                if prepare(input_value) == "ra7":
    ##voice "audio/voice/room3/cat_3_003.mp3"
                    cat_th "ลืมบอกว่า Check Mate รึเปล่า? Rxa7#"
                    cat_en "Did you forget to say Check Mate? Rxa7#"
                    hide puzzle2_3
                    show puzzle2_1 with dissolve
                    jump answer_roome03
    ##voice "audio/voice/room3/cat_3_004.mp3"
                cat_th "เกือบจะชนะแล้วแท้ๆ ลองใหม่ดีไหม?"
                cat_en "You were almost winning. Want to try again?"
                hide puzzle2_3
                show puzzle2_1 with dissolve
                jump answer_roome03
            if prepare(input_value) == "ra2":
    ##voice "audio/voice/room3/cat_3_005.mp3"
                cat_en "It's just an example."
                cat_th "เค้าแค่ยกตัวอย่าง"
                jump answer_roome03

            if prepare(input_value) == "ra7":
    ##voice "audio/voice/room3/cat_3_006.mp3"
                cat_en "Did you forget to say it's an attack? Rxa7+"
                cat_th "ลืมบอกว่ารุกรึเปล่า Rxa7+"
                jump answer_roome03
            if prepare(input_value) == "rxa7":
    ##voice "audio/voice/room3/cat_3_007.mp3"
                cat_th "ลืมบอกว่ารุกรึเปล่า Rxa7+"
                cat_en "Did you forget to say it's an attack? Rxa7+"
                jump answer_roome03
            if prepare(input_value) == "rxa7+":
    ##voice "audio/voice/room3/cat_3_008.mp3"
                cat_th "หมากนี้เล่นต่อน่าจะแพ้นะ"
                cat_en "Continuing this move should lead to a loss."
                jump answer_roome03
            if prepare(input_value) == "b7":
    ##voice "audio/voice/room3/cat_3_009.mp3"
                cat_th "ลืมบอกว่ารุกรึเปล่า xB7"
                cat_en "Did you forget to say it's an attack? xB7"
                jump answer_roome03
            if prepare(input_value) == "bx7":
    ##voice "audio/voice/room3/cat_3_010.mp3"
                cat_th "แบบนี้เกมส์น่าจะเสมอนะ"
                cat_en "With this, the game should end in a draw."
                jump answer_roome03
            
    ##voice "audio/voice/room3/cat_3_011.mp3"
            cat_th "ไม่ได้คล้ายเลยเธอ"
            cat_en "It's not similar at all."
            jump answer_roome03
        "ใบ้หน่อยสิ":
    ##voice "audio/voice/room3/cat_3_012.mp3"
            cat_th "คุ้นๆ Paul Morphy's problem บ้างไหม"
            cat_en "Do you recognize Paul Morphy's problem?"
            jump answer_roome03
        "กลับห้องโถง":
            hide puzzle2_1
            jump main_map
    


label after_room_3:
    stop music
    play music 星が輝く冬
    scene fb1 with dissolve
    
    yume_th "ฉันมองเห็นแล้ว"
    yume_en "I see it now."

    voice "audio/voice/room3/mary_3_000.mp3"
    mary0_th "เห็นอะไรเหรอจ้ะ?"
    mary0_en "What do you see?"

    yume_th  "เส้นทางสู่ชัยชนะของฉัน"
    yume_en "My path to victory."

    voice "audio/voice/room3/mary_3_001.mp3"
    mary0_th  "รุกฆาตจ้ะ"
    mary0_en "Checkmate"

    yume_th  "เฮ้ย!"
    yume_en "Hey!"

    voice "audio/voice/room3/mary_3_002.mp3"
    mary0_th  "มัวแต่ดูหมากตัวเอง แล้วไม่ดูหมากศัตรูก็แบบนี้แหละจ้ะ"
    mary0_en "That's what happens when you only focus on your pieces and ignore your opponent's."

    yume_th  "ไม่จริงน่า แพ้อีกแล้ว!"
    yume_en "That's not true. I lost again!"

    voice "audio/voice/room3/mary_3_003.mp3"
    mary0_th  "แข่งกัน 30 ครั้ง เธอชนะฉัน 3 ครั้ง แค่นี้ก็สุดยอดมากแล้วนะ"
    mary0_en "Out of 30 games, you've won 3. That's quite impressive already."

    yume_th  "3 ครั้งที่ชนะนั่น เธอดันเล่นไปหมากรุกไปดูหนังไปอีกต่างหาก โอย..."
    yume_en "Those 3 wins were when you were playing chess, watching a movie, and distracted. Oh dear..."

    voice "audio/voice/room3/mary_3_004.mp3"
    mary0_th  "อย่าคิดมากสิจ้ะ ฉันก็แค่เก่งกว่าเธอมากๆๆๆเท่านั้นเอง"
    mary0_en "Don't overthink it. I'm just much, much better than you."

    yume_th  "ไม่ต้องย้ำคำว่า ‘มาก’ หลายๆครั้งก็ได้น่า"
    yume_en "You don't have to emphasize 'much' so many times."

    voice "audio/voice/room3/mary_3_005.mp3"
    mary0_th  "ฉันรอวันที่เธอจะชนะฉันอีกนะจ้ะ"
    mary0_en "I'm looking forward to the day you beat me again."

    yume_th  "ฉันจะลองดู"
    yume_en "I'll try."

    voice "audio/voice/room3/mary_3_006.mp3"
    mary0_th  "สงสัยคงต้องเลือกหนังสักเรื่องล่วงหน้าก่อน อืม...เอาเรื่องนี้ดีไหมนะ?"
    mary0_en  "I guess I should pick a movie in advance. Hmm... how about this one?"

    yume_th  "เธอกะออมมือเต็มที่เลยนี่หว่า!"
    yume_en "You're really holding back, aren't you!"
    
    voice "audio/voice/room3/mary_3_007.mp3"
    mary0_th  "ถ้าเธอแพ้จนหมดใจ ฉันจะเล่นกับใครล่ะจ้ะ?"
    mary0_en "If you lose hope, who will I play with?"

    
    yume_th  "วันหลังฉันไปพาแมวที่บ้านมาเล่นแทนฉัน"
    yume_en "Next time, I'll bring the cat from home to play instead of me."

    voice "audio/voice/room3/mary_3_008.mp3"
    mary0_th  "เล่นหมากรุกกับแมวนี่เล่นกับตัวเองยังสนุกกว่าเลยจ้ะ"
    mary0_en "Playing chess with a cat is even more boring than playing alone."

    yume_th  "เธอเล่นกับตัวเองมันจะได้อะไร?"
    yume_en "What's the point of playing by yourself?"

    voice "audio/voice/room3/mary_3_009.mp3"
    mary0_th  "ถ้าเราเก่งจนอยู่ในจุดที่ชนะได้ทุกคน ก็มีแค่ตัวฉันเองเท่านั้นล่ะจ้ะที่ชนะตัวเองได้"
    mary0_en "If one is skilled enough to beat everyone, the only challenge left is to beat oneself."

    yume_th  "ประโยคเพ้อฝันอย่างกับหลุดมาจากการ์ตูนต่อสู้"
    yume_en "That sounds like a delusional line from a fighting manga."

    voice "audio/voice/room3/mary_3_010.mp3"
    mary0_th  "เธอแพ้คนเพ้อฝันบ่อยๆจะนับเป็นตัวอะไรกันล่ะจ้ะ?"
    mary0_en "What does it say about you if you keep losing to a dreamer?"

    yume_th  "ด่ากันขนาดนี้ ลากไปตบกลางสี่แยกยังใจดีกว่านะ"
    yume_en "Insulting me like this, dragging me to a public square for a beating would be kinder."

    voice "audio/voice/room3/mary_3_011.mp3"
    mary0_th  "ไม่ได้ว่าจ้ะ แค่พูดตามความจริง"
    mary0_en "I'm not insulting you, just stating the truth."

    yume_th  "ยอมไม่ได้แล้ว มาแข่งกันอีกรอบสิ!"
    yume_en "I can't take it anymore. Let's play another round!"

    voice "audio/voice/room3/mary_3_012.mp3"
    mary0_th  "ขอเลือกหนังก่อนเล่นตาต่อไปสักนาทีหนึ่งนะ"
    mary0_en "Let me pick a movie for the next game, just a minute."
    
    yume_th  "อย่าออมมือกับฉันสิ!"
    yume_en "Don't hold back on me!"
    
    th "เสียงโวยวายของเราสิ้นสุดลง ภาพก็กลับมามืดดำ"
    en "Our arguing ceased, and everything returned to darkness."

    scene room_s_1080 with dissolve
    play music 哀愁漂うホラー的な
    
    th "เราเริ่มจำได้แล้ว"
    en "I'm starting to remember."
    
    th "เรามีใครสักคนหนึ่งที่สำคัญกับเรามากๆ เธอคนนั้นเล่นหมากรุกกับเราประจำ"
    en "There was someone very important to me, someone who often played chess with me."

    yume_th "....."
    yume_en "....."

    th "ทั้งๆที่สำคัญขนาดนั้น แต่ทำไมเราถึงนึกหน้าของคนคนนั้นไม่ออกนะ"
    en "Even though they were that important, why can't I recall their face? Why is that?"

    show cat normal
    voice "audio/voice/room3/cat_3_013.mp3"
    
    cat_th normal "ยินดีด้วยที่ชนะเป็นครั้งที่สี่แล้วนะ"
    cat_en normal "Congratulations on your fourth win"

    yume_th "หา?"
    yume_en "What?"

    voice "audio/voice/room3/cat_3_014.mp3"
    cat_th normal "ไม่มีอะไรหรอก ไปห้องต่อไปกันเถอะ"
    cat_en normal "Nothing much, let's move to the next room."

    th "เจ้าแมวส้มยิ้มให้เราบางๆก่อนจะเดินนำหน้าเรา เราเดินตามมันเพราะไม่มีทางเลือกอื่นใด"
    en "The orange cat gave me a faint smile before walking ahead."
    
    th "หนทางที่จะรู้ความจริง มีแต่แก้ปริศนาเท่านั้น"
    en "I followed because there was no other choice. The only way to uncover the truth is to solve these puzzles."

    th "สู่ประตูบานต่อไป..."
    en "Towards the next door..."


    hide cat
    jump cutscene_main
