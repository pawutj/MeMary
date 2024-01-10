
label room02:
    $ _skipping = True
    scene library_n_1080 with dissolve
    stop music
    play music 不穏

    
    if room02_is_pass == False: 
        play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
        show cat normal with dissolve
        th "น่าแปลก"
        en "It's curious."

        th "ทั้งๆที่เราไม่ควรจะมีความทรงจำเหลืออยู่ แต่ทำไมเราถึงรู้จักอักษรพวกนี้ได้"
        en "Even though I shouldn't have any remaining memories, why do I recognize these characters?"
        
        th "...เป็นไปได้หรือเปล่าว่าตัวตนของเราค่อยๆกลับมาระหว่างการไขปริศนา..."
        en "Could it be that my true self is slowly resurfacing as I solve this puzzle?"

        th "ถ้าเป็นอย่างนั้น เราก็คงต้องตอบคำถามข้อนี้ให้ได้"
        en "If that's the case, I must find the answer to this question."
        hide cat

        
        jump answer_room2
        
    else :
        th "this room has nothing"
        jump main_map 
label answer_room2:
    show puzzle3 with dissolve
    menu:
        "Answer":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "oblivion":
                cat_th "ลองไปหาใน Clue สิ"
                hide puzzle3
                jump answer_room2

            if prepare(input_value) == "recall":
                $ room02_is_pass = True
                play sound "audio/sfx/correct-6033.mp3" volume 1
                th "สีขาวกลืนกินทุกอย่างอีกครั้ง ภาพความทรงจำอันลางเรือนปรากฏขึ้น"
                en "White engulfs everything once again, and a vague memory surfaces."
                hide puzzle3
                jump after_room_2

            if prepare(input_value) == "idol":
                hide puzzle3

                jump easteregg_3

            if prepare(input_value) == "rune":
    ##voice "audio/voice/room2/cat_2_000.mp3"
                cat_th "ลองเทียบอักษรดูสิ"
                cat_en "Try comparing the letters."
                hide puzzle3
                jump answer_room2
            if prepare(input_value) == "obliion":
    ##voice "audio/voice/room2/cat_2_001.mp3"
                cat_th "คำมันแปลกๆอยู่นะ ลองๆเติมอะไรให้มันอ่านออกมั้ย"
                cat_en "The words are strange, aren't they? Try filling in something to make them readable."
                hide puzzle3
                jump answer_room2
            else :
    ##voice "audio/voice/room2/cat_2_002.mp3"
                cat_th "ผิดจ้า"
                cat_en "Wrong."
                jump answer_room2
        "Hint":
    ##voice "audio/voice/room2/cat_2_003.mp3"
            cat_th "ดูถ้าจะคล้ายๆกับ อักษรรูน นะ ดูเหมือนจะเทียบอักษรเป็นภาษาอังกฤษได้อยู่นะ"
            cat_en "It looks similar to Rune letters. It seems like they can be compared to English letters."
            jump answer_room2

        "Skip Answer":
                hide puzzle2
                $ room02_is_pass = True
                jump after_room_2
        "Return to Hall":
            hide puzzle3
            jump main_map
    

