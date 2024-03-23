from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])
from In_window import*
from menu_dining_room import*

class Question():
    def __init__(self,question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question=question
        self.right_answer=right_answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3

questions=[
    Question("А,Б,В чи Г:","А","Б","В","Г"),
    Question("ЯКОЇ ТИ НАЦІЇ:","ЄВРЕЙ","ДА","НІМЕЦЬ","ТУРОК ННІМЕЦЬКИЙ"),
    Question("Ти капібара:","Можливо","ДА","НЄ","₴!№;?"),
    Question("Cos A прямокутного трикутнику це:","Прилегла пряма поділити на Гіпотенузою","Прилегла пряма поділити на Протилежну пряму","Протилежну пряму поділити на Гіпотенузу","Ало Дядя я у 1 класі")


]

Radio_Button=[rb_ans1,rb_ans2,rb_ans3,rb_ans4]

def new_question():
    qwa=choice(questions)
    lb_question.setText(qwa.question)
    lb_right_result.setText(qwa.right_answer)
    Radio_Button[0].setText(qwa.right_answer)
    Radio_Button[1].setText(qwa.wrong_answer1)
    Radio_Button[2].setText(qwa.wrong_answer2)
    Radio_Button[3].setText(qwa.wrong_answer3)
    shuffle(Radio_Button)

new_question()

def click_ok():
    if btn_ans.text()=="Відповісти":
        group.setExclusive(False)
        for AAAAAA_RASTREL in Radio_Button:
            if AAAAAA_RASTREL.isChecked():
                if AAAAAA_RASTREL.text()==lb_right_result.text():
                    lb_result.setText("Правильно!")
                else:
                    lb_result.setText("Неправильно!")
                break
        group.setExclusive(True)
        gb_ques.hide()
        gb_ans.show()
        btn_ans.setText("Наступне завдання")
    else:
        new_question()
        gb_ans.hide()
        gb_ques.show()
        btn_ans.setText("Відповісти")

btn_ans.clicked.connect(click_ok)

def in_negr():
    win.hide()
    menu_win.show()

btn_menu.clicked.connect(in_negr)

def clear():
    le_question.clear()
    le_question1.clear()
    le_question2.clear()
    le_question3.clear()
    le_question4.clear()

btn_clear.clicked.connect(clear)

def add_f():
    new_question=Question(le_question.text(),le_question1.text(),le_question2.text(),le_question3.text(),le_question4.text())
    questions.append(new_question)
    clear()

btn_add_question.clicked.connect(add_f)

app.exec_()