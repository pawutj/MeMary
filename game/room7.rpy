
label room07:   
    $ _skipping = True
    scene garden_n_1080 with dissolve
    stop music
    play music 廃墟洋館

    if room07_is_pass == False: 
        show cat normal with dissolve
        voice "audio/voice/room7/cat_7_000.mp3"
        cat_th normal "เธอชอบดูดาวหรือเปล่าล่ะ?"
        cat_en normal "Do you like stargazing?"
        th "คำถามของแมวส้มทำให้เรานึกถึงความทรงจำบางอย่าง"
        en "The orange cat's question triggered a memory."
        th "เมื่อสมัยก่อนเคยมีใครถามเราแบบนี้หรือเปล่านะ?"
        en "Had someone asked me this before?"
        yume_th "เฉยๆน่ะ"
        yume_en "It's okay."
        voice "audio/voice/room7/cat_7_001.mp3"
        cat_th normal "ทั้งๆที่ปากบอกเฉยๆ แต่น้ำเสียงมีแต่อารมณ์หม่นๆนะ"
        cat_en normal "Even though you say it's okay, your tone sounds rather melancholy."
        yume_th  "....."
        yume_en "....."
        voice "audio/voice/room7/cat_7_002.mp3"
        cat_th smile "ไม่ต้องคิดมากหรอกจ้ะ มองโจทย์สักพักก็เข้าใจเอง"
        cat_en smile "Don't overthink it. Just look at the puzzle for a while, and you'll understand."
        scene star3 with dissolve
        yume_th  "ฉันเห็นแต่แสงสว่างยุ่บยั่บเต็มไปหมด"
        yume_en "All I see are flickering lights everywhere."
        voice "audio/voice/room7/cat_7_003.mp3"
        cat_th ah "คำตอบมันก็อยู่ในแสงสว่างท่ามกลางท้องฟ้าสีดำพวกนั้นล่ะ"
        cat_en ah "The answer lies within those lights twinkling in the dark sky."
        yume_th  "คำตอบครั้งนี้น่าจะหายากพอสมควร"
        yume_en "This answer seems hard to find."
        #voice "audio/voice/room7/cat_7_004.mp3"
        cat_th lick "..."
        cat_en lick "..."
        yume_th  "เงียบทำไมล่ะ?"
        yume_en "Why so silent?"
        th "เจ้าแมวส้มเบิกตากว้างขึ้นน้อยๆก่อนจะพูดขึ้น"
        en "The orange cat's eyes widened slightly before it spoke."
        voice "audio/voice/room7/cat_7_005.mp3"
        cat_th ah  "เธอดูพูดเก่งขึ้นนะ"
        cat_en ah "You seem to be more talkative."
        yume_th  "เหรอ?"
        yume_en "Really?"
        voice "audio/voice/room7/cat_7_006.mp3"
        cat_th lick "เริ่มเข้าใจตัวเองมากขึ้นแล้วหรือเปล่าเลยต่อปากต่อคำเก่งขึ้นน่ะ?"
        cat_en lick "Are you beginning to understand yourself better? Is that why you're more articulate now?"
        th "แมวส้มถามลองใจเรา แต่เรากลับตอบมันได้แค่ความเงียบ"
        en "The orange cat probed, but I could only respond with silence."
        th "เรายังไม่แน่ใจหรอกว่าเราตอนนี้ใกล้เคียงกับเราตัวจริงมากแค่ไหน"
        en "I wasn't sure how close I was to my true self yet."
        yume_th "ขอเวลาสักพัก ฉันจะตอบข้อนี้ได้เอง"
        yume_en "Give me a moment. I'll figure out this puzzle on my own."
        voice "audio/voice/room7/cat_7_007.mp3"
        cat_th smile  "จะรอดูนะ"
        cat_en smile "I'll be waiting to see."
        th "เจ้าแมวส้มส่งยิ้มให้เรา"
        en "The orange cat gave me a smile."

        
        jump answer_room7
    
    else :
        th "this room has nothing"
        en "this room has nothing"
        jump main_map 

