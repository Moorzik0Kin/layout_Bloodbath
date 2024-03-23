from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLineEdit, QGroupBox,QButtonGroup,QPushButton, QRadioButton, QMessageBox , QLabel,QHBoxLayout, QVBoxLayout

menu_win = QWidget()
menu_win.resize(400,300)
menu_win.setWindowTitle("Menu")

lbl_question = QLabel("Введіть запитання")
le_question =QLineEdit()

lbl_question1 = QLabel("Введть вірну відповідь")
le_question1 =QLineEdit()

lbl_question2 = QLabel("Ведіть Першу Хибну відповідь")
le_question2 =QLineEdit()

lbl_question3 = QLabel("Ведіть Друга Хибну відповідь")
le_question3 =QLineEdit()

lbl_question4 = QLabel("Ведіть Третя Хибну відповідь")
le_question4 =QLineEdit()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lbl_question)
vl_labels.addWidget(lbl_question1)
vl_labels.addWidget(lbl_question2)
vl_labels.addWidget(lbl_question3)
vl_labels.addWidget(lbl_question4)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_question1)
vl_lineEdits.addWidget(le_question2)
vl_lineEdits.addWidget(le_question3)
vl_lineEdits.addWidget(le_question4)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)
 
btn_add_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("Назад")

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

vl_main = QVBoxLayout()
vl_main.addLayout(hl_question)
vl_main.addLayout(hl_buttons)
vl_main.addWidget(btn_back)

menu_win.setLayout(vl_main)