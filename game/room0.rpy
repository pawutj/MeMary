label memary_scene:



    scene memary  with Dissolve(5.0)
    $ renpy.pause(1 , hard=True)
    scene nameless with Dissolve(3.0)
    $ renpy.pause(1 , hard=True)
    scene black with Dissolve(3.0)

    jump after_room_0_1
    return 

label intro:    
 
    #Just Test

    scene rouka_s_1080
    play music 廃墟洋館
    
    th "... เส้นทางที่ไม่รู้จุดหมายทอดยาวต่อหน้าเรา..."
    en "... A path with no known destination stretches out before me..."
    
    th "ที่นี่คือที่ไหนกัน?"
    en "Where is this place?"

    th "ตัวเราคือใครกัน?"
    en "Where is this place?"

    th "....."
    en "....."

    th "ความมืดมิดโอบล้อมรอบร่างกายจนกระทั่งเราลืมตาตื่นขึ้น"
    en "As darkness envelops my body, I open my eyes to wakefulness."

    th "ทัศนะการมองเห็นค่อยๆกลับมาแจ่มชัด"
    en "My vision gradually becomes clearer."
    
    th "ร่างกายที่รู้สึกหนักหน่วงค่อยๆเบาบางลง"
    en "My heavy body slowly feels lighter."

    th "สิ่งแรกที่เราทำหลังจากหยั่งยืนบนพื้นทางเดินอันมืดมนคือจ้องมองแขนขาและเรือนร่างของตัวเอง"
    en "The first thing I do after standing on the dark path is to gaze at my arms, legs, and body."
    
    yume_th "นี่มัน...."
    yume_en "This is...."

    yume_th "น้ำเสียงของเราแหบพร่าอย่างผิดปกติ"
    yume_en "My voice is unusually hoarse."
    
    yume_th "แต่สิ่งที่น่าประหลาดยิ่งกว่านั้นคือร่างกายของเรากลับมีเพียงความว่างเปล่า"
    yume_en "But what's more strange is that my body is just emptiness."

    yume_th "...ทำ...ไม...?"
    yume_en "...Why...?"
    
    th "คำพูดของเราขาดห้วง"
    en "My words are incomplete."

    th "ทั้งๆที่เราประสาทสัมผัสบอกเราว่าร่างกายของเรามีอยู่จริง ทั้งแขนทั้งขากำลังขยับตามคำสั่งของเราทุกประการ แต่เมื่อจ้องมองไปยังส่วนที่ควรจะเป็นเรือนร่าง เรากลับพบเพียงอากาศธาตุเท่านั้น"
    en "Even though my senses tell me that my body is real, that my arms and legs are moving as I command, when I gaze at where my body should be, I see only air."

    th "ร่างกาย...ของเรา...?"
    en "My body...?"
    
    th "...นี่เรากำลังล่องหนอยู่เหรอ?"
    en "...Am I a ghost?"

    th "...หรือว่าเราไม่มีร่างกายตั้งแต่แรก?"
    en "Or have I never had a body to begin with?"
    
    th "เราพยายามนึกถึงเหตุผลที่ทำไมเรามาอยู่ตรงนี้ แต่ไม่ว่าพยายามนึกถึงเท่าไหร่ก็นึกไม่ออก"
    en "I try to remember why I am here, but no matter how hard I try, I can't recall."

    th "ที่นี่คือสถานที่ที่เราไม่รู้จัก"
    en "This place is unfamiliar to me."

    th "มันทั้งมืดมิด ทั้งหนาวเหน็บและวังเวงไร้ผู้คน"
    en "It's dark, cold, and eerily empty."

    yume_th "....."
    yume_en "....."

    th "ต้นกำเนิดแสงหนึ่งเดียวมีเพียงแสงสว่างที่ทอดผ่านหน้าต่างบานใหญ่ลงมา"
    en "The only source of light is the moonlight streaming through a large window."
    
    scene moonlight3 with dissolve
    th "ดวงจันทร์สีเงินขนาดใหญ่สาดทอแสง ราวกับมันกำลังจ้องมองเราจากเบื้องบนไม่มีผิด"
    en "The large silver moon seems to be watching me from above."

    th "....."
    en "....."

    th "เราก้มมองร่างกายของตัวเองที่เหลือเพียงความว่างเปล่าพร้อมกับตั้งคำถาม"
    en "I look down at my empty body and ask myself."

    th "ไม่ใช่เพียงร่างกายที่หายไป แต่ความทรงจำข้างในก็กลวงเปล่าเช่นกัน"
    en "Not only is my body gone, but my memories inside are empty as well."

    th "...นี่เรา...เป็นใครกัน?"
    en "I: ...Who am I?"

    th "....."
    en "....."

    scene rouka_s_1080 with dissolve
    voice "audio/voice/room0/cat_0_000.mp3"
    cat0_th "ไม่มีใครมาที่นี่นานแล้ว"
    cat0_en "No one has been here for a long time."

    yume_th "นั่นเสียงใคร?"
    yume_en "Whose voice is that?"
    
    voice "audio/voice/room0/cat_0_001.mp3"
    cat0_th "ก้มลงมองข้างล่างสิ"
    cat0_en "Look down."

    stop music
    play music 不穏
    
    show cat normal with dissolve
    th "เราเผลอมองตามคำพูดลึกลับด้วยความอยากรู้อยากเห็น"
    en "I curiously look down as the mysterious voice suggested."

    th "เจ้าของเสียงเล็กแหลมที่ดังขึ้นข้างกายเรามีขนาดเล็กจ้อยพอๆกับสองฝ่ามือคนเท่านั้น"
    en "The owner of the sharp little voice next to me is as small as two human palms."

    yume_th "...แมว?"
    yume_en "...A cat?"

    th "เราอุทานขึ้นด้วยความตกใจเพราะไม่เคยเห็นสัตว์พูดได้มาก่อน"
    en "I exclaim in surprise as I've never seen a talking animal before."

    th "เจ้าแมวลายส้มหรี่ตามองเราราวกับไม่สบอารมณ์น้อยๆ"
    en "The orange-striped cat squints at me as if slightly displeased."

    voice "audio/voice/room0/cat_0_002.mp3"
    cat_th smile "ไม่ใช่แมว แต่เป็นผู้นำทางต่างหาก"  with dissolve
    cat_en smile "I'm not a cat, but a guide."  with dissolve

    yume_th "ผู้นำทาง?"
    yume_en "A guide?"


    th "แมวลายส้มตากลมโตจ้องมองเราด้วยความประหลาดใจ"
    en "The orange-striped cat with big round eyes looks at me in surprise."
    
    th "ทั้งๆที่แมวไม่ควรจะแสดงสีหน้าได้ชัดเจน แต่แมวตัวนี้กลับแสดงอารมณ์ได้ราวกับเป็นคน"
    en "Even though cats shouldn't be able to express emotions clearly, this one seems to emote like a human."

    voice "audio/voice/room0/cat_0_003.mp3"
    cat_th ah "ดูเหมือนว่าเธอจะไม่รู้อะไรเลยสินะ" with dissolve 
    cat_en ah "It seems you don't know anything." with dissolve 

    yume_th "ฉัน?"
    yume_en "Me?"

    th "เราพูดขึ้นด้วยความสงสัย"
    en "speak, puzzled."

    th "เมื่อถูกถามคำถามนั้น เราก็พยายามนึกถึงเรื่องของตัวเองเพื่อให้ตอบคำถามได้"
    en "When asked that question, I try to think of something about myself to answer."

    yume_th "...อึก!!"
    yume_en "...Ugh!!"

    th "ทันใดที่เราพยายามนึกถึงบางสิ่ง ความเจ็บปวดทรมานก็แล่นไปทั่ว"
    en "As soon as I try to remember something, a painful torment spreads throughout my non-existent body, resisting my own will."

    th "ร่างกายที่ไม่มีอยู่จริงกำลังต่อต้านเจตจำนงของตัวเอง"
    en ""

    th "...นี่มัน...อะไรกัน...?"
    en "...What is this...?"

    voice "audio/voice/room0/cat_0_004.mp3"
    cat_th normal "เธออย่าฝืนจะดีกว่า" with dissolve
    cat_en normal "You better not force it." with dissolve

    yume_th "ฝืน?"
    yume_en "Force?"

    voice "audio/voice/room0/cat_0_005.mp3"
    cat_th lick "ตอนนี้เธอไม่สามารถนึกได้หรอกว่าตัวเธอเป็นใคร"
    cat_en lick "You better not force it."

    yume_th "....."
    yume_en "....."

    voice "audio/voice/room0/cat_0_006.mp3"
    cat_th smile "ถ้าเธออยากได้คำตอบว่าเธอเป็นใคร ทำไมเธอถึงอยู่ที่นี่ เธอมีทางเลือกเดียวเท่านั้น" with dissolve
    cat_th smile "If you want answers about who you are and why you are here, there's only one choice." with dissolve

    yume_th "ทางเลือก?"
    yume_en "A choice?"

    voice "audio/voice/room0/cat_0_007.mp3"
    cat_th  normal "ตามฉันมา" with dissolve
    cat_en  normal "Follow me." with dissolve
    hide cat
    jump room0

