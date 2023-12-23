
label room04:
    $ _skipping = True
    scene gyokuza_s_1080 with dissolve
    stop music
    play music 不穏

    if room04_is_pass == False:
        play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
        th "เข้ามาข้างในห้องก็เจอกับกระดานดำที่เขียนโจทย์คณิตศาสตร์โชว์หรา"
        en "Upon entering the room, I was greeted by a blackboard covered in complex mathematical equations."
        
        th "Sin cos นี่มันอะไรกันนะ?"
        en "Sin, cos... what are these?"

        th "คุ้นๆเหมือนเคยเรียนแต่ลืมไปแล้ว"
        en "They seem familiar, like something I've learned but forgotten."

        show cat normal with dissolve
        voice "audio/voice/room4/cat_4_000.mp3"
        cat_th normal "ตรีโกณมิติจ้ะ"
        cat_en normal "Trigonometry."

        yume_th "แมวคิดเลขเป็นด้วยเหรอ!?"
        yume_en "You mean, even a cat can do math!?"

        voice "audio/voice/room4/cat_4_001.mp3"
        cat_th ah "ง่ายขนาดแมวยังทำได้ คนทำไม่ได้ก็ไม่รู้จะว่าไงดีอ่ะ"
        cat_en ah "It's so easy that even a cat can do it. I don't know what to say if a person can't."
        
        yume_th "หยามกันขนาดนี้นี่จะท้าทายกันใช่ไหม?"
        yume_en "Is that a challenge?"

        voice "audio/voice/room4/cat_4_002.mp3"
        cat_th smile "จะเรียกว่าท้าทายได้ต้องดูก่อนจ้ะว่าผู้ท้าชิงฉลาดพอไหม?"
        cat_en small "To call it a challenge, we first have to see if the challenger is smart enough."

        th "ทั้งๆที่เราไม่มีร่างกาย แต่ทำไมถึงรู้สึกเหมือนมีเส้นเลือดปูดขึ้นข้างหัวกันนะ?"
        en "Even though I don't have a body, why do I feel like veins are popping on my forehead?"

        th "ชักอยากเอาเจ้าแมวส้มมาเช็ดกระดานแล้วสิ"
        en "I'm starting to want to use that orange cat as an eraser for this board."

        voice "audio/voice/room4/cat_4_003.mp3"
        cat_th normal "ปริศนาข้อนี้ง่ายขนาดแมวยังทำได้ โชคดีนะจ้ะ"
        cat_en normal "This puzzle is so simple, even a cat can solve it. Good luck."

        th "เจ้าแมวส้มว่าแล้วก็ล้มตัวลงนอนกลิ้งกับพื้น"
        en "The orange cat said this and then flopped down to roll on the floor."

        th "แมวทำได้ คนก็ต้องทำได้"
        en "Cats can do it, so humans must be able to do it too."

        th "ให้มันรู้ไปว่าคนไม่มีวันแพ้แมว!"
        en "I'll show it that humans will never lose to cats!"

        hide cat
        show puzzle4
        jump answer_roome04
        
    else :
        th "this room has nothing"
        jump main_map 

