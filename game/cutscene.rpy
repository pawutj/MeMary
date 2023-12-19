label cutscene_main:
    if ((room01_is_pass == True)  + (room02_is_pass == True) + (room03_is_pass == True) ) == 1:
        jump cutscene_2

    if ( (room01_is_pass == True)  + (room02_is_pass == True) + (room03_is_pass == True) + (room04_is_pass == True) + (room05_is_pass == True) + (room06_is_pass == True) + (room07_is_pass == True) + (room08_is_pass == True) ) == 3 :
        jump cutscene_0
    if ( (room01_is_pass == True)  + (room02_is_pass == True) + (room03_is_pass == True) + (room04_is_pass == True) + (room05_is_pass == True) + (room06_is_pass == True)  + (room07_is_pass == True) + (room08_is_pass == True)) == 6 :
        jump cutscene_1

    if ( (room07_is_pass == True) + (room08_is_pass == True) == 2  ):
        jump cutscene_3
    jump main_map
label cutscene_2:
    scene hall_n_1080 with dissolve
    "เสียงปลดล็อกงั้นหรอ หรือว่ามีห้องถูกปลดล็อกเพิ่มกันนะ"
    show cat normal with dissolve
    ##voice "audio/voice/cutscene/cat_13_000.mp3"
    cat lick "อยากรู้ก็ลองไปดูสิ"
    hide cat
    "มีประตูเปิดเพิ่มอีก 3 บาน"
    jump main_map

label cutscene_3:
    scene hall_n_1080 with dissolve
    yume "ตอนนี้ผ่านมานานเท่าไหร่แล้วนะ"

    show cat normal with dissolve
    ##voice "audio/voice/cutscene/cat_13_001.mp3"
    cat smile "ช้าหรือเร็ว อยู่กับว่าเธอไขปริศนาได้เร็วแค่ไหน"
    ##voice "audio/voice/cutscene/cat_13_002.mp3"
    cat ah "ถ้ารู้สึกว่านาน แสดงว่าเธอไขปริศนาได้ช้ารึเปล่า"
    ##voice "audio/voice/cutscene/cat_13_003.mp3"
    cat lick "แต่ถ้าเธอรู้สึกว่าเร็วเกินไป ฉันว่า เธอแอบเปิดโพยรึเปล่า?"
    "..."

    ##voice "audio/voice/cutscene/cat_13_004.mp3"
    cat ah "เหลืออีกไม่กี่ห้องก็จบแล้วสินะ หลังจากที่เราแยกกัน เธออาจจะคิดถึงฉันก็ได้ \n"
    ##voice "audio/voice/cutscene/cat_13_005.mp3"
    cat lick "ฉันจะอนุญาติให้เธอลูบหัวเป็นกรณีพิเศษก็ได้"

    yume "ไม่ล่ะ ขอบใจ"

    #sfx click
    ##voice "audio/voice/cutscene/cat_13_006.mp3"
    cat normal "ดูเหมือนห้องจะปลดล็อกเพิ่มขึ้นอีกแล้วสินะ"
    yume "รีบทำให้มันจบลงดีกว่า"
    "ความจริงอยู่แค่เอื้อมแล้ว"
    jump main_map

