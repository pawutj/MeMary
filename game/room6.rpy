
label room06:
    $ _skipping = True
    scene garden_n_1080 with dissolve
    stop music
    play music midnight

    if room06_is_pass == False: 

        th "เราจับจ้องโจทย์บนกระดานอย่างไม่วางตา"
        yume_th "นี่มันดอกพลับพลึง?"
        show cat normal with dissolve
    ##voice "audio/voice/room6/cat_6_000.mp3"
        cat_th normal "จำชื่อมันได้ด้วยเหรอ?"
        th "คำพูดของแมวทำให้เรานึกได้ว่าเราพูดชื่อดอกไม้ในภาพขึ้นมาโดยไม่รู้ตัว"
        th "บางสิ่งบางอย่างในตัวเราทำให้เรานึกถึงชื่อของมันได้"
        th "เป็นไปได้ไหมที่ดอกไม้นี้จะเกี่ยวพันกับตัวเราในอดีต"
        yume_th "คงไม่มีทางเลือกอื่นนอกจากต้องตอบคำถามสินะ"
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
                th "ถูกต้อง"
                $ room06_is_pass = True
                th "ภาพดอกไม้เลือนหายไป ภาพอดีตปรากฏขึ้นอีกครั้ง"
                hide puzzle6
                jump after_room_6
            if prepare(input_value) == "spiderlily":
                th "ตอบเป็นชื่อวิทยาศาสตร์"
                jump answer_roome06
            if prepare(input_value) == "sunflower":
                th "อะไรที่มันแทนที่ดอกทานตะวันกันนะ?"
                jump answer_roome06
            else :
                th "ผิดจ้า"
                jump answer_roome06
        "ใบ้หน่อยสิ":
            th "เหมือนฉันเคยได้ยินบทกวีนี้นะ แต่เอ้ะ เหมือนมีอะไรต่างจากต้นฉบับอยู่"
            jump answer_roome06
        "กลับห้องโถง":
            hide puzzle6
            jump main_map

label after_room_6:

    scene fb2_3 with dissolve
    stop music
    play music lost

    th "ดวงตาของใครสักคนหนึ่งกำลังมองดอกไม้ใกล้ตัวเรา"
    th "แววตาส่องประกายแสดงให้เห็นถึงความชื่นชอบที่เธอคนนั้นมีต่อดอกไม้สีขาวบริสุทธิ์"
    yume_th "เธอดูชอบมันนะ"
    ##voice "audio/voice/room6/mary_6_000.mp3"
    mary0_th "หืม?"
    th "เราทักเธอขึ้นทำให้เธอหันมามองหน้าเรา"
    th "เธอเอียงคอน้อยๆด้วยความสงสัยว่าเราเรียกเธอทำไมเพราะปกติเราไม่ค่อยชวนเธอคุยก่อน"
    yume_th "ทำไมเธอถึงชอบดอกไม้นั่นล่ะ?"
    ##voice "audio/voice/room6/mary_6_001.mp3"
    mary0_th "ไม่มีเหตุผลหรอกจ้ะ มันแค่สวยดี"
    yume_th "ดอกพลับพลึงสีแดงมีความหมายไม่ดีเท่าไหร่หรอกนะ"
    ##voice "audio/voice/room6/mary_6_002.mp3"
    mary0_th "แต่ที่ฉันชอบมันคือสีขาวนี้จ้ะ แล้วภาษาดอกไม้ของมันก็ไม่เหมือนกับสีแดงด้วย"
    yume_th "สีแดงสื่อถึงความตาย แล้วสีขาวสื่อถึงอะไรล่ะ?"
    ##voice "audio/voice/room6/mary_6_003.mp3"
    mary0_th "ความหมายของมันโรแมนติคมากเลยล่ะ"
    yume_th "โรแมนติค?"
    th "สัมผัสอบอุ่นปรากฏขึ้นบนหลังมือของเราในอดีต"
    th "มือของคนตรงหน้าวางลงบนหลังมือเราอย่างอ่อนโยนโดยที่เราไม่ทันตั้งตัว"
    ##voice "audio/voice/room6/mary_6_004.mp3"
    mary0_th "ความหมายของมันคือ ‘ฉันปรารถนาแค่เธอคนเดียว’ จ้ะ"
    yume_th "...อึก"
    ##voice "audio/voice/room6/mary_6_005.mp3"
    mary0_th "หน้าแดงง่ายจังนะจ้ะ"
    yume_th "อย่ามาล้อเล่นกันสิ"
    ##voice "audio/voice/room6/mary_6_006.mp3"
    mary0_th "ถ้าไม่ได้ล้อเล่นจะเป็นไงกันนะ?"
    yume_th "ในอดีตสะดุ้งเฮือกเล็กๆ"
    th "ความเขินอายที่แทรกมากะทันหันทำให้เราเม้มปากแน่น"
    yume_th "เธอนี่ขี้แกล้งชะมัด"
    ##voice "audio/voice/room6/mary_6_007.mp3"
    mary0_th "เธอก็หัวทึบพอสมควรเลยจ้ะ"
    yume_th "พูดแบบนี้หมายความว่ายังไง? หา?"
    th "เธอคนนั้นไม่ได้ตอบคำถามของเรา"
    th "เธอเพียงแค่หัวเราะเสียงใสดังกังวานให้เราเท่านั้น"

    scene garden_n_1080 with dissolve
    stop music
    play music midnight

    yume_th "....."
    th "ความทรงจำที่ชวนให้รำลึกถึงค่อยๆเพิ่มขึ้น"
    th "ช่วงเวลาที่ทำให้มีความสุข ชวนให้เราถวิลหาถึงตัวตนในอดีตมากกว่าเดิม"
    show cat normal with dissolve
    ##voice "audio/voice/room6/cat_6_001.mp3"
    cat_th normal "เธอรู้ไหมว่าดอกพลับพลึงสีขาวมีความหมายว่าอะไร?"
    th "เจ้าแมวส้มเอ่ยคำถามที่เสียดแทงเข้ามาในใจเรา"
    th "หลายครั้งแล้วที่มันเหมือนกับกำลังอ่านใจเราอยู่ไม่มีผิด"
    yume_th "ฉันปรารถนาแค่เธอคนเดียว"
    ##voice "audio/voice/room6/cat_6_002.mp3"
    cat_th lick "มันยังมีอีกความหมายหนึ่ง"
    yume_th "คือ?"
    ##voice "audio/voice/room6/cat_6_003.mp3"
    cat_th normal "ฉันเฝ้ารอวันที่จะมาพบกันอีกครั้ง"
    th "ความหมายที่สองทำให้เรารู้สึกเหมือนหัวใจกระตุกวูบ"
    th "ทั้งๆที่ไม่มีร่างกายแล้ว แต่ความเจ็บปวดนี่มันอะไรกันนะ?"
    th "เจ้าแมวส้มพูดแค่นั้นแล้วมันก็เดินนำหน้าเราไปยังประตูอีกฝั่ง"
    th "...สู่ประตูต่อไป..."

    hide cat

    jump cutscene_main




