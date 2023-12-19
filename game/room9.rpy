
label room09:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 不穏

    if room09_is_pass == False: 
        show cat normal with dissolve
        yume_th  "เป็นโจทย์ที่แปลกจริงๆ"
    ##voice "audio/voice/room9/cat_9_000.mp3"
        cat_th normal "ข้อท้ายๆก็ต้องยากหน่อยล่ะจ้ะ"
        th "คำพูดของเจ้าแมวส้มทำให้เราประหลาดใจเล็กน้อย"
        yume_th  "นี่เรามาไกลแล้วสินะ"
    ##voice "audio/voice/room9/cat_9_001.mp3"
        cat_th lick  "ตามหลักก็ใช่จ้ะ"
        yume_th  "ดูตอบกำกวมนะ"
        th "เจ้าแมวส้มเงียบลงสักพัก ไม่นานหลังจากนั้นมันก็มองสบตาเราตรงๆ"
    ##voice "audio/voice/room9/cat_9_002.mp3"
        cat_th smile "ฉันหวังว่าเธอจะทนรับทุกอย่างได้เมื่อตัวตนของเธอกลับมา"
        yume_th  "....."
    ##voice "audio/voice/room9/cat_9_003.mp3"
        cat_th normal  "ฉันเชื่อว่าเธอมีพลังมากพอที่จะออกไปจากสถานที่แห่งนี้ได้นะ"
        th "เจ้าแมวส้มมองเราด้วยสายตาคาดหวัง"
        yume_th  "ฉันก็อยากจะเชื่อแบบนั้นเหมือนกัน"
        th "เจ้าแมวส้มหุบปากเงียบลงอีกครั้ง"
        th "นี่เราคิดไปเองหรือเปล่านะว่ามันกำลังแอบส่งยิ้มให้เรา"


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
                th "ภาพอดีตถูกฉายขึ้นอีกครั้ง"
                th "ต่อจากนี้จะมีความจริงแบบไหนรอเราอยู่กันนะ?"
                hide puzzle9
                jump after_room_9
            else :
                th "it's not answer"
                jump answer_roome09
        "return":
            hide puzzle9
            jump main_map