label room0:
    yume_th "ประตู?"
    yume_en "A door?"
    show cat normal with dissolve
    voice "audio/voice/room0/cat_0_008.mp3"
    cat_th ah "เปิดเข้าไปสิ"
    cat_en ah "Open it."

    th "เรามองแมวสีส้มด้วยความไม่ไว้ใจ"
    en "I look at the orange cat with distrust."

    th "ดูเหมือนเจ้าแมวส้มจะอ่านความคิดเราออกมา มันเลยพูดขึ้น"
    en "It seems like the orange cat can read my thoughts, so it speaks up."
    voice "audio/voice/room0/cat_0_009.mp3"
    cat_th normal "ฉันเข้าใจว่ามันไม่น่าไว้ใจ แต่ถ้าเธอไม่ทำตามคำพูดฉัน เธอก็ไม่มีทางเลือกอื่นนอกจากกลับไปหลงที่ทางเดินอย่างไร้จุดหมาย" with dissolve
    cat_en normal "I understand it doesn't seem trustworthy, but if you don't follow my words, your only other option is to wander aimlessly back in the corridors." with dissolve
    
    yume_th "....."
    yume_en "....."

    voice "audio/voice/room0/cat_0_010.mp3"
    cat_th lick "เธอจำอะไรไม่ได้สักอย่างเลยสินะ" with dissolve
    cat_en lick "You can't remember anything, can you?" with dissolve

    yume_th "...อืม"
    yume_en "...Yeah."

    voice "audio/voice/room0/cat_0_011.mp3"
    cat_th normal "ไม่แปลกหรอก ถ้าหากเธอรู้ว่าตัวเองเป็นใคร เธอจะไม่มีวันเดินหลงในสถานที่แห่งนี้เป็นอันขาด" with dissolve
    cat_en normal " It's not surprising. If you knew who you were, you would never wander lost in this place." with dissolve

    yume_th "ที่นี่คือที่ไหน?"
    yume_en "Where is this place?"

    voice "audio/voice/room0/cat_0_012.mp3"
    cat_th bored "...."
    can_en bored "...."

    yume_th "แล้วฉันล่ะ...เป็นใคร...?"
    yume_en "And who am I...?"

    th "เจ้าแมวส้มจ้องหน้าเรา ดวงตาของมันมองเข้ามาในตาของเราราวกับมองทะลุไปถึงตัวตนข้างใน"
    en "The orange cat gazes at me."

    voice "audio/voice/room0/cat_0_013.mp3"
    cat_th lick "ถ้าเธออยากรู้คำตอบ เธอก็ต้องเปิดประตู"
    cat_en lick "Its eyes seem to penetrate into mine, seeing through to my inner self."

    yume_th "...."
    yume_en "...."

    voice "audio/voice/room0/cat_0_014.mp3"
    cat_th normal "เธอไม่มีทางเลือกหรอก"
    cat_en normal "You don't have a choice."

    th "เจ้าแมวส้มยืนยันเสียงแข็ง" 
    en "The orange cat asserts firmly, making it clear that there is no other path for me but this one."

    th "ดูเหมือนว่าเราจะไม่มีเส้นทางอื่นให้ไปนอกจากนี้ สุดท้าย เราก็เปิดประตูและเดินเข้าไปในห้อง"
    en "Finally, I open the door and step into the room."
    
    scene library_s_1080 with dissolve
    
    stop music
    play music 神隠しの真相
    yume_th "...นี่มัน...?"
    yume_en "...What is this...?"

    voice "audio/voice/room0/cat_0_015.mp3"
    cat_th lick "ปริศนาไงล่ะ"
    cat_en lick "It's a puzzle."

    yume_th "ปริศนา?"
    yume_en "A puzzle?"
    
    hide cat
    show puzzle0 with dissolve
    th "เราจ้องมองโจทย์ที่ถูกเขียนบนกระดานและพูดทวนคำเจ้าแมวส้มด้วยความไม่เข้าใจ"
    en "I stare at the problem written on the board and repeat the orange cat's words in confusion."

    th "เมื่อเจ้าแมวเห็นเราสงสัย มันจึงพูดขยายความขึ้น"
    en "Seeing my bewilderment, the cat elaborates."

    voice "audio/voice/room0/cat_0_016.mp3"
    cat_th normal "นี่ไม่ใช่ห้องๆเดียว เส้นทางต่อจากนี้ยังมีอีกหลายห้อง"
    cat_en normal "This is not the only room. There are many more rooms along this path."

    voice "audio/voice/room0/cat_0_017.mp3"
    cat_th ah "ทางเดียวที่เธอจะไปถึงความจริงได้คือเธอต้องตอบปริศนาที่อยู่ในแต่ละห้องให้ถูกต้อง"
    cat_en ah "The only way you can reach the truth is by solving the puzzles in each room."
    
    voice "audio/voice/room0/cat_0_018.mp3"
    cat_th normal "เมื่อตอบปริศนาประจำห้องถูกต้อง ประตูห้องต่อไปจะเปิดออก"
    cat_en normal "When you solve the puzzle of a room correctly, the door to the next room will open."
    
    voice "audio/voice/room0/cat_0_019.mp3" 
    cat_th lick "เมื่อถึงประตูบานสุดท้าย เธอจะเข้าใจความจริงทุกอย่างเอง"
    cat_en lick "Once you reach the final door, you will understand everything."


    th "เจ้าแมวส้มอธิบายสิ่งที่เราต้องเจอต่อจากนี้ไป"
    en "The orange cat explains what I will encounter next."

    th "สถานที่ที่แปลกประหลาดนี้มีบททดสอบที่ถูกสร้างขึ้นอย่างจงใจด้วยสาเหตุบางอย่าง"
    en "This strange place has tests deliberately created for some reason."

    th "ทำไมต้องเป็นปริศนา?"
    en "Why puzzles?"
    
    th "ทำไมกัน?"
    en "Why?"
    
    voice "audio/voice/room0/cat_0_020.mp3"
    cat_th normal "ปริศนาข้อแรกคือข้อที่ง่ายที่สุด ถ้าหากทำข้อนี้ไม่ได้ก็ไม่มีวันไปถึงข้อต่อไปได้"
    cat_en normal "The first puzzle is the easiest. If you can't solve this one, you'll never reach the next."

    th "เราพูดไม่ออก"
    en "I am speechless."
    
    th "สายตาของเจ้าแมวส้มคล้ายกับกำลังหยั่งเชิงเราไม่มีผิด"
    en "The cat's gaze seems to be testing me."
    
    yume_th "...ก็ได้"
    yume_en "...Alright."
    
    th "ในเมื่อเราไม่มีทางอื่นให้มุ่งหน้าไป ก็มีแต่ต้องตอบปริศนาให้ได้"
    en "Since I have no other path to take, I must solve the puzzle."
    
    th "ลองสักตั้งก็คงไม่เสียหาย"
    en "Trying won't hurt."
    jump answer_roome0



