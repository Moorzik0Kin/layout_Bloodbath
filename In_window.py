from PyQt5.QtCore import*
from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QVBoxLayout, QRadioButton, QButtonGroup

win=QWidget()
win.resize(400, 200)
# Memory Cart
win.setWindowTitle("Приємного страдання!")

btn_menu=QPushButton("Меню")

rb_ans1=QRadioButton()
rb_ans2=QRadioButton()
rb_ans3=QRadioButton()
rb_ans4=QRadioButton()

group=QButtonGroup()
group.addButton(rb_ans1)
group.addButton(rb_ans2)
group.addButton(rb_ans3)
group.addButton(rb_ans4)

lb_question=QLabel("Запитання")
lb_result=QLabel()
lb_right_result=QLabel("Правила відповідь")

gb_ques=QGroupBox("Варіанти відповідей")
rb_v1=QVBoxLayout()
rb_v2=QVBoxLayout()
rb_h1=QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)

gb_ques.setLayout(rb_h1)

gb_ans=QGroupBox()
v_10000010001_10000111011_10001001111=QVBoxLayout()
v_10000010001_10000111011_10001001111.addWidget(lb_result)
v_10000010001_10000111011_10001001111.addWidget(lb_right_result)
gb_ans.setLayout(v_10000010001_10000111011_10001001111)

btn_ans=QPushButton("Відповісти")

in_window=QVBoxLayout()
in_window.addWidget(btn_menu)
in_window.addWidget(lb_question, alignment=Qt.AlignCenter)
in_window.addWidget(gb_ques)
in_window.addWidget(gb_ans)
gb_ans.hide()
in_window.addWidget(btn_ans)

win.setLayout(in_window)
win.show()