label answer_roome04:
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "easierthanyouthink":
                play sound "audio/sfx/correct-6033.mp3" volume 1
    ##voice "audio/voice/room4/cat_4_004.mp3"
                cat_th  "ง่ายกว่าที่เธอคิดใช่ไหม?"
                cat_en "Easier than you think?"
                $ room04_is_pass = True
                th "หลังจากตอบคำถามได้ สีขาวก็ปกคลุมการมองเห็นของเรา"
                en "white enveloped my vision once again."
                hide puzzle4
                jump after_room_4

            if prepare(input_value) == "passwordiseasierthanyouthink":
    ##voice "audio/voice/room4/cat_4_005.mp3"
                cat_th "ทำไมถึงอ่านตามกระดานอย่างนั้นล่ะ"
                cat_en "Why are you reading the board like that?"
                jump answer_roome04
            
            if prepare(input_value) == "iseasierthanyouthink":
    ##voice "audio/voice/room4/cat_4_006.mp3"
                cat_th "แปลกๆอยู่นะ มันน่าจะเป็นคณิตศาสตร์รึเปล่า"
                cat_en "It's strange. Could it be mathematics?"
                jump answer_roome04
            if prepare(input_value) == "0":
    ##voice "audio/voice/room4/cat_4_007.mp3"
                cat_th "ไม่ใช่ว่าเจออะไรก็ตอบ 0 ก่อนสิ"
                cat_en "It's not like you should answer '0' for everything you encounter."
                jump answer_roome04
            if prepare(input_value) == "1":
    ##voice "audio/voice/room4/cat_4_008.mp3"
                cat_th "ฉันว่าเธอน่าจะบวกเลขผิดนะ"
                cat_en "I think you might have added the numbers incorrectly."
                jump answer_roome04
            if prepare(input_value) == "2":
    ##voice "audio/voice/room4/cat_4_009.mp3"
                cat_th "เธอไปหาคำตอบมาจริงๆหรอเนี่ย แต่เสียใจด้วยจ้ะ"
                cat_en "Did you really go look for the answer? But I'm sorry to say."
                jump answer_roome04
            else :
    ##voice "audio/voice/room4/cat_4_010.mp3"
                cat_th "ผิดจ้า"
                cat_en "Wrong."
                jump answer_roome04
        "ใบ้หน่อยสิ":
    ##voice "audio/voice/room4/cat_4_011.mp3"
            cat_th "X^3 + Y^3 = (X+Y) * (X^2 - XY + Y^2)  
            \nเห็นไหมล่ะ? Easier Than You Think"
            cat_en "X^3 + Y^3 = (X+Y) * (X^2 - XY + Y^2)  
            \nSee? Easier Than You Think"
            jump answer_roome04
        "return":
            hide puzzle4
            jump main_map
    
