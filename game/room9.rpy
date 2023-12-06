
label room09:
    $ _skipping = True
    scene library_s_1080 with dissolve
    stop music
    play music 不穏

    if room09_is_pass == False: 
        show cat normal with dissolve
        yume  "เป็นโจทย์ที่แปลกจริงๆ"
        cat normal "ข้อท้ายๆก็ต้องยากหน่อยล่ะจ้ะ"
        "คำพูดของเจ้าแมวส้มทำให้เราประหลาดใจเล็กน้อย"
        yume  "นี่เรามาไกลแล้วสินะ"
        cat lick  "ตามหลักก็ใช่จ้ะ"
        yume  "ดูตอบกำกวมนะ"
        "เจ้าแมวส้มเงียบลงสักพัก ไม่นานหลังจากนั้นมันก็มองสบตาเราตรงๆ"
        cat smile "ฉันหวังว่าเธอจะทนรับทุกอย่างได้เมื่อตัวตนของเธอกลับมา"
        yume  "....."
        cat normal  "ฉันเชื่อว่าเธอมีพลังมากพอที่จะออกไปจากสถานที่แห่งนี้ได้นะ"
        "เจ้าแมวส้มมองเราด้วยสายตาคาดหวัง"
        yume  "ฉันก็อยากจะเชื่อแบบนั้นเหมือนกัน"
        "เจ้าแมวส้มหุบปากเงียบลงอีกครั้ง"
        "นี่เราคิดไปเองหรือเปล่านะว่ามันกำลังแอบส่งยิ้มให้เรา"


        show puzzle9
        jump answer_roome09
    
    else :
        "this room has nothing"
        jump main_map 

label answer_roome09:

    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "cafeaulait":
                $ room09_is_pass = True
                "ภาพอดีตถูกฉายขึ้นอีกครั้ง"
                "ต่อจากนี้จะมีความจริงแบบไหนรอเราอยู่กันนะ?"
                hide puzzle9
                jump after_room_9
            else :
                "it's not answer"
                jump answer_roome09
        "return":
            hide puzzle9
            jump main_map

