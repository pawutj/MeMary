
label room08:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music midnight

    if room08_is_pass == False: 
        show cat normal with dissolve
        yume_th "นี่คืออะไรกัน?"
    ##voice "audio/voice/room8/cat_8_000.mp3"
        cat_th normal "ถ้าบอกก็ง่ายเกินไปสิ"
        yume_th "....."
    ##voice "audio/voice/room8/cat_8_001.mp3"
        cat_th smile "ไขปริศนาให้ได้ แล้วจะเข้าใจอะไรมากขึ้นเอง"
        th"เจ้าแมวส้มพูดราวกับท้าทาย"
        th "ดวงตาเจนจัดของมันทำให้เรารู้สึกเหมือนโดนมองทะลุอีกครั้ง"

        show puzzle8
        jump answer_roome08
    
    else :
        "this room has nothing"
        jump main_map 

label answer_roome08:

    menu:
        "answer":
            "ตอบคำถาม"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "russell":
                $ room08_is_pass = True
                th "ภาพอดีตถูกฉายขึ้นอีกครั้ง"
                th "ต่อจากนี้จะมีความจริงแบบไหนรอเราอยู่กันนะ?"
                hide puzzle8
                jump after_room_8
            else :
                th "it's not answer"
                jump answer_roome08
        "return":
            hide puzzle8
            jump main_map