label answer_roome0:
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "memary":
                scene white with dissolve
                th "ทันใดที่เราเขียนคำตอบที่ถูกต้อง โลกรอบข้างก็ถูกสีขาวกลืนเข้าไป"
                en ""
                th "แสงสว่าง?"
                th "มันเกิดอะไรขึ้นกันแน่?"
                hide puzzle0
                stop music
                jump after_room_0
            if prepare(input_value) == "password" or prepare(input_value) == "pass" :
    ##voice "audio/voice/room0/cat_0_021.mp3"
                cat_th "ก็ Classic เกิ้น"
                jump answer_roome0
            if prepare(input_value) == "answer":
    ##voice "audio/voice/room0/cat_0_022.mp3"
                cat_th "มาถูกทางแล้ว"
                jump answer_roome0
            if prepare(input_value) == "yourgamepath" or prepare(input_value) == "/clue/room0" :
    ##voice "audio/voice/room0/cat_0_023.mp3"
                cat_th "ไปลองค้นหาดูสิ"
                jump answer_roome0
            
    ##voice "audio/voice/room0/cat_0_024.mp3"
            cat_th "ผิดจ้า"
            jump answer_roome0
        "ไม่รู้":
            if point_0 == 0 :
    ##voice "audio/voice/room0/cat_0_025.mp3"
                cat_th "ก็ลองคิดดูสิจ้ะ"
                $ point_0 = point_0 +1
                jump answer_roome0
            if point_0 == 1 :
    ##voice "audio/voice/room0/cat_0_026.mp3"
                cat_th "ทำไมถึงคิดว่าตอบแบบนี้จะแก้ปัญหาได้ล่ะ"
                $ point_0 = point_0 +1
                jump answer_roome0
            if point_0 == 2 :
    ##voice "audio/voice/room0/cat_0_027.mp3"
                cat_th "น่าจะต้องไปถามพ่อเธอดูล่ะจ้ะ"
                $ point_0 = point_0 +1
                jump answer_roome0  
            if point_0 == 3 :
    ##voice "audio/voice/room0/cat_0_028.mp3"
                cat_th "ยินดีด้วย คุณได้รับฉากจบลับ"
                $ point_0 = 0
                jump answer_roome0

    