label after_room_2:
    stop music
    play music up_to_you
    scene fb1 with dissolve
    yume_th "อักษรหน้าตาประหลาดพวกนี้คืออะไร?"
    yume_en "What are these strange characters?"
    
    voice "audio/voice/room2/mary_2_000.mp3"
    mary0_th "มันคืออักษรรูนจ้ะ"
    mary0_en "They are runes, ancient European letters."

    yume_th "อ่านไม่เห็นออกเลย มันมีไว้ทำอะไรรึ?"
    yume_en "I can't read them at all. What are they for?"
    
    voice "audio/voice/room2/mary_2_001.mp3"
    mary0_th "มันเป็นอักษรโบราณของคนยุโรปน่ะ ฉันเห็นว่ามันเท่ดีเลยจะเอามาทำปริศนาทายเธอ"
    mary0_en "They are ancient letters used by Europeans. I thought they looked cool, so I decided to create a riddle with them for you."

    yume_th "ปริศนาอีกแล้วเหรอ?"
    yume_en "Another riddle?"

    voice "audio/voice/room2/mary_2_002.mp3"
    mary0_th "ใช่สิ ของน่าสนใจแบบนี้จะหลุดรอดได้ยังไง"
    mary0_en "Of course! How could I let something as interesting as this slip by?"
    
    yume_th "เธอสนใจ แต่ฉันไม่สนใจน่ะสิ"
    yume_en "You may be interested, but I'm not."
    
    voice "audio/voice/room2/mary_2_003.mp3"
    mary0_th "อย่างน้อยๆก็แกล้งทำเป็นสนใจในฐานะที่เราสนิทกันเถอะน้า--"
    mary0_en "At least pretend to be interested, for the sake of our friendship--"

    yume_th "....."
    yume_en "....."
    
    voice "audio/voice/room2/mary_2_004.mp3"
    mary0_th "นะๆๆๆ"
    mary0_en "Please?"

    yume_th "สนใจก็ได้"
    yume_en "Fine, I'm interested."

    voice "audio/voice/room2/mary_2_005.mp3"
    mary0_th "เย้! ในที่สุดก็มีเพื่อนไว้กวนประสา...เอ้ย ไว้เล่นด้วยแล้ว"
    mary0_en "Yay! Finally, I have a friend to tease... I mean, to play with."

    yume_th "เมื่อกี้ฉันไม่ได้หูแว่วใช่ไหม?"
    yume_en "I didn't mishear that, did I?"

    voice "audio/voice/room2/mary_2_006.mp3"
    mary0_th "ไม่มี๊ ไม่มี"
    mary0_en "Nope, not at all!"

    yume_th "ยิ้มน่าสงสัยชะมัด"
    yume_en "That smile looks suspicious."

    voice "audio/voice/room2/mary_2_007.mp3"
    mary0_th "ฮะๆๆ เดี๋ยวฉันจะสอนอ่านอักษรพวกนี้ให้นะ" 
    mary0_en "Ha ha, soon I'll teach you how to read these letters."

    yume_th "ลองสักตั้งก็ได้ ไหนๆก็ไม่มีอะไรทำอยู่แล้ว"
    yume_en "Might as well try. I’ve got nothing else to do anyway."

    voice "audio/voice/room2/mary_2_008.mp3"
    mary0_th "ไม่มีอะไรทำ? แสดงว่าทำการบ้านเสร็จหมดแล้วเหรอ?"
    mary0_en "Nothing else to do? Does that mean you've finished all your homework?"

    yume_th "ใช่"
    yume_en "Yes."

    voice "audio/voice/room2/mary_2_009.mp3"
    mary0_th "ทำเร็วมาก สุดยอดเลยจ้า"
    mary0_en "That was quick. You're amazing!"

    yume_th "ขอบคุณที่ชม..."
    yume_en "Thanks for the compliment..."

    voice "audio/voice/room2/mary_2_010.mp3"
    mary0_th "ขอลอกหน่อยสิจ้ะ"
    mary0_en "Let me copy it, will you?"

    yume_th "เอาความรู้สึกดีๆฉันคืนมาเลยนะ"
    yume_en "Give me back my good feelings right now."

    
    scene library_n_1080 with dissolve
    show cat normal

    th "เรากลับมาที่ห้องเดิมแล้ว"
    en "We return to the original room."

    th "เราเข้าใจอักษรพวกนี้เพราะเคยมีใครบางคนสอนเรา"
    en "I understand these characters because someone once taught me."

    th "...เหมือนลืมบางอย่างที่สำคัญมากๆเลย..."
    en "...It's like I've forgotten something very important..."

    voice "audio/voice/room2/cat_2_004.mp3"
    cat_th normal "พยายามนึกให้ออกตอนนี้ยังเร็วไปนะ"
    cat_en normal "Trying to remember now is still too early."

    yume_th "....."
    yume_en "....."

    voice "audio/voice/room2/cat_2_005.mp3"
    cat_th ah "ประตูยังมีอีกหลายบาน เธอต้องมุ่งหน้าต่อไป"
    cat_en ah "There are many more doors to open. You must keep going forward."

    th "เจ้าแมวส้มเดินนำหน้าเราประมาณสองช่วงตัวคน เราจึงค่อยๆเดินตามมัน"
    en "The orange cat walks about two body lengths ahead of me, and I slowly follow it."
    
    th "...สู่ประตูต่อไป..."
    en "...Towards the next door..."
    hide cat
    jump cutscene_main

label easteregg_3:
    scene white with Dissolve(3)

    th "ใช่แล้วฉันนึกออกแล้ว ความรู้สึกนี้ เสียงของผู้คนรอบกาย"
    en "Yes, I remember now. This feeling, the voices of people around."
    #เสียงเชีย

    th "ณ สถานที่แห่งนี้ เธอนี่แหละคือไอดอลของทุกคน!!"
    en "Here at this place, you are everyone's idol!!"
    $ persistent.cg_pass[2] = True
    scene idol00 with Dissolve(2)

    th "เสียงเชียร์ของทุกคน กำลังกลายเป็นพลังให้กับเธอผู้นี้"
    en "The cheers of everyone are turning into power for you."

    #[mary_e3_000]
    mary0_th "ทุกคนนน ใครร้องได้ช่วยกันร้องด้วยนะ"
    mary0_en "Everyone, anyone who can sing, please sing along."

    #เสียงเชีย
    #[mary_e3_001]
    mary0_th "โปรดจงรับความรู้สึกที่ออกมาจากหัวใจของฉัน ขอส่งต่อมันให้กับทุกคนในเวทีแห่งนี้!!" 
    mary0_en "Please accept the feelings coming from my heart. I want to convey them to everyone on this stage!!"

    #[mary_e3_002]
    mary0_th "MeMary X'mas!!" 
    mary0_en "MeMary X'mas!!"

    #เสียงเชีย
    scene white with Dissolve(3)
    th "......"
    en "......"

    scene library_n_1080 with Dissolve(1)

    yume_th "นี่ฉันเป็นติ่งไอดอลอย่างงั้นเหรอ!?"
    yume_en "Am I an idol fan like this!?"

    #[cat_e3_000]
    cat_th "จะไปใช่ได้ไงเล่า!" 
    cat_en "How could that be possible!"

    jump answer_room2