label after_room_8:
    scene fb2_5 with dissolve
    stop music
    play music lost


    ##voice "audio/voice/room8/mary_8_000.mp3"
    mary0_th "อ่านหนังสือเข้าใจยากแบบนั้นอีกแล้วเหรอ?"
    yume_th "หนังสือปรัชญาธรรมดาเองน่า"
    ##voice "audio/voice/room8/mary_8_001.mp3"
    mary0_th "ปริศนาของฉันยังน่าสนใจกว่าเลยนะ"
    yume_th "ฉันว่าไม่นะ"
    ##voice "audio/voice/room8/mary_8_002.mp3"
    mary0_th "อย่ากล่าวหาแบบนี้สิ"
    th "คู่สนทนาของเราทำแก้มป่องน้อยๆด้วยความงอน"
    yume_th "เวลาชีวิตมีอะไรน่าปวดหัว อ่านของเข้าใจยากแบบนี้มันทำให้รู้สึกดีแปลกๆน่ะ"
    ##voice "audio/voice/room8/mary_8_003.mp3"
    mary0_th "อ่านแล้วเข้าใจหรือเปล่าน่ะ?"
    yume_th "เข้าใจบ้าง ไม่เข้าใจบ้าง"
    ##voice "audio/voice/room8/mary_8_004.mp3"
    mary0_th "....."
    yume_th "อย่าทำสายตาไม่เชื่อฉันแบบนั้นสิ"
    ##voice "audio/voice/room8/mary_8_005.mp3"
    mary0_th "เธอคิดไปเองจ้ะ"
    yume_th "ไม่รู้ๆๆๆ อ่านต่อแล้ว"
    ##voice "audio/voice/room8/mary_8_006.mp3"
    mary0_th "ขีดจำกัดภาษาของฉันคือขีดจำกัดโลกของฉัน"
    th "คำพูดของคู่สนทนาทำให้เราเบิกตากว้างด้วยความแปลกใจ"
    ##voice "audio/voice/room8/mary_8_007.mp3"
    mary0_th "ถ้าจำไม่ผิด มันน่าจะมีคำพูดแบบนี้ในหนังสือนั้น"
    yume_th "เธอเคยอ่านหนังสือของฉันด้วยเหรอ?"
    ##voice "audio/voice/room8/mary_8_008.mp3"
    mary0_th "ไม่เคยหรอก แค่เคยได้ยินคนอ้างอิงบ่อยๆเพราะมันเท่ดีน่ะ"
    yume_th "ถึงตอนนี้ฉันยังไม่เข้าใจเลยว่าประโยคนั้นหมายถึงอะไร"
    ##voice "audio/voice/room8/mary_8_009.mp3"
    mary0_th "เรื่องบางเรื่องไม่เข้าใจแล้วอาจจะเท่กว่าก็ได้นะ"
    th "คู่สนทนาของเราส่งเสียงหัวเราะเบาๆ"
    th "เราเข้าใจว่าเธอพยายามพูดให้เราอารมณ์ดี แต่เราในตอนนี้ไม่มีทางหรอกที่จะรู้สึกดีขึ้นได้"
    yume_th "เธอรู้ไหมว่าพ่อของฉันชอบอ่านหนังสือเล่มนี้"
    ##voice "audio/voice/room8/mary_8_010.mp3"
    mary0_th "....."
    yume_th "สมัยที่เขาสนิทกับฉันและยังคุยกับคนอื่นรู้เรื่องนะ ฮะๆๆ"
    ##voice "audio/voice/room8/mary_8_011.mp3"
    mary0_th "....."
    th "เราหัวเราะแห้งๆให้กับอดีต แต่คู่สนทนาของเราเงียบลงเพราะเธอมองออก"
    th "ทุกครั้งที่เราพูดเรื่องครอบครัวมักเต็มไปด้วยความถวิลหาอดีตและความเศร้าเสมอ"
    yume_th "ช่างมันเถอะ เวลาเปลี่ยนคนก็เปลี่ยน ตอนนี้พ่อของฉันก็เป็นแค่พวกไม่ได้เรื่อง"
    ##voice "audio/voice/room8/mary_8_012.mp3"
    mary0_th "....."
    yume_th "แล้วบ้านของเธอเป็นยังไงบ้างล่ะ?"
    ##voice "audio/voice/room8/mary_8_013.mp3"
    mary0_th "....."
    th "คู่สนทนาของเราอ้ำอึ้งเหมือนไม่กล้าตอบคำถาม"
    yume_th "ฉันคงละลาบละล้วงเกินไปสินะ"
    ##voice "audio/voice/room8/mary_8_014.mp3"
    mary0_th "ไม่หรอกจ้ะ"
    yume_th "....."
    ##voice "audio/voice/room8/mary_8_015.mp3"
    mary0_th "อย่างที่เธอรู้ บ้านของฉันอาจจะไม่ได้ถึงขนาดเธอ แต่มันก็ไม่ได้น่าอยู่มากหรอก"
    yume_th "นั่นสินะ"
    ##voice "audio/voice/room8/mary_8_016.mp3"
    mary0_th "แต่ว่า..."
    th "สัมผัสอบอุ่นปรากฏขึ้นที่หลังมือเรา"
    th "มือของคู่สนทนาวางบนมือเราอย่างแผ่วเบา"
    ##voice "audio/voice/room8/mary_8_017.mp3"
    mary0_th "ไม่เป็นไรหรอก ก็มีฉันมีเธอแล้วนี่นา"
    yume_th "งั้นเหรอ"
    th "เราได้แต่ยิ้มเศร้าๆเท่านั้น"
    th"คู่สนทนาของเราก็เช่นกัน"

    scene library_s_1080 with dissolve
    stop music
    play music midnight

    yume_th "....."
    th "ทั้งๆที่ภาพที่เห็นเป็นแค่ความทรงจำ แต่สัมผัสอบอุ่นที่เกิดขึ้นยังตกต้างอยู่"
    th "เหตุการณ์ทั้งหมดนั้นเคยเกิดขึ้นจริง ไม่งั้นมันคงไม่สร้างความรู้สึกรุนแรงในตัวเรา"
    th "...นี่คือความโหยหา...หรือเปล่านะ...?"
    show cat normal with dissolve
    ##voice "audio/voice/room8/cat_8_002.mp3"
    cat_th normal "พอจะนึกอะไรออกหรือยังล่ะ?"
    yume_th "....."
    th "เราไม่ได้ตอบเจ้าแมวส้ม"
    th "ความหนักหน่วงในอกทำให้เราไม่กล้าเอ่ยคำแม้แต่คำเดียว"
    ##voice "audio/voice/room8/cat_8_003.mp3"
    cat_th normal "ไม่ต้องคิดมากหรอก"
    yume_th "....."
    ##voice "audio/voice/room8/cat_8_004.mp3"
    cat_th smile "คำตอบอยู่อีกไม่ไกลแล้ว"
    th "เจ้าแมวส้มเดินนำหน้าเรา เราจึงเดินตามมัน"
    hide cat
    jump cutscene_main