label after_room_0:
    play music up_to_you
    scene fb1 with Dissolve(2)
    voice "audio/voice/room0/mary_0_000.mp3"
    mary0_th "ถ้าเราจะตั้งชื่อเกมทายปริศนา เราจะตั้งชื่อว่าอะไรดี?"
    mary0_en "If we were to name this puzzle game, what would we call it?"

    yume_th "ฉันสงสัยมากกว่าว่าทำไมเธอถึงชอบเกมปริศนาขนาดนั้น"
    yume_en "I'm more curious about why you like puzzles so much."

    voice "audio/voice/room0/mary_0_001.mp3"
    mary0_th "ไม่มีเหตุผลเป็นพิเศษหรอกจ้ะ"
    mary0_en "No special reason."

    yume_th  "เธอนี่แปลกคนจริงๆ"
    yume_en  "You're really a strange one."
    
    voice "audio/voice/room0/mary_0_002.mp3"
    mary0_th "เธอก็แปลกเหมือนกันจ้ะ ทั้งๆที่ไม่ชอบปริศนาแต่ก็ยังตอบคำถามฉันทุกครั้ง"
    mary0_en "You're strange too. Despite not liking puzzles, you still answer every question I ask."
    
    yume_th "ถ้าทิ้งให้เธอคิดคำถามคนเดียวแล้วฉันไม่ตอบ ฉันจะรู้สึกผิดน่ะสิ"
    yume_en "If I left you to think of questions alone and didn't answer, I would feel guilty."

    voice "audio/voice/room0/mary_0_003.mp3"
    mary0_th "ใจดีจริงๆเลยนะ ฮะๆๆ"
    mary0_en "That's very kind of you. Ha ha ha."

    yume_th "อึก...ไม่ได้มากมายอะไรขนาดนั้นหรอก..."
    yume_en "Uh... it's not that big of a deal..."

    voice "audio/voice/room0/mary_0_004.mp3"
    mary0_th "กลับมาที่สาระเดิมดีกว่าจ้ะ"
    mary0_en "Let's get back to the point."

    yume_th "ที่เราคุยกันนี่มีสาระจริงๆเหรอ?"
    yume_en "Our conversation has a point?"

    voice "audio/voice/room0/mary_0_005.mp3"
    mary0_th "โหดร้ายจริงๆนะ เธอไม่คิดว่าเรื่องไร้สาระก็มีความสนุกในรูปแบบของมันเหรอ?"
    mary0_en "That's harsh. Don't you think even silly things can be fun in their own way?"


    yume_th "ก็ได้ๆ...ให้คิดชื่อเกมปริศนาให้เธอใช่ไหม?"
    yume_en "Alright, alright... You want me to think of a name for your puzzle game, right?"

    voice "audio/voice/room0/mary_0_006.mp3"
    mary0_th "ใช่จ้ะ"
    mary0_en "Yes."
    
    yume_th "อืมม..."
    yume_en "Hmm..."
    
    voice "audio/voice/room0/mary_0_007.mp3"
    mary0_th "ว่าไงจ้ะ?"
    mary0_en "What do you think?"

    yume_th "งั้นเอาเป็นชื่อ..."
    yume_en "Then how about the name..."

    scene black with dissolve
    
    th "ภาพตรงหน้าจมลงสู่ความมืดในทันที"
    en "Suddenly, the scene in front of me plunges into darkness."
    
    th "เงาร่างอันลางเรือนที่ปรากฏตรงหน้าเราหายไปแล้ว"
    en "The faint silhouette that appeared before me disappears."
    
    th "เหลือทิ้งไว้เพียงคำบางอย่างที่ตกค้างในความทรงจำ"
    en "All that's left are some words lingering in my memory."

    jump memary_scene