label answer_room7:
    show puzzle7
    menu:
        "Answer":
            $ input_value = renpy.input("Answer?")
            if prepare(input_value) == "orion":
                $ room07_is_pass = True
                play sound "audio/sfx/correct-6033.mp3" volume 1
                th "ท้องฟ้าสีดำที่เต็มไปด้วยดวงดาวเปลี่ยนผันกลายเป็นฉากขาว"
                en "The black sky filled with stars transformed into a white backdrop."
                th "ความทรงจำในอดีตกำลังหลั่งไหลเข้ามาอีกครั้งราวกับสายน้ำ"
                en "Memories from the past began to flow into me like a river."

                hide puzzle7
                jump after_room_7

            if prepare(input_value) == "libra" :
                jump easteregg_2
            else :
                th "it's not answer"
                en "Wrong!"
                jump answer_room7
        "Hint":
            th "เหมือนฉันจะเห็นดาวสีน้ำเงินเข้มอยู่ในภาพนะ ดูผิดธรรมชาติมากเลย"
            jump answer_room7

        "Hint More" :
            ""
            menu : 
                "Try Answer":
                    jump answer_room7
                "Skip Answer":
                    hide puzzle7
                    $ room07_is_pass = True
                    jump after_room_7

        "Return to Hall":
            hide puzzle7
            jump main_map

