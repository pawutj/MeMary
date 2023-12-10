
label room05:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 不可解な事件簿的な
    if room05_is_pass == False:
        show cat normal with dissolve
        
        "ปริศนาข้อต่อไปนี่มันอะไรกันนะ?"
        cat normal "เธอชอบฟังเพลงหรือเปล่าล่ะ?"
        yume "หา?"
        cat ah "ลองตอบคำถามดู"
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
                "ถูกต้อง"
                "ปริศนาได้รับการตอบ ความจริงในอดีตจึงฉายขึ้นอีกครั้ง"
                hide puzzle5
                jump after_room_5
            if prepare(input_value) == "gstring":
                "ชื่อเหมือนอะไรหื่นๆเลยนะจ้ะ" 
                jump answer_roome05
            if prepare(input_value) == "spectrogram":
                "ดูมาถูกทางอยู่นะจ้ะ" 
                jump answer_roome05
            else :
                "ผิดจ้า"
                jump answer_roome05
        "ใบ้หน่อยสิ":
            "เอ.. สเปคตรัม? แกรม? มันคืออะไรกันนะ"
            jump answer_roome05
        "กลับห้องรวม":
            hide puzzle5
            jump main_map

label after_room_5:
    scene fb2_2 with dissolve
    stop music
    play music up_to_you

    yume "ฟังเพลงคลาสสิคอีกแล้วเหรอ?"
    mary0 "ใช่จ้ะ"
    yume "เพลงอะไร?"
    mary0 "Air on G string จ้ะ"
    yume "ทำไมชื่อมันดูหื่นจัง"
    mary0 "ฉันว่าเราเข้าใจกันคนละจีสตริงแล้วนะจ้ะ"
    yume "เพลงชื่อหื่นๆนี่มันอะไรกันนะ?"
    mary0 "ถ้าบาคยังยังมีชีวิตอยู่ เขาฟังเธอแล้วคงยกออร์แกนมาทุ่มหัวเธอจ้ะ"
    yume "บาคคือใคร?"
    mary0 "ชื่อคนแต่งเพลงจ้ะ"
    yume "คนอะไรชื่อว่า ‘เห่า’ ...แปลกชะมัด..."
    mary0 "เขาไม่ใช่คนอังกฤษจ้ะ เขาเป็นเยอรมัน ชื่อเขาแปลแบบนั้นไม่ได้"
    yume "ฟังเพลงแบบนั้นไม่ง่วงแย่เหรอ"
    mary0 "เพลงมันก็ละมุนดีนะจ้ะ"
    yume "มาฟังร็อคแอนด์โรลกับฉันดีกว่านะ ฟังแล้วมันส์กว่าเยอะ"
    mary0 "เธอนี่ไม่มีความละเอียดอ่อนเลยนะจ้ะ"
    yume "ไหงงั้น!?"
    mary0 "ไม่ฟังเธอแล้ว ฟังเพลงดีกว่าจ้ะ"
    yume "ฉันขอโทษน่า!"

    scene library_s_1080 with dissolve
    stop music
    play music 不可解な事件簿的な

    "เรากลับมาที่ห้องมืดอีกครั้ง"
    "เธอคนนั้นชอบฟังเพลงคลาสสิคสินะ เราจำได้แล้ว"
    "แล้วเราก็ชวนเธอมาฟังเพลงที่เราชอบฟังบ้าง พอเธอฟังจบก็ไม่ฟังเพลงเราอีกเลย"
    "จริงอยู่ที่คุยกันถูกคอ แต่รสนิยมหลายๆอย่างของเราสวนทางกัน เป็นเรื่องน่าแปลกจริงๆที่เราอยู่ด้วยกันมานานหลายปี"
    "...หลายปี...?"
    yume "...อึก"
    show cat normal with dissolve
    cat normal "เป็นไงบ้าง?"
    yume "เหมือนจะคิดอะไรออก แต่จู่ๆก็ปวดทรมานไปหมดน่ะ"
    cat normal "นั่นเพราะเธอยังไขปริศนาไม่ได้ทั้งหมด"
    yume "....."
    cat normal "ไม่ต้องรีบร้อน ปลายทางยังอีกยาวไกล"
    "เรากับเจ้าแมวส้มเดินไปข้างหน้า"
    "...สู่ประตูต่อไป..."

    hide cat
    jump cutscene_main