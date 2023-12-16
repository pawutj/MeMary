
label room05:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 不可解な事件簿的な
    if room05_is_pass == False:
        show cat normal with dissolve
        
        "ปริศนาข้อต่อไปนี่มันอะไรกันนะ?"
    ##voice "audio/voice/room5/cat_5_000.mp3"
        cat_th normal "เธอชอบฟังเพลงหรือเปล่าล่ะ?"
        yume_th "หา?"
    ##voice "audio/voice/room5/cat_5_001.mp3"
        cat_th ah "ลองตอบคำถามดู"
        "เจ้าแมวส้มว่าแล้วก็ส่งยิ้มบางๆให้เรา"
        hide cat
        jump answer_roome05
        
    else :
        "this room has nothing"
        jump main_map 

label answer_roome05:
    show puzzle5 with dissolve
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "springisintheair":
                $ room05_is_pass = True
                th "ถูกต้อง"
                th "ปริศนาได้รับการตอบ ความจริงในอดีตจึงฉายขึ้นอีกครั้ง"
                hide puzzle5
                jump after_room_5
            if prepare(input_value) == "gstring":
                th "ชื่อเหมือนอะไรหื่นๆเลยนะจ้ะ" 
                jump answer_roome05
            if prepare(input_value) == "spectrogram":
                th "ดูมาถูกทางอยู่นะจ้ะ" 
                jump answer_roome05
            else :
                th "ผิดจ้า"
                jump answer_roome05
        "ใบ้หน่อยสิ":
            th "เอ.. สเปคตรัม? แกรม? ถ้ารวมกันมันจะได้อะไรนะ /nที่แน่ๆคงไม่ใช่แกรมสีรุ้งแน่ๆ"
            jump answer_roome05
        "กลับห้องรวม":
            hide puzzle5
            jump main_map

label after_room_5:
    scene fb2_2 with dissolve
    stop music
    play music up_to_you

    yume_th "ฟังเพลงคลาสสิคอีกแล้วเหรอ?"
    ##voice "audio/voice/room5/mary_5_000.mp3"
    mary0_th "ใช่จ้ะ"
    yume_th "เพลงอะไร?"
    ##voice "audio/voice/room5/mary_5_001.mp3"
    mary0_th "Air on G string จ้ะ"
    yume_th "ทำไมชื่อมันดูหื่นจัง"
    ##voice "audio/voice/room5/mary_5_002.mp3"
    mary0_th "ฉันว่าเราเข้าใจกันคนละจีสตริงแล้วนะจ้ะ"
    yume_th "เพลงชื่อหื่นๆนี่มันอะไรกันนะ?"
    ##voice "audio/voice/room5/mary_5_003.mp3"
    mary0_th "ถ้าบาคยังยังมีชีวิตอยู่ เขาฟังเธอแล้วคงยกออร์แกนมาทุ่มหัวเธอจ้ะ"
    yume_th "บาคคือใคร?"
    ##voice "audio/voice/room5/mary_5_004.mp3"
    mary0_th "ชื่อคนแต่งเพลงจ้ะ"
    yume_th "คนอะไรชื่อว่า ‘เห่า’ ...แปลกชะมัด..."
    ##voice "audio/voice/room5/mary_5_005.mp3"
    mary0_th "เขาไม่ใช่คนอังกฤษจ้ะ เขาเป็นเยอรมัน ชื่อเขาแปลแบบนั้นไม่ได้"
    yume_th "ฟังเพลงแบบนั้นไม่ง่วงแย่เหรอ"
    ##voice "audio/voice/room5/mary_5_006.mp3"
    mary0_th "เพลงมันก็ละมุนดีนะจ้ะ"
    yume_th "มาฟังร็อคแอนด์โรลกับฉันดีกว่านะ ฟังแล้วมันส์กว่าเยอะ"
    ##voice "audio/voice/room5/mary_5_007.mp3"
    mary0_th "เธอนี่ไม่มีความละเอียดอ่อนเลยนะจ้ะ"
    yume_th "ไหงงั้น!?"
    ##voice "audio/voice/room5/mary_5_008.mp3"
    mary0_th "ไม่ฟังเธอแล้ว ฟังเพลงดีกว่าจ้ะ"
    yume_th "ฉันขอโทษน่า!"

    scene library_s_1080 with dissolve
    stop music
    play music 不可解な事件簿的な

    th "เรากลับมาที่ห้องมืดอีกครั้ง"
    th "เธอคนนั้นชอบฟังเพลงคลาสสิคสินะ เราจำได้แล้ว"
    th "แล้วเราก็ชวนเธอมาฟังเพลงที่เราชอบฟังบ้าง พอเธอฟังจบก็ไม่ฟังเพลงเราอีกเลย"
    th "จริงอยู่ที่คุยกันถูกคอ แต่รสนิยมหลายๆอย่างของเราสวนทางกัน เป็นเรื่องน่าแปลกจริงๆที่เราอยู่ด้วยกันมานานหลายปี"
    th "...หลายปี...?"
    yume_th "...อึก"
    show cat normal with dissolve
    ##voice "audio/voice/room5/cat_5_002.mp3"
    cat_th normal "เป็นไงบ้าง?"
    yume_th "เหมือนจะคิดอะไรออก แต่จู่ๆก็ปวดทรมานไปหมดน่ะ"
    ##voice "audio/voice/room5/cat_5_003.mp3"
    cat_th normal "นั่นเพราะเธอยังไขปริศนาไม่ได้ทั้งหมด"
    yume_th "....."
    ##voice "audio/voice/room5/cat_5_004.mp3"
    cat_th normal "ไม่ต้องรีบร้อน ปลายทางยังอีกยาวไกล"
    "เรากับเจ้าแมวส้มเดินไปข้างหน้า"
    "...สู่ประตูต่อไป..."

    hide cat
    jump cutscene_main