label after_room_7:
    scene fb2 with dissolve
    stop music
    play music 神隠しの真相

    voice "audio/voice/room7/mary_7_000.mp3"
    mary0_th "เธอชอบดูดาวหรือเปล่าล่ะ?"
    mary0_en "Do you like stargazing?"
    yume_th "หา?"
    yume_en "Huh?"
    voice "audio/voice/room7/mary_7_001.mp3"
    mary0_th "จะ ‘หา’ ทำไมล่ะจ้ะ? ฉันก็ถามอะไรตรงไปตรงมานี่"
    mary0_en "Why the \'huh\'? I'm just asking a straightforward question."
    yume_th "ไม่ได้ชอบเป็นพิเศษหรอก"
    yume_en "I'm indifferent to it."
    voice "audio/voice/room7/mary_7_002.mp3"
    mary0_th "แล้วทำไมมาดูกับฉันล่ะจ้ะ?"
    yume_th "ก็..."
    voice "audio/voice/room7/mary_7_003.mp3"
    mary0_th "ก็...?"
    yume_th "ปล่อยให้ผู้หญิงคนเดียวมาดูดาวที่เปลี่ยวตอนกลางคืนมันอันตรายนี่นา"
    #voice "audio/voice/room7/mary_7_004.mp3"
    mary0_th "......."
    "ความเงียบก่อตัวขึ้นระหว่างเราสองคนสักพัก"
    "ไม่นานหลังจากนั้น มือบางของอีกฝ่ายก็วางลงบนศีรษะเราเบาๆ"
    yume_th "เฮ้ย จะจับหัวฉันทำไม?"
    voice "audio/voice/room7/mary_7_005.mp3"
    mary0_th "ฉันรู้จ้ะว่าเธอไม่ชอบให้คนอื่นแตะตัว แต่เธอตอนนี้น่ารักดีจ้ะเลยเผลอลูบหัว"
    yume_th "พิลึกจริง"
    voice "audio/voice/room7/mary_7_006.mp3"
    mary0_th "งั้นเรามาทายปริศนากันดีกว่า"
    yume_th "ปริศนาอีกแล้วเรอะ?"
    voice "audio/voice/room7/mary_7_007.mp3"
    mary0_th "อย่าทำหน้าเบื่อโลกสิจ้ะ"
    yume_th "ขนาดเลิกเรียนแล้วก็ยังมานั่งทายปริศนาชวนหัว ชีวิตฉันต้องไขปริศนาไปถึงเมื่อไหร่กัน?"
    voice "audio/voice/room7/mary_7_008.mp3"
    mary0_th "จนกว่าฉันจะขี้เกียจถามเธอจ้ะ"
    yume "สรุปง่ายๆคือจนกว่าพวกเราจะตายกันสักข้างสินะ"
    voice "audio/voice/room7/mary_7_009.mp3"
    mary0_th "เอาล่ะ...กลุ่มดาวดวงนั้นคือกลุ่มดาวอะไรจ้ะ?"
    yume_th "ไม่ได้ฟังฉันสักแอะเลยนี่หว่า"
    "เราถอนหายใจเบาๆแต่ก็ยอมมองตามนิ้วของคนข้างตัวแต่โดยดี"
    voice "audio/voice/room7/mary_7_010.mp3"
    mary0_th "ลองทายดูสิ ข้อนี้ไม่ยา..."
    yume_th "กลุ่มดาวนายพรานสินะ"
    th "คำตอบอันรวดเร็วของเราทำให้อีกฝ่ายดูประหลาดใจไม่น้อย"
    th "เธอคงคาดหวังว่าเราจะตอบไม่ได้แล้วให้เธอสอนเราแหงๆ มุกนี้โดนมาเยอะแล้ว"
    yume_th "เอามือมาวางบนหน้าผากฉันทำไม?"
    voice "audio/voice/room7/mary_7_011.mp3"
    mary0_th "เธอฉลาดผิดปกติเลยนึกว่าไข้ขึ้นอ่ะจ้ะ"
    yume_th "ตอบผิดก็โดนว่าโง่ ตอบผิดก็หาว่าป่วย นี่มันทั้งขึ้นทั้งล่องชัดๆ"
    voice "audio/voice/room7/mary_7_012.mp3"
    mary0_th "ล้อเล่นจ้ะๆ ว่าแต่เธอรู้ได้ไงจ้ะ?"
    yume_th "กลุ่มดาวนี้มันดังอยู่ ฉันพอจะรู้จักน่ะ"
    voice "audio/voice/room7/mary_7_013.mp3"
    mary0_th "เดาว่าอ่านการ์ตูนมาเลยจำได้แหงๆจ้ะ"
    yume_th "รู้ได้ไง...ไม่สิ อย่าคิดว่าฉันจะตื้นเขินขนาดนั้นสิ"
    voice "audio/voice/room7/mary_7_014.mp3"
    mary0_th "ไม่เนียนเลยจ้ะ"
    th "เด็กสาวข้างตัวหัวเราะเสียงใส ทำให้เรารู้สึกหน้าอุ่นขึ้นอย่างควบคุมไม่ได้"
    th "สักพักหลังจากนั้น คนข้างกายเราก็หุบยิ้มลงและจ้องหน้าเรา"

    stop music
    play music 手紙のさよなら
    
    voice "audio/voice/room7/mary_7_015.mp3"
    mary0_th "ช่วงนี้เธอดูเครียดๆนะจ้ะ"
    mary0_en "You seem stressed lately."
    yume_th "....."
    yume_en "....."
    th "เราหุบปากเงียบลง"
    en "I fell silent."
    th "ทั้งๆที่เมื่อครู่ยังแสดงความขี้เล่นออกมาแท้ๆ แต่ตอนนี้คนข้างตัวเรากลับมองเราด้วยสายตาเจนจัด"
    en "Despite my playful demeanor just moments ago, the person beside me now looked at me with intense scrutiny"
    th "อย่างกับคนคนนี้มองทะลุผ่านเราไม่มีผิด"
    en "as if seeing right through me."
    yume_th "เรื่องเดิมๆน่ะ"
    yume_en "It's the same old issues."
    voice "audio/voice/room7/mary_7_016.mp3"
    mary0_th "ปัญหาที่บ้านเหรอจ้ะ?"
    mary0_en "Family problems?"
    th "คำกล่าวของเด็กสาวข้างกายเสียดแทงใจเรา"
    en "The girl's words pierced through me."
    th "เราไม่สามารถปิดบังจิตใจของเราจากเธอได้จริงๆ"
    en "I couldn't hide my feelings from her"
    yume_th "มองออกตลอดเลยนะ"
    yume_en "You always see right through me."
    voice "audio/voice/room7/mary_7_017.mp3"
    mary0_th "คนที่มีปัญหาคล้ายๆกันจะเข้าใจกันดีจ้ะ"
    mary0_en "People with similar troubles understand each other well."
    th "เด็กสาวยิ้มเศร้าๆให้เรา"
    en "The girl gave me a sad smile."
    th "เราได้ยินเสียงถอนใจจากคู่สนทนาที่เงยหน้ามองฟ้าด้วยสายตาเหม่อลอย"
    en "I heard a sigh from my companion as she looked up at the sky, lost in thought."
    yume_th "พ่อของฉันขโมยของคนอื่นจนต้องเข้าคุกเข้าตะรางอีกแล้ว"
    yume_en  "My dad got caught stealing again, he's back in jail."
    #voice "audio/voice/room7/mary_7_018.mp3"
    mary0_th "....."
    mary0_en "....."
    yume_th "ตั้งแต่แม่ก่อคดีรุนแรงและตายไป พ่อก็เปลี่ยนไปเหมือนอีกคนหนึ่งเลย" 
    yume_en "Ever since mom committed that violent crime and died, dad's changed. He's like a different person."
    #voice "audio/voice/room7/mary_7_019.mp3"
    mary0_th "....."
    mary0_en "....."
    yume_th "ชีวิตมันห่วยแตกเนอะ"
    yume_en "Life's pretty messed up, huh?"
    th "เด็กสาวข้างกายเราไม่ได้พูดอะไรมากความ เธอเพียงแค่ยื่นมือมาลูบศีรษะเราเบาๆอีกครั้งหนึ่ง"
    en "The girl beside me didn't say much. She just gently patted my head again."
    th "ปกติแล้วเราไม่ชอบให้ใครมาแตะตัวเรา แต่สัมผัสของเธอช่างอบอุ่นจริงๆ"
    en "Normally, I don't like being touched, but her touch was so warm."
    yume_th "บอกแล้วไงว่าอย่าลูบหัวฉัน"
    yume_en "I told you not to pat my head."
    voice "audio/voice/room7/mary_7_020.mp3"
    mary0_th "ไม่ฟังหรอกจ้ะ"
    mary0_en "I won't listen."
    yume_th "หา?"
    yume_en "Huh?"
    voice "audio/voice/room7/mary_7_021.mp3"
    mary0_th "จะห้ามไม่ให้ปลอบใจคนที่ทำหน้าเหมือนจะร้องไห้น่ะ ฉันทำไม่ลงหรอกจ้ะ"
    mary0_en "I can't resist comforting someone who looks like they're about to cry."
    th "เราพูดอะไรไม่ออกแม้แต่คำเดียว"
    en "I was speechless."
    th "รู้ตัวอีกที เราก็เลื่อนตัวเข้าใกล้คนข้างกายและก้มหน้าซุกกับแขนเสื้อเธอแล้ว"
    en "Before I knew it, I moved closer to her and buried my face in her sleeve."
    voice "audio/voice/room7/mary_7_022.mp3"
    mary0_th "น่าจะเป็นฝนตกล่ะนะ"
    mary0_en "Looks like it's going to rain."
    yume_th "ฝน?"
    yume_en "Rain?"
    voice "audio/voice/room7/mary_7_023.mp3"
    mary0_th "เพราะฝนตก แขนเสื้อฉันเลยชื้นไปหมดน่ะ"
    mary0_en "Because of the rain, my sleeve got all wet."
    yume_th "....."
    yume_en "....."
    voice "audio/voice/room7/mary_7_024.mp3"
    mary0_th "ฉันไม่เห็นอะไรทั้งนั้นจ้ะ" 
    mary0_en "I didn’t see anything."
    th "เราได้แต่พยักหน้ารับทั้งๆที่ดวงตาของเราชนกับชายเสื้อของเธอ"
    en "I just nodded, my eyes meeting her sleeve."
    th "ความรู้สึกตื้นตันทะลักทลายอย่างหยุดไม่ได้ สายฝนแห่งความรู้สึกพรั่งพรูออกมา"
    en "A flood of deep emotions surged uncontrollably, a downpour of feelings spilling out."
    voice "audio/voice/room7/mary_7_025.mp3"
    mary0_th "ฉันจะอยู่กับเธอจนกว่าฝนจะหยุดตกเองจ้ะ"
    mary0_en "I'll stay with you until the rain stops."
    yume_th "ขอบคุณนะ"
    yume_en "Thank you."
    voice "audio/voice/room7/mary_7_026.mp3"
    mary0_th "ไม่เป็นไรจ้ะ"
    mary0_en "It's nothing."
    th "สัมผัสอันอ่อนโยนวางประทับเหนือศีรษะของเรา"
    en "A tender touch rested on my head."
    th "อ้อมกอดของเธอทำให้เรารู้สึกไม่ได้อยู่ตัวคนเดียวอีกต่อไป"
    en "Her embrace made me feel I was not alone anymore."

    scene garden_n_1080 with dissolve
    stop music
    play music 泣カナイデ

    yume_th "...อึก"
    yume_en "...Uh"
    th"ทั้งๆที่เราไม่ควรจะมีร่างกาย แต่ความเปียกชื้นที่เกิดขึ้นนี่มันอะไรกันนะ?"
    en "Even though I shouldn't have a body, what is this wetness I'm feeling?"
    th "น้ำตาเหรอ?"
    en "Tears?"
    th "...ทำไมกัน?"
    en "...Why?"
    th "...ทั้งๆที่คนคนนั้นอ่อนโยนกับเราขนาดนั้น ทำไมเราถึงลืมเธอลง?"
    en "...Why did I forget her, despite her kindness towards me?"
    th "...ทำไม?"
    en "...Why?"

    show cat normal with dissolve

    voice "audio/voice/room7/cat_7_008.mp3"
    cat_th lick "ไปต่อกันเถอะจ้ะ"
    cat_en lick "Let's move on."
    yume_th "...เจ้าแมว..."
    yume_en "...You, cat..."
    voice "audio/voice/room7/cat_7_009.mp3"
    cat_th smile  "มาถึงตรงนี้ พวกเราถอยไม่ได้แล้วล่ะจ้ะ"
    cat_en smile "We can't turn back now."
    yume_th "....."
    yume_en "....."
    th "เจ้าแมวพูดถูก"
    en "The cat was right."
    th "ถึงความรู้สึกอึดอัดจะก่อตัวขึ้น ถึงความหมองหม่นจะไม่หายไป แต่ถ้ายังไม่ไปถึงปลายทาง เราก็ไม่รู้ว่าบทสรุปที่แท้จริงคืออะไรกัน"
    en "Despite the suffocating feelings building up, despite the persisting gloom, I wouldn’t know the real ending unless I reached the destination."
    play sound "audio/sfx/dorm-door-opening-6038.mp3" volume 1
    hide cat
    jump cutscene_main

