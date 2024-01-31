
label room08:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music midnight

    if room08_is_pass == False: 
        play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
        show cat normal with dissolve
        yume_th "นี่คืออะไรกัน?"
        yume_en "What is this?"
        voice "audio/voice/room8/cat_8_000.mp3"
        cat_th normal "ถ้าบอกก็ง่ายเกินไปสิ"
        cat_en normal "It would be too easy if I told you."
        yume_th "....."
        yume_en "....."
        voice "audio/voice/room8/cat_8_001.mp3"
        cat_th smile "ไขปริศนาให้ได้ แล้วจะเข้าใจอะไรมากขึ้นเอง"
        cat_en smile "Solve the puzzle, and you'll understand more."
        th "เจ้าแมวส้มพูดราวกับท้าทาย"
        en "The orange cat spoke as if issuing a challenge."
        th "ดวงตาเจนจัดของมันทำให้เรารู้สึกเหมือนโดนมองทะลุอีกครั้ง"
        en "Its intense gaze made me feel like I was being seen through once again."

        show puzzle8
        jump answer_room8
    
    else :
        "this room has nothing"
        jump main_map 

label answer_room8:

    menu:
        "{size=*1.5}/clue/Poppy{/size}"
        "Answer":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "series":
                $ room08_is_pass = True
                play sound "audio/sfx/correct-6033.mp3" volume 1
                th "ภาพอดีตถูกฉายขึ้นอีกครั้ง"
                en "The past was projected once more."
                th "ต่อจากนี้จะมีความจริงแบบไหนรอเราอยู่กันนะ?"
                en "What kind of truth awaits us next?"
                hide puzzle8
                jump after_room_8
            else :
                th "it's not answer"
                en "Wrong!"
                jump answer_room8

        "Hint":
            th "1.2 The world divides into facts -> T\n1.21 Any one can either be the case or not be the case, and everything
else remain the same. -> A"
            en "1.2 The world divides into facts -> T\n1.21 Any one can either be the case or not be the case, and everything
else remain the same. -> A"
            jump answer_room8

            

        "Skip Answer":
            hide puzzle8
            $ room08_is_pass = True
            jump after_room_8
        "Return to Hall":
            hide puzzle8
            jump main_map