label after_room_4:
    scene fb2_1 with dissolve
    stop music
    play music 星が輝く冬

    yume_th "เธอรู้ว่าฉันสอบเลขไม่ผ่าน ใจคอยังจะให้ตอบปริศนาเลขอีกเหรอ?"
    yume_en "You know I failed my math exam. Are you really going to make me solve a mathematical puzzle?"

    voice "audio/voice/room4/mary_4_000.mp3"
    mary0_th "ตรีโกณมิติที่แมวก็ยังทำได้จ้ะ เธอเป็นคนอย่าเพิ่งยอมแพ้สิจ้ะ"
    mary0_en "It's trigonometry that even a cat can do. Don't give up just because you're human."

    yume_th "โจทย์มันเขียนมามึนๆงี้จะให้ทำยังไง?"
    yume_en "How am I supposed to solve it when the problem is written so confusingly?"

    # voice "audio/voice/room4/mary_4_001.mp3"
    mary0_th "....."
    mary0_en "....."

    yume_th "แล้วข้างล่างที่เขียนว่า ‘ง่ายกว่าที่คิด’ นี่มันอะไรกัน?"
    yume_en "And what about the part written below that says ‘easier than you think’?"

    # voice "audio/voice/room4/mary_4_002.mp3"
    mary0_th "....."
    mary0_en "....."

    yume_th "อย่าเงียบเป็นเป่าสากสิ ใบ้ฉันหน่อย!" 
    yume_en "Don't be as silent as a statue, give me a hint!"

    voice "audio/voice/room4/mary_4_003.mp3"
    mary0_th "Password is easier than you think จ้ะ"
    mary0_en "Password is easier than you think"

    yume_th "What?"
    yume_en "What?"

    voice "audio/voice/room4/mary_4_004.mp3"
    mary0_th "Password is easier than you think จ้ะ"
    mary0_en "Password is easier than you think"

    yume_th "ฉันไม่ได้บอกให้เธออ่านซ้ำ ฉันบอกให้เธอใบ้ฉัน"
    yume_en "I didn't ask you to repeat it, I asked for a hint."

    voice "audio/voice/room4/mary_4_005.mp3"
    mary0_th "คำใบ้บางคำเท่ากับการเฉลยแล้วจ้ะ"
    mary0_en "Sometimes a hint is equivalent to giving away the answer."

    yume_th "หา?"
    yume_en "Huh?"

    voice "audio/voice/room4/mary_4_006.mp3"
    mary0_th "คิดดูดีๆสิจ้ะ ถ้าฉันรู้ว่าเธอไม่เก่งเลข ฉันจะใจร้ายขนาดเอาปริศนาเลขมาให้เธอทำไหม?"
    mary0_en "Think about it. If I knew you weren't good at math, why would I be so cruel as to give you a math puzzle?"

    yume_th "คิด"
    yume_en "Thinking"


    ##voice "audio/voice/room4/mary_4_007.mp3"
    mary0_th "....."
    mary0_en "....."

    yume_th "เธอดูเหมือนพวกที่จะหัวเราะเยาะเพื่อนทุกครั้งที่ตัวเองฉลาดกว่าน่ะ"
    yume_en "You seem like the type to laugh at friends every time you're smarter than them."

    voice "audio/voice/room4/mary_4_008.mp3"
    mary0_th "ใจร้าย!"
    mary0_en "That's mean!"

    yume_th "ทีนี้ช่วยใบ้ฉันให้ชัดกว่านี้ที ฉันขอล่ะ"
    yume_en "Now give me a clearer hint. I'm asking you, please."

    voice "audio/voice/room4/mary_4_009.mp3"
    mary0_th "ไม่มีชัดกว่านี้แล้วจ้ะ"
    mary0_en "There's no clearer hint than this."

    yume_th "จริงรึ?"
    yume_en "Really?"

    voice "audio/voice/room4/mary_4_010.mp3"
    mary0_th "จริงอ่ะดิ"
    mary0_en "Really."

    yume_th "........."
    th "เราพูดไม่ออก สุดท้ายเราก็ได้แต่นั่งจิ้มกระดาษทายปริศนาของคนตรงหน้า"
    th "น่าเจ็บใจจริงๆ"

    scene gyokuza_s_1080 with dissolve
    yume_th "เฮ้อ..."
    yume_en "Sigh..."

    th "ปริศนาเลขบ้าอะไรกัน? ตรีโกณมิติบ้าอะไรกัน?"
    en "What's with this absurd math puzzle? Trigonometry? Seriously?"
    
    th "นี่มันโจทย์กวนประสาทชัดๆ!"
    en "It's a downright annoying question!"
    
    show cat normal
    
    voice "audio/voice/room4/cat_4_012.mp3"
    cat_th normal "ในที่สุดก็ไขปริศนาได้ แต่ก็ยังตอบช้ากว่าแมวนะจ้ะ"
    cat_en normal "Finally, you solved the puzzle. But still slower than a cat."
    th "ถ้าเรายังมีใบหน้าอยู่ เราคงเบิกตาโพลงใส่แมวส้มไปแล้ว"
    en "If I still had a face, I would probably be staring wide-eyed at the orange cat by now."

    yume_th "คำตอบมันบอกกันโต้งๆเลยนี่ แล้วจะมีโจทย์ข้างบนทำไม?"
    yume_en "The answer was spelled out so blatantly, then why have the problem in the first place?"
    
    voice "audio/voice/room4/cat_4_013.mp3"
    cat_th normal "เพื่อขายขำจ้ะ"
    cat_en normal "For fun."
    
    yume_th "......" 
    yume_en "......"
    
    voice "audio/voice/room4/cat_4_014.mp3"
    cat_th normal "ทำไมเธอเข้าใกล้ฉันขนาดนั้นล่ะจ้ะ?"
    cat_en normal "Why are you getting so close to me?"
    
    yume_th "จะยกแกไปเช็ดกระดาน หมั่นไส้"
    yume_en "I'm going to use you as an eraser for that board, you're annoying."
    voice "audio/voice/room4/cat_4_015.mp3"
    cat_th normal "ใจร้ายกับแมวชะมัด!"
    cat_en normal "So cruel to a cat!"

    th "เจ้าแมวส้มรีบวิ่งหนีจากเรา เราจึงวิ่งตามมัน"
    en "The orange cat quickly ran away from me, and I chased after it."

    th "...สู่ประตูต่อไป..."
    en "...Towards the next door..."

    hide cat
    jump cutscene_main