label after_room_0_1:
    stop music 
    play music 泣カナイデ

    scene library_s_1080 with dissolve
    
    show cat normal
    yume_th  "...อึก"
    yume_en "...Uh."

    th "เราลืมตาตื่นขึ้นและพบตัวเองในห้องเดิม"
    en "I open my eyes and find myself back in the same room."
    
    yume_th "เมื่อกี้นี้...เกิดอะไรขึ้น...?"
    yume_en "What just happened...?"

    voice "audio/voice/room0/cat_0_029.mp3"
    cat_th normal "มันคือเศษเสี้ยวของความทรงจำ"
    cat_en normal "It was a fragment of your memory."

    yume_th  "ความทรงจำ?"
    yume_en "Memory?"


    voice "audio/voice/room0/cat_0_030.mp3"
    cat_th  smile "ทุกครั้งที่เธอตอบคำถามได้ เธอจะได้ความทรงจำของเธอกลับมาส่วนหนึ่ง"
    cat_en  smile "Every time you answer a question correctly, you regain a part of your memories."

    yume_th  "....."
    yume_en "....."

    voice "audio/voice/room0/cat_0_031.mp3"
    cat_th normal "เธออาจไม่เข้าใจว่าทำไมสถานที่แห่งนี้ถึงทำงานแบบนี้ แต่เมื่อเธอได้ความทรงจำกลับมาทั้งหมด เธอจะรู้ตัวตนที่แท้จริงของตัวเองและเหตุผลที่เธอมาที่นี่เอง"
    cat_en normal "You may not understand why this place works like this, but when you regain all your memories, you will understand your true identity and the reason you came here."    
    
    th "เจ้าแมวส้มจับจ้องเข้ามาในดวงตาเราตรงๆ"
    en "The orange cat stares directly into my eyes."

    th "สายตาเจนจัดของมันทำให้เรารู้สึกเหมือนจ้องหน้ามนุษย์ไม่มีผิด"
    en "Its intense gaze makes me feel like I'm looking into the eyes of a human."

    yume_th  "ถ้างั้นก็มีแต่ต้องตอบคำถามไปเรื่อยๆสินะ"
    yume_en "So, I just have to keep answering questions."

    voice "audio/voice/room0/cat_0_032.mp3"
    cat_th smile "ใช่แล้ว"
    cat_en smile "Exactly."

    th "เจ้าแมวส้มตอบรับเราพลางพยักหน้า เราที่ไม่มีทางเลือกอื่นจึงทำได้แต่เดิมตามเกมของมัน"
    en "The orange cat nods in agreement. With no other choice, I continue to follow its game."

    th "เมื่อเราจะเดินเข้าสู่ประตูบานต่อไป เรากลับพบกับวัตถุบางอย่างบนพื้นก่อน"
    en "As I approach the next door, I find something on the floor."

    show letter with Dissolve(1)
    voice "audio/voice/room0/cat_0_033.mp3"
    cat_th  lick "เก็บมันไปสิ"
    cat_en lick "Pick it up."

    yume_th  "จดหมาย?"
    yume_en "A letter?"

    voice "audio/voice/room0/cat_0_034.mp3"
    cat_th ah "มันคือรางวัลของผู้ชนะห้องแรก พกไปเถอะ มันไม่มีอันตรายอะไรหรอก"
    cat_en ah "It's the prize for the winner of the first room. Carry it with you. It's harmless."

    th "เจ้าแมวส้มยืนยัน เราจึงถือจดหมายไว้"
    en "The orange cat assures me, so I take the letter."

    th "ไม่นานหลังจากนั้น เราก็พบตัวเองอยู่ตรงหน้าประตูบานต่อไป"
    en "Soon after, I find myself in front of numerous doors."
    hide letter
    voice "audio/voice/room0/cat_0_035.mp3"
    cat_th  smile  "....."
    cat_en  smile  "....."

    th "ถึงแม้จะยังไม่เข้าใจอะไร แต่เมื่อเราได้เห็นภาพอันลางเรือนหลังตอบคำถามแล้ว ความรู้สึกถวิลหาก็ปรากฏขึ้นในใจของเรา"
    en "Even though I still don't understand everything, after seeing that fleeting image following the question, a sense of yearning emerges in my heart."

    th "คนที่คุยกับเราในภาพความทรงจำนั้นคือใคร?"
    en "Who was the person I was talking to in that memory?"

    th "...ความรู้สึกอันรุนแรงเพรียกร้องให้เราเดินต่อไปข้างหน้า..."
    en "An intense feeling urges me to keep moving forward."
    
    th "รู้ตัวอีกที เราก็เปิดประตูบานต่อไปแล้ว"
    en "Before I know it, I have opened one of those doors."

    scene hall_n_1080 with dissolve
    th "ห้องที่อยู่ต่อหน้าสายตาของฉันเป็นห้องที่กว้างขวาง มีประตูจำนวนมากขนาบอยู่ด้านข้าง"
    show cat normal with dissolve
    voice "audio/voice/room0/cat_0_036.mp3"
    cat_th normal "ยินดีต้อนรับสู่ห้องโถงของคฤหาสน์แห่งนี้ นี่จะเป็นห้องที่เชื่อมต่อกับห้องอื่นๆมากมายในคฤหาสน์"
    voice "audio/voice/room0/cat_0_037.mp3"
    cat_th lick "เธอสามารถเปิดประตูบานไหนก็ได้ เพื่อเข้าสู่ห้องต่อไป"
    hide cat with dissolve
    th "ฉันเดินไปหาประตูที่ใกล้ที่สุดด้านขวามือ"
    #sfx คลิ๊ก
    yume_th "ไม่เห็นเปิดออกเลย"
    
    show cat lick with dissolve
    voice "audio/voice/room0/cat_0_038.mp3"
    cat_th lick "ไม่ได้บอกนี่ว่ามันไม่ได้ล็อก"
    th "ซักวันนึง แมวตัวนี้ต้องถูกนำไปโกนขน ฉันสาบานตัวเองไว้เช่นนั้น"
    voice "audio/voice/room0/cat_0_039.mp3"
    cat_th smile "ไม่ต้องมองด้วยสายตาอาฆาตขนาดนั้นก็ได้ เธอลองมองที่แผนผังอันนี้สิ"
    hide cat
    #show minimap
    th "..."
    voice "audio/voice/room0/cat_0_040.mp3"
    cat_th ah "ขอแค่มีแผนผังนี่ เธอก็สามารถรู้ได้แล้วว่า ห้องไหนที่เข้าได้หรือไม่ได้ \nแล้วมันยังบอกด้วยว่าห้องไหนที่เราเคยผ่านมาแล้ว"
    th "ถ้างั้น ฉันจะเริ่มที่ห้องไหนดี?"
    jump main_map
