
label room05:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 不可解な事件簿的な
    if room05_is_pass == False:
        play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
        show cat normal with dissolve
        
        th "ปริศนาข้อต่อไปนี่มันอะไรกันนะ?"
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
        "Answer":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "springisintheair":
                play sound "audio/sfx/correct-6033.mp3" volume 1
                $ room05_is_pass = True
                th "ถูกต้อง"
                en "Correct!"
                th "ปริศนาได้รับการตอบ ความจริงในอดีตจึงฉายขึ้นอีกครั้ง"
                en "The puzzle was solved, and once again, the truth of the past was illuminated."
                hide puzzle5
                jump after_room_5
            if prepare(input_value) == "gstring":
                th "ชื่อเหมือนอะไรหื่นๆเลยนะจ้ะ"
                en "The name sounds kind of risqué, doesn't it?"
                jump answer_roome05
            if prepare(input_value) == "spectrogram":
                th "ดูมาถูกทางอยู่นะจ้ะ" 
                en "It seems you're on the right track."
                jump answer_roome05
            else :
                th "ผิดจ้า"
                en "Wrong."
                jump answer_roome05
        "Hint Me":
            th "เอ.. สเปคตรัม? แกรม? ถ้ารวมกันมันจะได้อะไรนะ /nที่แน่ๆคงไม่ใช่แกรมสีรุ้งแน่ๆ"
            en "Uh.. spectrum? Gram? What do you get if you combine them? \nDefinitely not a rainbow gram, for sure."
            jump answer_roome05
        "Return to Hall":
            hide puzzle5
            jump main_map
        "Skip Answer":
            $ room05_is_pass = True
            hide puzzle5
            jump after_room_5

label after_room_5:
    scene fb2 with dissolve
    stop music
    play music up_to_you

    yume_th "ฟังเพลงคลาสสิคอีกแล้วเหรอ?"
    yume_en "Listening to classical music again?"
    voice "audio/voice/room5/mary_5_000.mp3"
    mary0_th "ใช่จ้ะ"
    mary0_en "Yes."
    yume_th "เพลงอะไร?"
    yume_en "Which piece?"
    voice "audio/voice/room5/mary_5_001.mp3"
    mary0_th "Air on G string จ้ะ"
    mary0_en "Air on G string."
    yume_th "ทำไมชื่อมันดูหื่นจัง"
    yume_en "Why does that title sound so lewd?"
    voice "audio/voice/room5/mary_5_002.mp3"
    mary0_th "ฉันว่าเราเข้าใจกันคนละจีสตริงแล้วนะจ้ะ"
    mary0_en "I think we're thinking of different 'G strings'."
    yume_th "เพลงชื่อหื่นๆนี่มันอะไรกันนะ?"
    yume_en "What's with this weirdly named music?"
    voice "audio/voice/room5/mary_5_003.mp3"
    mary0_th "ถ้าบาคยังยังมีชีวิตอยู่ เขาฟังเธอแล้วคงยกออร์แกนมาทุ่มหัวเธอจ้ะ"
    mary0_en "If Bach were still alive, he might just drop an organ on your head for saying that."
    yume_th "บาคคือใคร?"
    yume_en "Who's Bach?"
    voice "audio/voice/room5/mary_5_004.mp3"
    mary0_th "ชื่อคนแต่งเพลงจ้ะ"
    mary0_en "He's the composer of the piece."
    yume_th "คนอะไรชื่อว่า ‘เห่า’ ...แปลกชะมัด..."
    yume_en "What a strange name, 'Bark'..."
    voice "audio/voice/room5/mary_5_005.mp3"
    mary0_th "เขาไม่ใช่คนอังกฤษจ้ะ เขาเป็นเยอรมัน ชื่อเขาแปลแบบนั้นไม่ได้"
    mary0_en "He's not English, he's German. His name doesn't translate like that."
    yume_th "ฟังเพลงแบบนั้นไม่ง่วงแย่เหรอ"
    yume_en "Doesn't listening to music like that make you sleepy?"
    voice "audio/voice/room5/mary_5_006.mp3"
    mary0_th "เพลงมันก็ละมุนดีนะจ้ะ"
    mary0_en "The music is quite soothing."
    yume_th "มาฟังร็อคแอนด์โรลกับฉันดีกว่านะ ฟังแล้วมันส์กว่าเยอะ"
    yume_en "You should listen to rock and roll with me. It's much more exciting."
    voice "audio/voice/room5/mary_5_007.mp3"
    mary0_th "เธอนี่ไม่มีความละเอียดอ่อนเลยนะจ้ะ"
    mary0_en "You really lack subtlety, don't you?"
    yume_th "ไหงงั้น!?"
    yume_en "What do you mean by that!?"
    voice "audio/voice/room5/mary_5_008.mp3"
    mary0_th "ไม่ฟังเธอแล้ว ฟังเพลงดีกว่าจ้ะ"
    mary0_en "I'm not listening to you anymore. I'd rather listen to the music."
    yume_th "ฉันขอโทษน่า!"
    yume_en "I'm sorry, okay!"

    scene library_s_1080 with dissolve
    stop music
    play music 不可解な事件簿的な

    th "เรากลับมาที่ห้องมืดอีกครั้ง"
    en "I returned to the dark room once more."
    th "เธอคนนั้นชอบฟังเพลงคลาสสิคสินะ เราจำได้แล้ว"
    en "She liked classical music, I remember now."
    th "แล้วเราก็ชวนเธอมาฟังเพลงที่เราชอบฟังบ้าง พอเธอฟังจบก็ไม่ฟังเพลงเราอีกเลย"
    en  "I even invited her to listen to the music I liked, but after hearing it, she never listened to my music again."
    th "จริงอยู่ที่คุยกันถูกคอ แต่รสนิยมหลายๆอย่างของเราสวนทางกัน เป็นเรื่องน่าแปลกจริงๆที่เราอยู่ด้วยกันมานานหลายปี"
    en "True, we got along well, but in many ways, our tastes diverged. It's strange how we've been together for so many years."
    th "...หลายปี...?"
    en "...Many years...?"
    yume_th "...อึก"
    yume_en "...Ugh"
    show cat normal with dissolve
    voice "audio/voice/room5/cat_5_002.mp3"
    cat_th normal "เป็นไงบ้าง?"
    cat_en normal "How are you feeling?"
    yume_th "เหมือนจะคิดอะไรออก แต่จู่ๆก็ปวดทรมานไปหมดน่ะ"
    yume_en "It's like I'm on the verge of remembering something, then suddenly it all turns to pain."
    voice "audio/voice/room5/cat_5_003.mp3"
    cat_th normal "นั่นเพราะเธอยังไขปริศนาไม่ได้ทั้งหมด"
    cat_en normal "That's because you haven't solved all the puzzles yet."
    yume_th "....."
    yume_en "....."
    voice "audio/voice/room5/cat_5_004.mp3"
    cat_th normal "ไม่ต้องรีบร้อน ปลายทางยังอีกยาวไกล"
    cat_en normal "Don't rush. The journey is still long."
    th "เรากับเจ้าแมวส้มเดินไปข้างหน้า"
    en "The orange cat and I continued forward."
    play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
    th "...สู่ประตูต่อไป..."
    en "...Towards the next door..."

    hide cat
    jump cutscene_main