label easteregg_2:
    
    scene white with Dissolve(2)
    th "ขณะที่พวกเราสองคนอ่านหนังสืออยู่ที่ห้องสมุด เธอคนนั้นก็ลุกขึ้นไปหยิบหนังสือบนบันไดพร้อมถามคำถามว่า"
    en "While the two of us were reading books in the library, she got up to grab a book from the stairs and asked,"
    $ persistent.cg_pass[3] = True
    scene library_1080 with Dissolve(3)
    mary_th "นี่เธอรู้รึเปล่าจ๊ะว่ากลุ่มดาวอะไรสามารถดูได้ที่คฤหาสน์นี้ตอนกลางวัน"
    mary_en "Do you know which constellation can be seen from this mansion during the day?"


    yume_th "ดาวเทียม?"
    yume_en "A satellite?"


    mary_th "ใช่ที่ไหนกันเล่า กลุ่มดาวไลบร้าต่างหากจ้ะ"
    mary_en "Not at all. It's the Libra constellation, actually."
    
    yume_th "ไลบร้า?"
    yume_en "Libra?"

    mary_th "ก็ “ไลบร้า”ลี่ ที่หมายถึงห้องสมุดไง ไงล่ะจ้ะ ว่าไปนั่น"
    mary_en "It's 'Library', meaning the library. Get it?"


    th "ตัวฉันที่กำลังจะหันหน้าขึ้นไปต่อว่าเธอที่เล่นมุกไร้สาระนี่บนบันไดก็พบกับกลุ่มดาวอีกดวงที่สามารถเห็นได้ในตอนกลางวัน"
    en "Just as I was about to turn and scold her for her silly joke on the stairs, I found another constellation that can be seen during the day."
    scene piyo with Dissolve(2)

    yume_th "เห…ฉันนึกว่ามีแค่ดาวไลบร้าที่เห็นได้ตอนกลางวัน ไม่คิดว่าจะได้เห็นดาวลูกไก่ด้วย"
    yume_en "Hey! Hold on! Are you peeking at my underwear!!"


    mary_th "นี่!! เดี๋ยวเถอะ!! นี่เธอแอบดูกางเกงในฉันหรอ!!"
    mary_en "Hey! Hold on! Are you peeking at my underwear!!"


    scene garden_n_1080 with Dissolve(3) 
    
    cat_th "ดูจากสีหน้าแล้วเหมือนจะได้เห็นความทรงจำสุดลามกด้วยล่ะ"
    cat_en "Judging by the look on your face, it seems like you've glimpsed some naughty memories as well."

    yume_th "ไม่ใช่เฟ้ย!"
    yume_en "No way!"


    jump answer_room7


    
    
 
    
