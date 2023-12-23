
label room09:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 不穏

    if room09_is_pass == False: 
        show cat normal with dissolve
        yume_th  "เป็นโจทย์ที่แปลกจริงๆ"
        yume_en "This is a really strange puzzle."
        voice "audio/voice/room9/cat_9_000.mp3"
        cat_th normal "ข้อท้ายๆก็ต้องยากหน่อยล่ะจ้ะ"
        cat_en normal "The last ones are supposed to be challenging."
        th "คำพูดของเจ้าแมวส้มทำให้เราประหลาดใจเล็กน้อย"
        en "The words of the orange cat slightly surprised me."
        yume_th  "นี่เรามาไกลแล้วสินะ"
        yume_en "We've come a long way, haven't we?"
        voice "audio/voice/room9/cat_9_001.mp3"
        cat_th lick  "ตามหลักก็ใช่จ้ะ"
        cat_en lick "Technically, yes." 
        yume_th  "ดูตอบกำกวมนะ"
        yume_en "That's a vague answer."
        th "เจ้าแมวส้มเงียบลงสักพัก ไม่นานหลังจากนั้นมันก็มองสบตาเราตรงๆ"
        en "The orange cat fell silent for a moment, then looked directly into my eyes."
        voice "audio/voice/room9/cat_9_002.mp3"
        cat_th smile "ฉันหวังว่าเธอจะทนรับทุกอย่างได้เมื่อตัวตนของเธอกลับมา"
        cat_en smile "I hope you can handle everything when your true self returns."
        yume_th  "....."
        yume_en "....."
        voice "audio/voice/room9/cat_9_003.mp3"
        cat_th normal  "ฉันเชื่อว่าเธอมีพลังมากพอที่จะออกไปจากสถานที่แห่งนี้ได้นะ"
        cat_en normal "I believe you have the strength to leave this place."
        th "เจ้าแมวส้มมองเราด้วยสายตาคาดหวัง"
        en "The orange cat gazed at me with expectation."
        yume_th  "ฉันก็อยากจะเชื่อแบบนั้นเหมือนกัน"
        yume_en "I want to believe that too."
        th "เจ้าแมวส้มหุบปากเงียบลงอีกครั้ง"
        en "The orange cat closed its mouth again and fell silent."
        th "นี่เราคิดไปเองหรือเปล่านะว่ามันกำลังแอบส่งยิ้มให้เรา"
        en "I wonder if it was secretly smiling at me."

        show puzzle9
        jump answer_roome09
    
    else :
        th "this room has nothing"
        jump main_map 

label answer_roome09:

    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "cafeaulait":
                $ room09_is_pass = True
                play sound "audio/sfx/correct-6033.mp3" volume 1
                th "ภาพอดีตถูกฉายขึ้นอีกครั้ง"
                en "The past was projected once more."
                th "ต่อจากนี้จะมีความจริงแบบไหนรอเราอยู่กันนะ?"
                en "What kind of truth awaits us next?"
                hide puzzle9
                jump after_room_9
            else :
                th "Wrong!"
                jump answer_roome09
        "return":
            hide puzzle9
            jump main_map