label after_room_8:
    scene fb2 with dissolve
    stop music
    play music lost


    voice "audio/voice/room8/mary_8_000.mp3"
    mary0_th "อ่านหนังสือเข้าใจยากแบบนั้นอีกแล้วเหรอ?"
    mary0_en "Struggling with that difficult book again?"
    yume_th "หนังสือปรัชญาธรรมดาเองน่า"
    yume_en "It's just ordinary philosophy."
    voice "audio/voice/room8/mary_8_001.mp3"
    mary0_th "ปริศนาของฉันยังน่าสนใจกว่าเลยนะ"
    mary0_en "My puzzles are more interesting than that."
    yume_th "ฉันว่าไม่นะ"
    yume_en "I don't think so."
    voice "audio/voice/room8/mary_8_002.mp3"
    mary0_th "อย่ากล่าวหาแบบนี้สิ"
    mary0_en "Don’t accuse me like that."
    th "คู่สนทนาของเราทำแก้มป่องน้อยๆด้วยความงอน"
    en "Our companion pouted slightly, showing a hint of annoyance."
    yume_th "เวลาชีวิตมีอะไรน่าปวดหัว อ่านของเข้าใจยากแบบนี้มันทำให้รู้สึกดีแปลกๆน่ะ"
    yume_en "When life gets complicated, reading something challenging like this feels strangely good."
    voice "audio/voice/room8/mary_8_003.mp3"
    mary0_th "อ่านแล้วเข้าใจหรือเปล่าน่ะ?"
    mary0_en "Do you understand what you read?"
    yume_th "เข้าใจบ้าง ไม่เข้าใจบ้าง"
    yume_en "Some of it, not all."
    #voice "audio/voice/room8/mary_8_004.mp3"
    mary0_th "....."
    mary0_en "....."
    yume_th "อย่าทำสายตาไม่เชื่อฉันแบบนั้นสิ"
    yume_en "Don’t look at me like you don’t believe me."
    voice "audio/voice/room8/mary_8_005.mp3"
    mary0_th "เธอคิดไปเองจ้ะ"
    mary0_en "You’re imagining things."
    yume_th "ไม่รู้ๆๆๆ อ่านต่อแล้ว"
    yume_en "I don’t know... let me keep reading."
    voice "audio/voice/room8/mary_8_006.mp3"
    mary0_th "ขีดจำกัดภาษาของฉันคือขีดจำกัดโลกของฉัน"
    mary0_en "The limits of my language mean the limits of my world."
    th "คำพูดของคู่สนทนาทำให้เราเบิกตากว้างด้วยความแปลกใจ"
    en "I was surprised by her statement."
    voice "audio/voice/room8/mary_8_007.mp3"
    mary0_th "ถ้าจำไม่ผิด มันน่าจะมีคำพูดแบบนี้ในหนังสือนั้น"
    mary0_en "If I remember correctly, that's a line from that book."
    yume_th "เธอเคยอ่านหนังสือของฉันด้วยเหรอ?"
    yume_en "You've read my book?"
    voice "audio/voice/room8/mary_8_008.mp3"
    mary0_th "ไม่เคยหรอก แค่เคยได้ยินคนอ้างอิงบ่อยๆเพราะมันเท่ดีน่ะ"
    mary0_en "Never. I've just heard people refer to it often because it sounds cool."
    yume_th "ถึงตอนนี้ฉันยังไม่เข้าใจเลยว่าประโยคนั้นหมายถึงอะไร"
    yume_en "I still don’t understand what that sentence means."
    voice "audio/voice/room8/mary_8_009.mp3"
    mary0_th "เรื่องบางเรื่องไม่เข้าใจแล้วอาจจะเท่กว่าก็ได้นะ"
    mary0_en "Some things might be cooler when you don't understand them."
    th "คู่สนทนาของเราส่งเสียงหัวเราะเบาๆ"
    en "She chuckled softly."
    th "เราเข้าใจว่าเธอพยายามพูดให้เราอารมณ์ดี แต่เราในตอนนี้ไม่มีทางหรอกที่จะรู้สึกดีขึ้นได้"
    en "I knew she was trying to cheer me up, but I couldn’t feel better at the moment."
    yume_th "เธอรู้ไหมว่าพ่อของฉันชอบอ่านหนังสือเล่มนี้"
    yume_en "Did you know my dad liked this book?"
    #voice "audio/voice/room8/mary_8_010.mp3"
    mary0_th "....."
    mary0_en "....."
    yume_th "สมัยที่เขาสนิทกับฉันและยังคุยกับคนอื่นรู้เรื่องนะ ฮะๆๆ"
    yume_en "Back when he was close to me and still made sense to others. Ha ha..."
    #voice "audio/voice/room8/mary_8_011.mp3"
    mary0_th "....."
    mary0_en "....."
    th "เราหัวเราะแห้งๆให้กับอดีต แต่คู่สนทนาของเราเงียบลงเพราะเธอมองออก"
    en "I laughed dryly at the past, but she fell silent, understanding the pain."
    th "ทุกครั้งที่เราพูดเรื่องครอบครัวมักเต็มไปด้วยความถวิลหาอดีตและความเศร้าเสมอ"
    en "Every time I talked about my family, it was always filled with nostalgia and sadness."
    yume_th "ช่างมันเถอะ เวลาเปลี่ยนคนก็เปลี่ยน ตอนนี้พ่อของฉันก็เป็นแค่พวกไม่ได้เรื่อง"
    yume_en "Forget it. People change over time. Now my dad is just a mess."
    #voice "audio/voice/room8/mary_8_012.mp3"
    mary0_th "....."
    mary0_en "....."
    yume_th "แล้วบ้านของเธอเป็นยังไงบ้างล่ะ?"
    yume_en "What about your family?"
    #voice "audio/voice/room8/mary_8_013.mp3"
    mary0_th "....."
    mary0_en "....."
    th "คู่สนทนาของเราอ้ำอึ้งเหมือนไม่กล้าตอบคำถาม"
    en "She hesitated as if afraid to answer."
    yume_th "ฉันคงละลาบละล้วงเกินไปสินะ"
    yume_en "I might be prying too much."
    voice "audio/voice/room8/mary_8_014.mp3"
    mary0_th "ไม่หรอกจ้ะ"
    mary0_en "Not at all."
    yume_th "....."
    yume_en "....."
    voice "audio/voice/room8/mary_8_015.mp3"
    mary0_th "อย่างที่เธอรู้ บ้านของฉันอาจจะไม่ได้ถึงขนาดเธอ แต่มันก็ไม่ได้น่าอยู่มากหรอก"
    mary0_en "As you know, my home might not be as bad as yours, but it's not pleasant either."
    yume_th "นั่นสินะ"
    yume_en "I see."
    voice "audio/voice/room8/mary_8_016.mp3"
    mary0_th "แต่ว่า..."
    mary0_en "But..."
    th "สัมผัสอบอุ่นปรากฏขึ้นที่หลังมือเรา"
    en "A warm touch appeared on the back of my hand."
    th "มือของคู่สนทนาวางบนมือเราอย่างแผ่วเบา"
    en "Her hand gently rested on mine."
    voice "audio/voice/room8/mary_8_017.mp3"
    mary0_th "ไม่เป็นไรหรอก ก็มีฉันมีเธอแล้วนี่นา"
    mary0_en "It's okay. We have each other, right?"
    yume_th "งั้นเหรอ"
    yume_en "Is that so?"
    th "เราได้แต่ยิ้มเศร้าๆเท่านั้น"
    en "I could only offer a sad smile."
    th"คู่สนทนาของเราก็เช่นกัน"
    en "She did the same."

    scene library_s_1080 with dissolve
    stop music
    play music midnight

    yume_th "....."
    yume_en "....."
    th "ทั้งๆที่ภาพที่เห็นเป็นแค่ความทรงจำ แต่สัมผัสอบอุ่นที่เกิดขึ้นยังตกต้างอยู่"
    en "Even though these visions are just memories, the warmth I felt was lingering."
    th "เหตุการณ์ทั้งหมดนั้นเคยเกิดขึ้นจริง ไม่งั้นมันคงไม่สร้างความรู้สึกรุนแรงในตัวเรา"
    en "These events must have really happened; otherwise, they wouldn't evoke such intense emotions in me."
    th "...นี่คือความโหยหา...หรือเปล่านะ...?"
    en "...Is this a longing... perhaps...?"
    show cat normal with dissolve
    voice "audio/voice/room8/cat_8_002.mp3"
    cat_th normal "พอจะนึกอะไรออกหรือยังล่ะ?"
    cat_en normal "Have you figured out anything yet?"
    yume_th "....."
    yume_en "....."
    th "เราไม่ได้ตอบเจ้าแมวส้ม"
    en "I didn’t respond to the orange cat."
    th "ความหนักหน่วงในอกทำให้เราไม่กล้าเอ่ยคำแม้แต่คำเดียว"
    en "The heaviness in my chest prevented me from uttering even a single word."
    voice "audio/voice/room8/cat_8_003.mp3"
    cat_th normal "ไม่ต้องคิดมากหรอก"
    cat_en normal "Don't overthink it."
    yume_th "....."
    yume_en "....."
    voice "audio/voice/room8/cat_8_004.mp3"
    cat_th smile "คำตอบอยู่อีกไม่ไกลแล้ว"
    cat_en normal "The answer isn't far away now."
    play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
    th "เจ้าแมวส้มเดินนำหน้าเรา เราจึงเดินตามมัน"
    en "The orange cat walked ahead, and I followed."
    hide cat
    jump cutscene_main



