screen show_cg01_01():
    key "mouseup_3" action Hide("show_cg01_01",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_01",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_02",Dissolve(0.1)),Hide("show_cg01_01")]
    add "cg/fb1.png"


screen show_cg01_02():
    key "mouseup_3" action Hide("show_cg01_02",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_02",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_03",Dissolve(0.1)),Hide("show_cg01_02")]
    add "cg/fb2.png"

screen show_cg01_03():
    key "mouseup_3" action Hide("show_cg01_03",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_03",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_04",Dissolve(0.1)),Hide("show_cg01_03")]
    add "cg/fb3_0.png"

screen show_cg01_04():
    key "mouseup_3" action Hide("show_cg01_04",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_04",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_05",Dissolve(0.1)),Hide("show_cg01_04")]
    add "cg/fb3_3.png"


screen show_cg01_05():
    key "mouseup_3" action Hide("show_cg01_05",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_05",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_06",Dissolve(0.1)),Hide("show_cg01_05")]
    add "cg/fb3_6.png"

screen show_cg01_06():
    key "mouseup_3" action Hide("show_cg01_06",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_06",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_07",Dissolve(0.1)),Hide("show_cg01_06")]
    add "cg/fb3_9.png"

screen show_cg01_07():
    key "mouseup_3" action Hide("show_cg01_07",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_07",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_08",Dissolve(0.1)),Hide("show_cg01_07")]
    add "cg/fb3_12.png"

screen show_cg01_08():
    key "mouseup_3" action Hide("show_cg01_08",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_08",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg01_09",Dissolve(0.1)),Hide("show_cg01_08")]
    add "cg/fb3_15.png"

screen show_cg01_09():
    key "mouseup_3" action Hide("show_cg01_09",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg01_09",Dissolve(0.1))
    key "mouseup_1" action Hide("show_cg01_09",Dissolve(0.1))
    add "cg/fb3_18.png"

screen show_cg02_01():
    key "mouseup_3" action Hide("show_cg02_01",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg02_01",Dissolve(0.1))
    key "mouseup_1" action [Show("show_cg02_02",Dissolve(0.1)),Hide("show_cg02_01")]
    add "cg/bakuhatu1.jpeg"


screen show_cg02_02():
    key "mouseup_3" action Hide("show_cg02_02",Dissolve(0.1))
    key "K_ESCAPE" action Hide("show_cg02_02",Dissolve(0.1))
    key "mouseup_1" action Hide("show_cg02_02",Dissolve(0.1))
    add "cg/bakuhatu2.jpg"