label cutscene_0:
    scene hall_n_1080 with dissolve
    play music 星が輝く冬
    th "เรากับเจ้าแมวส้มเดินกลับมายังห้องโถงที่ถูกรายล้อมด้วยประตูมากมาย"
    en "The orange cat and I walked back to the hall, surrounded by numerous doors."

    th "ก่อนที่จะเดินเข้าห้องต่อไป จู่ๆเจ้าแมวส้มก็หันมาคุยกับเรา"
    en "Before entering the next room, the cat suddenly turned to talk to me."

    show cat normal with dissolve
    ##voice "audio/voice/cutscene/cat_13_007.mp3"
    cat_th normal "ฉันรู้นะว่าเธอจ้องสังเกตฉันอยู่"
    cat_en normal "I know you've been watching me."

    th "ความเงียบเป็นของเรา พร้อมกับความสงสัยที่ผุดพรายขึ้นในใจ"
    en "Silence enveloped us, along with a rising curiosity in my heart."

    th "ระหว่างที่เรากำลังสับสน เจ้าแมวส้มก็ค่อยๆเดินใกล้เข้ามาและเงยหน้ามองเราด้วยดวงตาคู่โต"
    en "As I stood perplexed, the orange cat slowly approached and looked up at me with its large eyes."

    ##voice "audio/voice/cutscene/cat_13_008.mp3"
    cat_th lick "ฉันเข้าใจเธอนะ"
    cat_en lick "I understand you."

    yume_th "เข้าใจ?"
    yume_en "Understand?"


    ##voice "audio/voice/cutscene/cat_13_009.mp3"
    cat_th normal "ไม่แปลกหรอกที่เธอจะสงสัยฉัน ลองคิดดูสิว่าจู่ๆเธอต้องมาทำปริศนาอะไรไม่รู้ แถมยังมีแมวลึกลับมาต่อล้อต่อเถียงกับเธออีกต่างหาก"
    cat_en normal "It's not strange that you're suspicious of me. Think about it: suddenly you're solving puzzles and arguing with a mysterious cat."
    
    yume_th "...."
    yume_en "...."

    ##voice "audio/voice/cutscene/cat_13_010.mp3"
    cat_th lick "เอางี้ไหม? เพื่อให้เธอไว้ใจฉันมากขึ้น ฉันจะตอบคำถามเธอสักข้อสองข้อ"
    cat_en lick "How about this? To gain your trust, I'll answer one or two of your questions."


    yume_th "ฉันสามารถถามอะไรก็ได้อย่างงั้นเหรอ?"
    yume_en "Can I ask anything?"

    th "คำถามของเราทำให้เจ้าแมวส้มหรี่ตาลงน้อยๆ"
    en "My question made the orange cat narrow its eyes slightly."


    th "มันหุบยิ้มลงชั่วขณะ หลังจากนั้นรอยยิ้มของมันก็ปรากฏบนใบหน้าตามเดิม"
    en "It momentarily ceased smiling, but soon its grin returned."

    ##voice "audio/voice/cutscene/cat_13_011.mp3"
    cat_th smile "ถ้าฉันตอบได้ ฉันจะตอบเธอก็แล้วกัน"  
    cat_en smile "If I can answer, I will."

    yume_th "แล้วถ้าตอบไม่ได้ล่ะ?"
    yume_en "And if you can't?"

    ##voice "audio/voice/cutscene/cat_13_012.mp3"
    cat_th lick "ก็คงทำหน้ามึนๆใส่เธอแล้วเดินหนีด้านๆล่ะมั้ง"
    cat_en lick "I'll probably just give you a blank look and sneak away."

    th "เราพูดไม่ออกกับความตรงไปตรงมาของสัตว์ตัวน้อย"
    en "I was speechless at the creature's frankness."

    th "จะว่าเจ้าแมวส้มนี่ขี้เล่นหรือซื่อสัตย์แบบแปลกๆดีนะ?"
    en "Should I consider the orange cat playful or oddly honest?"

    yume_th "ถ้าฉันถามว่าฉันเป็นใคร..."
    yume_en "If I ask who I am..."

    ##voice "audio/voice/cutscene/cat_13_013.mp3"
    cat_th ah "ลองดูสิ แล้วเธอจะเห็นฉันหันก้นวิ่งหนีเธอจ้ะ"
    cat_en ah "Try it, and you'll see me turn and run away."

    yume_th "..........."
    yume_en "..........."

    th "เราเงียบเป็นเป่าสากเมื่อเห็นหน้าเนือยๆของผู้ตอบคำถาม"
    en "I fell silent upon seeing the nonchalant face of my respondent."

    th "ถ้าตอบเรื่องที่สำคัญที่สุดไม่ได้แล้วมันจะมีความหมายอะไรกัน"
    en "What's the point if it can't answer the most crucial question?"

    ##voice "audio/voice/cutscene/cat_13_014.mp3"
    cat_th lick "ผู้ไขปริศนาที่ดีต้องไม่ถามเฉลยตรงๆนะ ไม่งั้นจะมีปริศนาไว้ทำไมล่ะ"
    cat_en lick "A good puzzle solver shouldn't ask for the solution outright. Otherwise, what's the point of the puzzle?"

    th "มันพูดอีกก็ถูกอีก แต่ท่าทางยียวนผสมเจ้าเล่ห์ของมันทำให้เราไม่สบอารมณ์ยังไงก็ไม่รู้"
    en "The cat was right again, but its smug and cunning demeanor somehow irritated me."

    th "น่าเสียดายที่เราไม่มีร่างกาย ถ้าเรามีเราคงเอาเท้าเขี่ยๆพุงเจ้าแมวสักทีแล้ว"
    en "It's a pity I don't have a physical body; if I did, I'd probably nudge the cat's belly with my foot."

    ##voice "audio/voice/cutscene/cat_13_015.mp3"
    cat_th smile "อึ๊ย..."
    cat_en smile "Oops..."

    yume_th "หา?"
    yume_en "Huh?"

    ##voice "audio/voice/cutscene/cat_13_016.mp3"
    cat_th smile "นี่ฉันคิดไปเองหรือเปล่าว่าเธอแอบปล่อยแรงกดดันใส่ฉัน"
    cat_en smile "Or am I just imagining that you're exerting some kind of pressure on me?"
    
    yume_th "แรงกดดัน?"
    yume_en "Pressure?"

    ##voice "audio/voice/cutscene/cat_13_017.mp3"
    cat_th ah "ไม่มีอะไรจ้ะ แค่ฉันจะบอกว่าสายตาเธอดูทิ่มแทงฉันผิดปกติเฉยๆ"
    cat_en ah "Nothing. Just saying your gaze seems unusually piercing."

    yume_th "...เหรอ...?"
    yume_en "...Really..."

    ##voice "audio/voice/cutscene/cat_13_018.mp3"
    cat_th  smile "ก็นั่นสินะจ้ะ"
    cat_en smile "That's right."

    th "เจ้าแมวส้มพูดทิ้งท้ายไว้เท่านั้นแล้วมันก็ค่อยๆเดินนำหน้าเราทีละก้าวๆ"
    en "The orange cat concluded and began to lead the way again, step by step."

    th "บทสนทนาระหว่างเรากับแมวสิ้นสุดลงแค่นั้น ทิ้งไว้ซึ่งความรู้สึกแปลกๆข้างในใจราวกับความจริงบางอย่างไม่กลมกลืนกัน"
    en "That was the end of our conversation, leaving behind a strange feeling in my heart, as if something wasn't quite right."
    
    th "...ทำไม?"
    en "...Why?"
    hide cat with dissolve
    jump main_map

