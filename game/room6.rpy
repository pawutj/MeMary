
label room06:
    $ _skipping = True
    scene garden_n_1080 with dissolve
    stop music
    play music midnight

    if room06_is_pass == False: 
        play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
        th "เราจับจ้องโจทย์บนกระดานอย่างไม่วางตา"
        en "I stared intently at the puzzle on the board, unable to look away."
        yume_th "นี่มันดอกพลับพลึง?"
        yume_en "Is this a plumeria flower?"
        show cat normal with dissolve
        
        voice "audio/voice/room6/cat_6_000.mp3"
        cat_th normal "จำชื่อมันได้ด้วยเหรอ?"
        cat_en normal "You remember its name?"
        th "คำพูดของแมวทำให้เรานึกได้ว่าเราพูดชื่อดอกไม้ในภาพขึ้นมาโดยไม่รู้ตัว"
        en "The cat's remark made me realize I had unknowingly spoken the name of the flower in the picture."
        th "บางสิ่งบางอย่างในตัวเราทำให้เรานึกถึงชื่อของมันได้"
        en "Something within me recalled its name."
        th "เป็นไปได้ไหมที่ดอกไม้นี้จะเกี่ยวพันกับตัวเราในอดีต"
        en "Could it be that this flower is connected to my past?"
        yume_th "คงไม่มีทางเลือกอื่นนอกจากต้องตอบคำถามสินะ"
        yume_en "It seems I have no choice but to answer the question."
        hide cat
        
        show puzzle6
        jump answer_roome06
        
    else :
        th "this room has nothing"
        jump main_map 

label answer_roome06:
    menu:
        "ตอบคำถาม":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "lycorisradiata":
                play sound "audio/sfx/correct-6033.mp3" volume 1
                th "ถูกต้อง"
                en "Correct!"
                $ room06_is_pass = True
                th "ภาพดอกไม้เลือนหายไป ภาพอดีตปรากฏขึ้นอีกครั้ง"
                en "The image of the flower fades away, and the image of the past appears once again."
                hide puzzle6
                jump after_room_6
            if prepare(input_value) == "spiderlily":
                th "ตอบเป็นชื่อวิทยาศาสตร์"
                en "Answer with the scientific name."
                jump answer_roome06
            if prepare(input_value) == "sunflower":
                th "อะไรที่มันแทนที่ดอกทานตะวันกันนะ?"
                en "What could replace the sunflower?"
                jump answer_roome06
            else :
                th "ผิดจ้า"
                en "Wrong."
                jump answer_roome06
        "ใบ้หน่อยสิ":
            th "เหมือนฉันเคยได้ยินบทกวีนี้ Willian Blake รึเปล่านะ แต่เอ้ะ เหมือนมีอะไรต่างจากต้นฉบับอยู่"
            en "It's like I've heard this poem before, from William Blake perhaps, but wait, it seems to differ from the original."
            jump answer_roome06
        "กลับห้องโถง":
            hide puzzle6
            jump main_map