label after_room_9:
    scene fb2_3 with dissolve
    stop music
    play music up_to_you

    voice "audio/voice/room9/mary_9_000.mp3"
    mary0_th  "เธอชอบดื่มกาแฟเหรอ?"
    mary0_en "Do you like coffee?"
    yume_th   "Cafe au lait มันก็อร่อยดีนะ"
    yume_en "Café au lait is quite nice."
    th "เราตอบคำถามของคู่สนทนาเรียบๆก่อนจะจิบกาแฟหนึ่งอึก"
    en "I replied nonchalantly and took a sip of my coffee."
    voice "audio/voice/room9/mary_9_001.mp3"
    mary0_th  "เลี้ยงกาแฟฉันหน่อยสิ"
    mary0_en "Treat me to a coffee?"
    yume_th  "หา?"
    yume_en "Huh?"
    voice "audio/voice/room9/mary_9_002.mp3"
    mary0_th  "นะๆๆๆ"
    mary0_en "Please?"
    th "คู่สนทนาของเราส่งสายตาอ้อนวอน" 
    en "She gave me a pleading look."
    th "ถึงเราจะอยากตอบรับเธอแต่เราก็ทำไม่ได้อยู่ดี"
    en "Despite wanting to say yes, I hesitated."
    yume_th  "ฉันไม่ได้มีเงินขนาดนั้นนะ อีกอย่างเธอรวยกว่าฉันไม่ใช่หรือไง?"
    yume_en "I don’t have that much money. Besides, aren’t you richer than me?"
    voice "audio/voice/room9/mary_9_003.mp3"
    mary0_th  "ของแบบนี้มันไม่ได้อยู่ที่ราคา แต่อยู่ที่ใจจ้ะ"
    mary0_en "It’s not about the price, it's about the sentiment."
    yume_th  "พูดก็พูดไป กาแฟมันก็ต้องใช้เงินจ่ายอยู่ดีแหละ"
    yume_en "Easy for you to say. Coffee still costs money."
    voice "audio/voice/room9/mary_9_004.mp3"
    mary0_th  "เธอนี่ไม่มีอารมณ์ขันเลยนะจ้ะ"
    mary0_en "You really have no sense of humor."
    th "คนพูดส่งเสียงหัวเราะกังวานใสในลำคอเบาๆ"
    en "She laughed softly."
    yume_th  "นั่นเธอจะทำอะไรน่ะ?"
    yume_en "What are you doing?"
    voice "audio/voice/room9/mary_9_005.mp3"
    mary0_th  "ดื่มจากแก้วเธอไง"
    mary0_en "I’m going to drink from your cup."
    yume_th  "....."
    yume_en "....."
    th "เราเงียบเพราะนึกว่าเธอล้อเล่น" 
    en "I was silent, thinking she was joking."
    th "แต่เมื่อเห็นอีกฝ่ายจับแก้วเรายกขึ้น เราก็ยื่นมือกดแขนเธอลงตามปฏิกิริยา"
    en "But when she reached for my cup, I instinctively pressed her arm down."
    voice "audio/voice/room9/mary_9_006.mp3"
    mary0_th  "ทำไมอ่ะ?"
    mary0_en "Why?"
    yume_th  "ฉันต่างหากที่อยากถามเธอว่าทำไม"
    yume_en "I should be asking you that."
    voice "audio/voice/room9/mary_9_007.mp3"
    mary0_th  "แหม...เราก็สนิทกันจะตาย...แค่ดื่มจากแก้วเดียวกันไม่ตายหรอก..."
    mary0_en "Come on... we’re close... sharing a drink won’t kill us..."
    th "คู่สนทนาเราพยายามยกแก้วขึ้นอีกครั้ง เราตอบสนองเธอด้วยการกดแขนเธอลง"
    en "She tried to lift the cup again, but I kept her arm down."
    voice "audio/voice/room9/mary_9_008.mp3"
    mary0_th  "อย่าใจร้ายสิ"
    mary0_en "Don't be so mean."
    yume_th  "....."
    yume_en "....."
    voice "audio/voice/room9/mary_9_009.mp3"
    mary0_th  "นิดหน่อยๆน่า"
    mary0_en "Just a little bit."
    th "เราในตอนนั้นสะดุ้งเฮือกให้กับรอยยิ้มเจ้าเล่ห์ของคู่สนทนา"
    en "I jumped at her mischievous smile."
    th "อุณหภูมิของใบหน้าเราสูงขึ้นอย่างควบคุมไม่ได้"
    en "The heat rose to my face uncontrollably."
    yume_th  "มันน่าอายจะตาย"
    yume_en "It’s embarrassing."
    voice "audio/voice/room9/mary_9_010.mp3"
    mary0_th  "เหรอ?"
    mary0_en "Really?"
    yume_th  "อย่ามาเหรอสิ"
    yume_en "Don’t 'really' me."
    voice "audio/voice/room9/mary_9_011.mp3"
    mary0_th  "หืม?"
    mary0_en "Hmm?"
    yume_th  "ถ้าเธอดื่มจากแก้วฉัน มันก็เป็นจูบทางอ้อมพอดีสิ"
    yume_en "If you drink from my cup, it’s like an indirect kiss."
    voice "audio/voice/room9/mary_9_012.mp3"
    mary0_th  "แค่นั้นก็อายเหรอ?"
    mary0_en "You're embarrassed over that?"
    yume_th  "อายสิ"
    yume_en "Yes, I am."
    voice "audio/voice/room9/mary_9_013.mp3"
    mary0_th  "ฮิๆ"
    mary0_en "Hehe."
    yume_th  "...!!"
    yume_en "...!!"

    # Cut Scene
    stop music
    play music 神隠しの真相

    th "เรายังพูดไม่ทันจบ ริมฝีปากก็ถูกหยุดลงก่อน"
    en "Before I could finish speaking, my words were halted."
    th "กลิ่นอันหอมหวนและปอยผมสีทองยาวสลวยของคนตรงหน้าปลิวไสวไล้เลียใบหน้าของเรา"
    en "The sweet fragrance and the long, golden hair of the person in front of me brushed against my face."
    th "สัมผัสนุ่มนวลและอบอุ่นปรากฏขึ้นบนริมฝีปากของเรา ก่อนที่การเชื่อมต่อระหว่างเราสองคนจะถูกคลี่คลายลงเมื่อคนตรงหน้าเลื่อนใบหน้าห่างออกไป"
    en "A soft and warm touch appeared on my lips before the connection between us was gently broken as she pulled her face a"
    th "ใบหน้าของเธอแดงระเรื่อน้อยๆ"
    en "Her face was slightly flushed."
    th "แน่นอนว่าตอนนี้ใบหน้าของเราก็แดงไม่แพ้เธอ"
    en "My face was undoubtedly as red as hers."

    yume_th  "เมื่อกี้นี้มัน..."
    yume_en "What just happened..."
    voice "audio/voice/room9/mary_9_014.mp3"
    mary0_th  "ฉันจะไม่โกหกความรู้สึกของฉันจ้ะ"
    mary0_en "I won't lie about my feelings."
    yume_th  "....."
    yume_en "....."
    voice "audio/voice/room9/mary_9_015.mp3"
    mary0_th "ฉันน่ะ..."
    mary0_en "The truth is..."
    
    th "ฉันน่ะ...ชอบเธอที่สุดเลย..."
    en "'I... like you the most...'"
    scene library_s_1080 with dissolve


    yume_th "...!!"
    yume_en "...!!"
    th "ความทรงจำที่กลับมาทำให้เรารู้สึกถึงแรงกระตุ้น"
    en "The returning memories ignited a surge within me."
    th "เราไม่ควรจะมีร่างกายแต่ทำไมรู้สึกเหมือนทั้งร่างร้อนวูบวาบไปหมด"
    en "Although I shouldn't have a body, why do I feel a burning sensation throughout?"
    th "ทั้งๆที่ไม่ควรจะมีดวงตา แต่กลับรู้สึกเหมือนมีสายธารแห่งความเศร้าไหลออกมา"
    en "Despite supposedly lacking eyes, it felt like a stream of sorrow was flowing out."
    th "นี่มัน...อะไรกัน...?"
    en "What is this...?"
    voice "audio/voice/room9/cat_9_004.mp3"
    cat_th normal "ดีใจด้วยนะที่มาถึงตรงนี้ได้"
    cat_en normal "Congratulations on making it this far."
    yume_th "หา?"
    yume_en "Huh?"
    voice "audio/voice/room9/cat_9_005.mp3"
    cat_th smile "เธออาจจะนึกว่าเธอไม่มีตัวตน แต่จริงๆแล้วเธอทำเป็นมองไม่เห็นมันหรือเปล่า?"
    cat_en smile "You might think you don't exist, but have you just been pretending not to see yourself?"
    yume_th "หมายความว่า..."
    yume_en  "Do you mean..."
    voice "audio/voice/room9/cat_9_006.mp3"
    cat_th normal "เธอไม่ได้หายไปไหนหรอก เธอยังอยู่ที่นี่ ตรงนี้"
    cat_en normal "You haven't disappeared. You are still here, right here."
    yume_th "....."
    yume_en "....."
    voice "audio/voice/room9/cat_9_007.mp3"
    cat_th ah "เพียงแต่เธอไม่อยากยอมรับว่าตัวเธอมีอยู่ เธอเลยทำเป็นมองข้ามความจริงทั้งหมดไป"
    cat_en ah "You just didn't want to accept your existence, so you overlooked all the truth."
    yume_th "นั่นมัน..."
    yume_en "That is..."
    voice "audio/voice/room9/cat_9_008.mp3"
    cat_th normal "หมดเวลาโกหกตัวเองแล้ว...ยูเมะ..."
    cat_en normal "It's time to stop lying to yourself... Yume..."

    scene white with dissolve
    th "จบคำพูดของเจ้าแมว ประตูบานหนึ่งก็ถูกเปิดออก"
    en "With the cat's words, a door opened on its own."
    th "ทั้งๆที่ไม่มีใครแตะต้องประตู แต่มันเปิดง้างออกมาราวกับมีเจตจำนงของมันเอง"
    en "Though no one touched it, it swung open as if with its own will."
    th "สิ่งที่อยู่ข้างหลังบานประตูคือแสงสว่าง"
    en "Behind the door was a bright light."
    th "ไม่ช้าหลังจากนั้น แสงสีขาวก็ขยายตัวกว้างขึ้นและกลืนกินร่างของเราเข้าไป"
    en "Soon after, the expanding white light engulfed and enveloped me."


    jump final