label cutscene_1:
    play music 星が輝く冬
    scene hall_n_1080 with dissolve
    yume "ก่อนเข้าห้องต่อไป ฉันมีอะไรจะถามแกสักหน่อย"
    "คำเรียกของเราทำให้เจ้าแมวส้มหันหน้ามามองเราด้วยความฉงน"
    "ดวงตาคู่โตของมันเบิกกว้างขึ้นเล็กน้อยทำให้น่าเอ็นดูขึ้น"
    show cat lick with dissolve
    ##voice "audio/voice/cutscene/cat_13_019.mp3"
    cat lick "ถามมาก็ตอบได้จ้ะ"
    yume "ถ้างั้นฉันขอถามว่า..."
    ##voice "audio/voice/cutscene/cat_13_020.mp3"
    cat ah "แต่ห้ามถามว่าเธอเป็นใครนะจ้ะ บอกไว้ก่อน"
    yume ".............."
    "เราถูกขัดคอล่วงหน้าราวกับเจ้าแมวเดาคำพูดของเราได้"
    "ดวงตากลมโตของมันมองเราด้วยความเจนจัดราวกับคนถือไพ่เหนือกว่า"
    ##voice "audio/voice/cutscene/cat_13_021.mp3"
    cat lick "แหม...เมื่อกี้จะขอถามเฉลยตรงๆเลยใช่ไหมล่ะ?"
    yume "แกคิดไปเอง"
    "เราพยายามบ่ายเบี่ยงเพราะไม่อยากเสียเชิงแมวส้ม"
    "อย่างไรก็ตาม เจ้าแมวดูไม่ลดละที่จะไล่ต้อนเรา"
    yume "...!!!"
    ##voice "audio/voice/cutscene/cat_13_022.mp3"
    cat ah "เธอหลอกสายตาอันเฉียบคมของฉันไม่ได้หรอกนะ!!!"
    "เจ้าแมวส้มยื่นหน้าพุ่งใส่เราอย่างไม่ทันตั้งตัว"
    "เราผงะจนถอยหลังเล็กน้อย แต่เจ้าแมวก็ยังไล่กวดตามมาเหมือนจับหนู"
    yume "เฮ้ย จะใกล้เกินไปแล้วนะ"
    ##voice "audio/voice/cutscene/cat_13_023.mp3"
    cat lick "ฉันดูออกนะ"
    yume "จะดูออกหรือดูไม่ออกก็ช่างมันเถอะ ออกไปห่างๆฉันก่อน"
    ##voice "audio/voice/cutscene/cat_13_024.mp3"
    cat smile "ฮะๆๆ ก็ได้ๆ"
    "เจ้าแมวส้มหัวเราะร่วนสักพักก่อนที่มันจะกระโดดห่างจากเราสองสามก้าว"
    ##voice "audio/voice/cutscene/cat_13_025.mp3"
    cat lick "เธอนี่นิสัยไม่ดีเหมือนเดิมเลยนะ คนไขปริศนาที่ไหนเค้าแอบหาเฉลยอ่านกัน"
    yume "ถ้าโจทย์มันยากเกินไป ใครๆเค้าก็หาโพยทั้งนั้นแหละ"
    "แมวส้มทำตาโตใส่เราพลางส่งเสียงถอนใจ"
    "นี่เราคิดไปเองหรือเปล่าว่าเจ้าแมวตัวนี้กวนประสาทแปลกๆ"
    ##voice "audio/voice/cutscene/cat_13_026.mp3"
    cat normal "เธอพูดไม่ผิดแหละ แต่ความสนุกของปริศนามาจากความยากและความท้าทาย ไม่ใช่ความง่ายระดับใครๆก็ตอบได้หรอก"
    yume "อะไรๆก็ง่ายทั้งนั้นแหละถ้ามีโพยให้อ่าน"
    "คำตอบของเราทำให้เจ้าแมวทำแก้มป่อง"
    "ดวงตาคู่โตของเจ้าแมวมองเราอย่างไม่พอใจ"
    ##voice "audio/voice/cutscene/cat_13_027.mp3"
    cat lick "หนึ่งคำก็โพย สองคำก็โพย ตอนเธอเรียนหนังสือนี่คงลอกการบ้านคนอื่นทุกวันเลยล่ะสิ ไม่ไหวๆ"
    "เจ้าแมวส่งเสียงเยาะเย้ยเรา"
    "ความรู้สึกหงุดหงิดผุดพรายขึ้นมาในใจเราอย่างควบคุมไม่ได้"
    yume "ฉันต่างหากล่ะที่ทำงานให้คนอื่นลอก!"
    ##voice "audio/voice/cutscene/cat_13_028.mp3"
    cat smile "เหรอ?"
    yume "...อึก"
    "เมื่อกี้มันอะไร? "
    "จู่ๆเราก็พูดขึ้นมาทั้งๆที่เราไม่ได้อยากพูด"
    "เราตอบสนองต่อคำพูดคนอื่นโดยที่ไม่รู้ตัวอย่างงั้นเหรอ?"
    "นี่มันแปลกชะมัด"
    ##voice "audio/voice/cutscene/cat_13_029.mp3"
    cat smile "เธอเริ่มจะกลับมาเป็นตัวของตัวเองแล้วนะ"
    yume "หา?"
    ##voice "audio/voice/cutscene/cat_13_030.mp3"
    cat normal "เดี๋ยวเธอก็เข้าใจเอง "
    "เจ้าแมวทิ้งท้ายไว้เท่านั้นก่อนที่มันจะนำทางเราไปยังห้องแห่งปริศนาต่อไป"
    #sfx 
    ##voice "audio/voice/cutscene/cat_13_031.mp3"
    cat ah "ดูเหมือนจะมีห้องที่ถูกปลดล็อกเพิ่มขึ้นแล้วนะ"
    ##voice "audio/voice/cutscene/cat_13_032.mp3"
    cat normal "รีบไปสิ อยากรู้ความจริงไม่ใช่เหรอ"
    hide cat
    jump main_map
   