label after_room_6:

    scene fb2_3 with dissolve
    stop music
    play music lost

    th "ดวงตาของใครสักคนหนึ่งกำลังมองดอกไม้ใกล้ตัวเรา"
    en "Someone's eyes were gazing at a flower close to us."
    th "แววตาส่องประกายแสดงให้เห็นถึงความชื่นชอบที่เธอคนนั้นมีต่อดอกไม้สีขาวบริสุทธิ์"
    en "Their eyes sparkled, showing a fondness for the pure white flower."
    yume_th "เธอดูชอบมันนะ"
    yume_en "You seem to like it."
    voice "audio/voice/room6/mary_6_000.mp3"
    mary0_th "หืม?"
    mary0_en "Hmm?"
    th "เราทักเธอขึ้นทำให้เธอหันมามองหน้าเรา"
    en "I called out to her, causing her to turn and face me."
    th "เธอเอียงคอน้อยๆด้วยความสงสัยว่าเราเรียกเธอทำไมเพราะปกติเราไม่ค่อยชวนเธอคุยก่อน"
    en "She tilted her head slightly, puzzled why I was initiating conversation, as I usually didn't engage her first."
    yume_th "ทำไมเธอถึงชอบดอกไม้นั่นล่ะ?"
    yume_en "Why do you like that flower?"
    voice "audio/voice/room6/mary_6_001.mp3"
    mary0_th "ไม่มีเหตุผลหรอกจ้ะ มันแค่สวยดี"
    mary0_en "No particular reason. It's just beautiful."
    yume_th "ดอกพลับพลึงสีแดงมีความหมายไม่ดีเท่าไหร่หรอกนะ"
    yume_en "Red plumerias aren't considered very auspicious, you know."
    voice "audio/voice/room6/mary_6_002.mp3"
    mary0_th "แต่ที่ฉันชอบมันคือสีขาวนี้จ้ะ แล้วภาษาดอกไม้ของมันก็ไม่เหมือนกับสีแดงด้วย"
    mary0_en "But the ones I like are these white ones. Their floral language isn't the same as the red ones."
    yume_th "สีแดงสื่อถึงความตาย แล้วสีขาวสื่อถึงอะไรล่ะ?"
    yume_en "Red symbolizes death, but what does white signify?"
    voice "audio/voice/room6/mary_6_003.mp3"
    mary0_th "ความหมายของมันโรแมนติคมากเลยล่ะ"
    mary0_en "Its meaning is quite romantic."
    yume_th "โรแมนติค?"
    yume_en "Romantic?"
    th "สัมผัสอบอุ่นปรากฏขึ้นบนหลังมือของเราในอดีต"
    en "A warm touch appeared on the back of my hand in the past."
    th "มือของคนตรงหน้าวางลงบนหลังมือเราอย่างอ่อนโยนโดยที่เราไม่ทันตั้งตัว"
    en "The hand of the person in front of me gently rested on mine unexpectedly."
    voice "audio/voice/room6/mary_6_004.mp3"
    mary0_th "ความหมายของมันคือ ‘ฉันปรารถนาแค่เธอคนเดียว’ จ้ะ"
    mary0_en "It means 'I desire only you'."
    yume_th "...อึก"
    yume_en "...Uh"
    voice "audio/voice/room6/mary_6_005.mp3"
    mary0_th "หน้าแดงง่ายจังนะจ้ะ"
    mary0_en "You blush so easily."
    yume_th "อย่ามาล้อเล่นกันสิ"
    yume_en "Stop teasing me."
    voice "audio/voice/room6/mary_6_006.mp3"
    mary0_th "ถ้าไม่ได้ล้อเล่นจะเป็นไงกันนะ?"
    mary0_en "What if it's not just teasing?"
    th "เราในอดีตสะดุ้งเฮือกเล็กๆ"
    en "I, from the past, jolted slightly."
    th "ความเขินอายที่แทรกมากะทันหันทำให้เราเม้มปากแน่น"
    en "Sudden embarrassment made me purse my lips tightly."
    yume_th "เธอนี่ขี้แกล้งชะมัด"
    yume_en "You're such a tease."
    voice "audio/voice/room6/mary_6_007.mp3"
    mary0_th "เธอก็หัวทึบพอสมควรเลยจ้ะ"
    mary0_en "You can be quite dense sometimes."
    yume_th "พูดแบบนี้หมายความว่ายังไง? หา?"
    yume_en "What does that mean? Huh?"
    th "เธอคนนั้นไม่ได้ตอบคำถามของเรา"
    en "She didn't answer my question."
    th "เธอเพียงแค่หัวเราะเสียงใสดังกังวานให้เราเท่านั้น"
    en "She just laughed a clear, ringing laugh for me alone."

    scene garden_n_1080 with dissolve
    stop music
    play music midnight

    yume_th "....."
    yume_en "....."
    th "ความทรงจำที่ชวนให้รำลึกถึงค่อยๆเพิ่มขึ้น"
    en "The memories that evoke nostalgia are slowly increasing."
    th "ช่วงเวลาที่ทำให้มีความสุข ชวนให้เราถวิลหาถึงตัวตนในอดีตมากกว่าเดิม"
    en "Times of happiness lead us to yearn more for our past selves."
    show cat normal with dissolve
    voice "audio/voice/room6/cat_6_001.mp3"
    cat_th normal "เธอรู้ไหมว่าดอกพลับพลึงสีขาวมีความหมายว่าอะไร?"
    cat_en normal "Do you know what the white spider-lily signifies?"
    th "เจ้าแมวส้มเอ่ยคำถามที่เสียดแทงเข้ามาในใจเรา"
    en "The orange cat asks a question that pierces our heart."
    th "หลายครั้งแล้วที่มันเหมือนกับกำลังอ่านใจเราอยู่ไม่มีผิด"
    en "Many times it feels like it's reading our minds accurately."
    yume_th "ฉันปรารถนาแค่เธอคนเดียว"
    yume_en "All I desire is just you."
    voice "audio/voice/room6/cat_6_002.mp3"
    cat_th lick "มันยังมีอีกความหมายหนึ่ง"
    cat_en lick "There is another meaning to it."
    yume_th "คือ?"
    yume_en "What is it?"
    voice "audio/voice/room6/cat_6_003.mp3"
    cat_th normal "ฉันเฝ้ารอวันที่จะมาพบกันอีกครั้ง"
    cat_en normal "I am waiting for the day we will meet again."
    th "ความหมายที่สองทำให้เรารู้สึกเหมือนหัวใจกระตุกวูบ"
    en "The second meaning makes us feel a sudden tug at our heart."
    th "ทั้งๆที่ไม่มีร่างกายแล้ว แต่ความเจ็บปวดนี่มันอะไรกันนะ?"
    en "Even though I no longer have a body, what is this pain?"
    th "เจ้าแมวส้มพูดแค่นั้นแล้วมันก็เดินนำหน้าเราไปยังประตูอีกฝั่ง"
    en "The orange cat says just that and then leads us to the door on the other side."
    play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
    th "...สู่ประตูต่อไป..."
    en "...towards the next door..."

    hide cat

    jump cutscene_main




