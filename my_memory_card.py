#import❄️🌨⛄
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel
from random import shuffle

class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3, wrong4, wrong5):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.wrong4 = wrong4
        self.wrong5 = wrong5

question_list = []
question_list.append(Question('Мистер пайтон устроил викторину. Ответь на все вопросы, и он пустит тебя на занятие', 'ладно', 'какой ужас', 'ну уж нет, я иду домой!', 'эмм.. нет', 'никогда', 'может быть'))
question_list.append(Question('На этот год я подготовил сложные вопросы', 'я смогу', 'подумаю', 'в прошлом году было проще', 'к сожалению', 'не люблю новый год', 'а можно завтра?'))
question_list.append(Question('Когда впервые упомянули снеговика?⛄', '1408', '2024', '1322', '1715', '734', '1879'))
question_list.append(Question('Кто придумал гирлянду?', 'Ральф Моррис', 'Никола Тесла', 'Уинстон Черчилль', 'Томас Эдисон', 'Вильгельм II', 'Тодоров Платон'))
question_list.append(Question('Год без лета был в...', '1816', '318', '1928', '23 до нашей эры', '1641', '1272'))
question_list.append(Question('Когда начинается зима в Австралии🌍?', 'в июне', 'в марте', 'в январе', 'в декабре', 'в сентябре', 'в октябре'))
question_list.append(Question('Как звучит "дед мороз" на японском?', 'Одзи-сан', 'Увлин Увгу', 'Юль Томтен', 'Мороз-сан', 'Санта Клаус', 'Муори'))
question_list.append(Question('Как ты оценишь свои результаты', 'отлично', 'хорошо', 'плохо', 'неплохо', 'могу лучше', 'не впечатляющие'))

#основное
app = QApplication([])

window = QWidget()
window2 = QWidget()

#виджеты
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году началась первая мировая война?')
RGB = QGroupBox('')
v3 = QRadioButton('')
v2 = QRadioButton('')
v1 = QRadioButton('')
v4 = QRadioButton('')
v5 = QRadioButton('')
v6 = QRadioButton('')

btn_OK.setStyleSheet("background-color: #00ffff;"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: #00bbbb;"
        "border-radius: 0px")

RGB.setStyleSheet('background-color: #00dddd;' 
                  "border-width: 3px;"
                  "border-color: #0000bb;"
                  "border-radius: 12px")
                  
v1.setStyleSheet('background-color: #ddf0ff;')
v2.setStyleSheet('background-color: #ddf0ff;')
v3.setStyleSheet('background-color: #ddf0ff;')
v4.setStyleSheet('background-color: #ddf0ff;')
v5.setStyleSheet('background-color: #ddf0ff;')
v6.setStyleSheet('background-color: #ddf0ff;')



AGB = QGroupBox('результат')
lb_Result = QLabel('правильные варианты')
lb_Correct = QLabel('ответ тут')



#layout
loans1 = QHBoxLayout()
loans2 = QVBoxLayout()
loans3 = QVBoxLayout()

loans2.addWidget(v1)
loans2.addWidget(v2)
loans2.addWidget(v6)
loans3.addWidget(v3)
loans3.addWidget(v4)
loans3.addWidget(v5)

loans1.addLayout(loans2)
loans1.addLayout(loans3)

RGB.setLayout(loans1)

lol1 = QHBoxLayout() #вопрос
lol2 = QHBoxLayout() #варианты
lol3 = QHBoxLayout() #ответить

lol1.addWidget(lb_Question, alignment=(Qt.AlignCenter | Qt.AlignCenter))
lol2.addWidget(RGB)
lol2.addWidget(AGB)
lol3.addWidget(btn_OK)
AGB.hide()

lr = QVBoxLayout()
lr.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
lr.addWidget(lb_Correct, alignment = Qt.AlignCenter, stretch=1)
AGB.setLayout(lr)

mega_super_giga_boss_layout = QVBoxLayout() #финальный layout‼
mega_super_giga_boss_layout.addLayout(lol1)
mega_super_giga_boss_layout.addLayout(lol2)
mega_super_giga_boss_layout.addLayout(lol3)



def show_result():
    RGB.hide()
    AGB.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RGB.show()
    AGB.hide()
    btn_OK.setText('Ответить')

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

answers = [v1, v2, v3, v4, v5, v6]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answers[4].setText(q.wrong4)
    answers[5].setText(q.wrong5)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        lb_Result.setText("ПРАВИЛЬНО")
        lb_Result.setStyleSheet('background-color: #aaffaa;')
        show_result()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked() or answers[4].isChecked() or answers[5].isChecked() or answers[6].isChecked():
            lb_Result.setText('Ты ошибся')
            lb_Result.setStyleSheet('background-color: #ffaaaa;')

            show_result()

def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if   btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(mega_super_giga_boss_layout)
window.setWindowTitle('Новогодняя викторина')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
next_question()
window.resize(400, 300)
window.show()
app.exec()
