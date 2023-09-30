label intro:
    scene rouka_s_1080
    play music 廃墟洋館
    "... เส้นทางที่ไม่รู้จุดหมายทอดยาวต่อหน้าเรา..."
    "ที่นี่คือที่ไหนกัน?"
    "ตัวเราคือใครกัน?"
    "....."
    "ความมืดมิดโอบล้อมรอบร่างกายจนกระทั่งเราลืมตาตื่นขึ้น"
    "ทัศนะการมองเห็นค่อยๆกลับมาแจ่มชัด"
    "ร่างกายที่รู้สึกหนักหน่วงค่อยๆเบาบางลง"
    "สิ่งแรกที่เราทำหลังจากหยั่งยืนบนพื้นทางเดินอันมืดมนคือจ้องมองแขนขาและเรือนร่างของตัวเอง"


    jump room0

label room0:
    "some text"
    "problem 0"
    show puzzle0
    jump answer_roome0



label answer_roome0:
    menu:
        "answer":
            "try"
            $ input_value = renpy.input("Answer?")
            if input_value == "pathaway":
                "pass"
                hide puzzle0
                jump main_map
            else :
                "it's not answer"
                jump answer_roome0
    