label after_room_9:
    scene fb2_3 with dissolve
    stop music
    play music up_to_you

    mary0  "เธอชอบดื่มกาแฟเหรอ?"
    yume   "Cafe au lait มันก็อร่อยดีนะ"
    "เราตอบคำถามของคู่สนทนาเรียบๆก่อนจะจิบกาแฟหนึ่งอึก"
    mary0  "เลี้ยงกาแฟฉันหน่อยสิ"
    yume  "หา?"
    mary0  "นะๆๆๆ"
    "คู่สนทนาของเราส่งสายตาอ้อนวอน" 
    "ถึงเราจะอยากตอบรับเธอแต่เราก็ทำไม่ได้อยู่ดี"
    yume  "ฉันไม่ได้มีเงินขนาดนั้นนะ อีกอย่างเธอรวยกว่าฉันไม่ใช่หรือไง?"
    mary0  "ของแบบนี้มันไม่ได้อยู่ที่ราคา แต่อยู่ที่ใจจ้ะ"
    yume  "พูดก็พูดไป กาแฟมันก็ต้องใช้เงินจ่ายอยู่ดีแหละ"
    mary0  "เธอนี่ไม่มีอารมณ์ขันเลยนะจ้ะ"
    "คนพูดส่งเสียงหัวเราะกังวานใสในลำคอเบาๆ"
    yume  "นั่นเธอจะทำอะไรน่ะ?"
    mary0  "ดื่มจากแก้วเธอไง"
    yume  "....."
    "เราเงียบเพราะนึกว่าเธอล้อเล่น" 
    "แต่เมื่อเห็นอีกฝ่ายจับแก้วเรายกขึ้น เราก็ยื่นมือกดแขนเธอลงตามปฏิกิริยา"
    mary0  "ทำไมอ่ะ?"
    yume  "ฉันต่างหากที่อยากถามเธอว่าทำไม"
    mary0  "แหม...เราก็สนิทกันจะตาย...แค่ดื่มจากแก้วเดียวกันไม่ตายหรอก..."
    "คู่สนทนาเราพยายามยกแก้วขึ้นอีกครั้ง เราตอบสนองเธอด้วยการกดแขนเธอลง"
    mary0  "อย่าใจร้ายสิ"
    yume  "....."
    mary0  "นิดหน่อยๆน่า"
    "เราในตอนนั้นสะดุ้งเฮือกให้กับรอยยิ้มเจ้าเล่ห์ของคู่สนทนา"
    "อุณหภูมิของใบหน้าเราสูงขึ้นอย่างควบคุมไม่ได้"
    yume  "มันน่าอายจะตาย"
    mary0  "เหรอ?"
    yume  "อย่ามาเหรอสิ"
    mary0  "หืม?"
    yume  "ถ้าเธอดื่มจากแก้วฉัน มันก็เป็นจูบทางอ้อมพอดีสิ"
    mary0  "แค่นั้นก็อายเหรอ?"
    yume  "อายสิ"
    mary0  "ฮิๆ"
    yume  "...!!"

    # Cut Scene
    stop music
    play music 神隠しの真相

    "เรายังพูดไม่ทันจบ ริมฝีปากก็ถูกหยุดลงก่อน"
    "กลิ่นอันหอมหวนและปอยผมสีทองยาวสลวยของคนตรงหน้าปลิวไสวไล้เลียใบหน้าของเรา"
    "สัมผัสนุ่มนวลและอบอุ่นปรากฏขึ้นบนริมฝีปากของเรา ก่อนที่การเชื่อมต่อระหว่างเราสองคนจะถูกคลี่คลายลงเมื่อคนตรงหน้าเลื่อนใบหน้าห่างออกไป"
    "ใบหน้าของเธอแดงระเรื่อน้อยๆ"
    "แน่นอนว่าตอนนี้ใบหน้าของเราก็แดงไม่แพ้เธอ"

    yume  "เมื่อกี้นี้มัน..."
    mary0  "ฉันจะไม่โกหกความรู้สึกของฉันจ้ะ"
    yume  "....."
    mary0 "ฉันน่ะ..."
    
    "ฉันน่ะ...ชอบเธอที่สุดเลย..."
    scene library_s_1080 with dissolve


    yume "...!!"
    "ความทรงจำที่กลับมาทำให้เรารู้สึกถึงแรงกระตุ้น"
    "เราไม่ควรจะมีร่างกายแต่ทำไมรู้สึกเหมือนทั้งร่างร้อนวูบวาบไปหมด"
    "ทั้งๆที่ไม่ควรจะมีดวงตา แต่กลับรู้สึกเหมือนมีสายธารแห่งความเศร้าไหลออกมา"
    "นี่มัน...อะไรกัน...?"
    cat normal "ดีใจด้วยนะที่มาถึงตรงนี้ได้"
    yume "หา?"
    cat smile "เธออาจจะนึกว่าเธอไม่มีตัวตน แต่จริงๆแล้วเธอทำเป็นมองไม่เห็นมันหรือเปล่า?"
    yume "หมายความว่า..."
    cat normal "เธอไม่ได้หายไปไหนหรอก เธอยังอยู่ที่นี่ ตรงนี้"
    yume "....."
    cat ah "เพียงแต่เธอไม่อยากยอมรับว่าตัวเธอมีอยู่ เธอเลยทำเป็นมองข้ามความจริงทั้งหมดไป"
    yume "นั่นมัน..."
    cat normal "หมดเวลาโกหกตัวเองแล้ว...ยูเมะ..."

    scene white with dissolve
    "จบคำพูดของเจ้าแมว ประตูบานหนึ่งก็ถูกเปิดออก"
    "ทั้งๆที่ไม่มีใครแตะต้องประตู แต่มันเปิดง้างออกมาราวกับมีเจตจำนงของมันเอง"
    "สิ่งที่อยู่ข้างหลังบานประตูคือแสงสว่าง"
    "ไม่ช้าหลังจากนั้น แสงสีขาวก็ขยายตัวกว้างขึ้นและกลืนกินร่างของเราเข้าไป"


    jump final