label after_room_9:
    scene fb2_3 with dissolve
    stop music
    play music up_to_you

    ##voice "audio/voice/room9/mary_9_000.mp3"
    mary0_th  "เธอชอบดื่มกาแฟเหรอ?"
    yume_th   "Cafe au lait มันก็อร่อยดีนะ"
    th "เราตอบคำถามของคู่สนทนาเรียบๆก่อนจะจิบกาแฟหนึ่งอึก"
    ##voice "audio/voice/room9/mary_9_001.mp3"
    mary0_th  "เลี้ยงกาแฟฉันหน่อยสิ"
    yume_th  "หา?"
    ##voice "audio/voice/room9/mary_9_002.mp3"
    mary0_th  "นะๆๆๆ"
    th "คู่สนทนาของเราส่งสายตาอ้อนวอน" 
    th "ถึงเราจะอยากตอบรับเธอแต่เราก็ทำไม่ได้อยู่ดี"
    yume_th  "ฉันไม่ได้มีเงินขนาดนั้นนะ อีกอย่างเธอรวยกว่าฉันไม่ใช่หรือไง?"
    ##voice "audio/voice/room9/mary_9_003.mp3"
    mary0_th  "ของแบบนี้มันไม่ได้อยู่ที่ราคา แต่อยู่ที่ใจจ้ะ"
    yume_th  "พูดก็พูดไป กาแฟมันก็ต้องใช้เงินจ่ายอยู่ดีแหละ"
    ##voice "audio/voice/room9/mary_9_004.mp3"
    mary0_th  "เธอนี่ไม่มีอารมณ์ขันเลยนะจ้ะ"
    th "คนพูดส่งเสียงหัวเราะกังวานใสในลำคอเบาๆ"
    yume_th  "นั่นเธอจะทำอะไรน่ะ?"
    ##voice "audio/voice/room9/mary_9_005.mp3"
    mary0_th  "ดื่มจากแก้วเธอไง"
    yume_th  "....."
    th "เราเงียบเพราะนึกว่าเธอล้อเล่น" 
    th "แต่เมื่อเห็นอีกฝ่ายจับแก้วเรายกขึ้น เราก็ยื่นมือกดแขนเธอลงตามปฏิกิริยา"
    ##voice "audio/voice/room9/mary_9_006.mp3"
    mary0_th  "ทำไมอ่ะ?"
    yume_th  "ฉันต่างหากที่อยากถามเธอว่าทำไม"
    ##voice "audio/voice/room9/mary_9_007.mp3"
    mary0_th  "แหม...เราก็สนิทกันจะตาย...แค่ดื่มจากแก้วเดียวกันไม่ตายหรอก..."
    th "คู่สนทนาเราพยายามยกแก้วขึ้นอีกครั้ง เราตอบสนองเธอด้วยการกดแขนเธอลง"
    ##voice "audio/voice/room9/mary_9_008.mp3"
    mary0_th  "อย่าใจร้ายสิ"
    yume_th  "....."
    ##voice "audio/voice/room9/mary_9_009.mp3"
    mary0_th  "นิดหน่อยๆน่า"
    th "เราในตอนนั้นสะดุ้งเฮือกให้กับรอยยิ้มเจ้าเล่ห์ของคู่สนทนา"
    th "อุณหภูมิของใบหน้าเราสูงขึ้นอย่างควบคุมไม่ได้"
    yume_th  "มันน่าอายจะตาย"
    ##voice "audio/voice/room9/mary_9_010.mp3"
    mary0_th  "เหรอ?"
    yume_th  "อย่ามาเหรอสิ"
    ##voice "audio/voice/room9/mary_9_011.mp3"
    mary0_th  "หืม?"
    yume_th  "ถ้าเธอดื่มจากแก้วฉัน มันก็เป็นจูบทางอ้อมพอดีสิ"
    ##voice "audio/voice/room9/mary_9_012.mp3"
    mary0_th  "แค่นั้นก็อายเหรอ?"
    yume_th  "อายสิ"
    ##voice "audio/voice/room9/mary_9_013.mp3"
    mary0_th  "ฮิๆ"
    yume_th  "...!!"

    # Cut Scene
    stop music
    play music 神隠しの真相

    th "เรายังพูดไม่ทันจบ ริมฝีปากก็ถูกหยุดลงก่อน"
    th "กลิ่นอันหอมหวนและปอยผมสีทองยาวสลวยของคนตรงหน้าปลิวไสวไล้เลียใบหน้าของเรา"
    th "สัมผัสนุ่มนวลและอบอุ่นปรากฏขึ้นบนริมฝีปากของเรา ก่อนที่การเชื่อมต่อระหว่างเราสองคนจะถูกคลี่คลายลงเมื่อคนตรงหน้าเลื่อนใบหน้าห่างออกไป"
    th "ใบหน้าของเธอแดงระเรื่อน้อยๆ"
    th "แน่นอนว่าตอนนี้ใบหน้าของเราก็แดงไม่แพ้เธอ"

    yume_th  "เมื่อกี้นี้มัน..."
    ##voice "audio/voice/room9/mary_9_014.mp3"
    mary0_th  "ฉันจะไม่โกหกความรู้สึกของฉันจ้ะ"
    yume_th  "....."
    ##voice "audio/voice/room9/mary_9_015.mp3"
    mary0_th "ฉันน่ะ..."
    
    th "ฉันน่ะ...ชอบเธอที่สุดเลย..."
    scene library_s_1080 with dissolve


    yume_th "...!!"
    th "ความทรงจำที่กลับมาทำให้เรารู้สึกถึงแรงกระตุ้น"
    th "เราไม่ควรจะมีร่างกายแต่ทำไมรู้สึกเหมือนทั้งร่างร้อนวูบวาบไปหมด"
    th "ทั้งๆที่ไม่ควรจะมีดวงตา แต่กลับรู้สึกเหมือนมีสายธารแห่งความเศร้าไหลออกมา"
    th "นี่มัน...อะไรกัน...?"
    ##voice "audio/voice/room9/cat_9_004.mp3"
    cat_th normal "ดีใจด้วยนะที่มาถึงตรงนี้ได้"
    yume_th "หา?"
    ##voice "audio/voice/room9/cat_9_005.mp3"
    cat_th smile "เธออาจจะนึกว่าเธอไม่มีตัวตน แต่จริงๆแล้วเธอทำเป็นมองไม่เห็นมันหรือเปล่า?"
    yume_th "หมายความว่า..."
    ##voice "audio/voice/room9/cat_9_006.mp3"
    cat_th normal "เธอไม่ได้หายไปไหนหรอก เธอยังอยู่ที่นี่ ตรงนี้"
    yume_th "....."
    ##voice "audio/voice/room9/cat_9_007.mp3"
    cat_th ah "เพียงแต่เธอไม่อยากยอมรับว่าตัวเธอมีอยู่ เธอเลยทำเป็นมองข้ามความจริงทั้งหมดไป"
    yume_th "นั่นมัน..."
    ##voice "audio/voice/room9/cat_9_008.mp3"
    cat_th normal "หมดเวลาโกหกตัวเองแล้ว...ยูเมะ..."

    scene white with dissolve
    th "จบคำพูดของเจ้าแมว ประตูบานหนึ่งก็ถูกเปิดออก"
    th "ทั้งๆที่ไม่มีใครแตะต้องประตู แต่มันเปิดง้างออกมาราวกับมีเจตจำนงของมันเอง"
    th "สิ่งที่อยู่ข้างหลังบานประตูคือแสงสว่าง"
    th "ไม่ช้าหลังจากนั้น แสงสีขาวก็ขยายตัวกว้างขึ้นและกลืนกินร่างของเราเข้าไป"


    jump final



