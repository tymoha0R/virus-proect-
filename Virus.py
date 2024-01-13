# не работает в визуал студио

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle('Заява киллеру ')
window.resize(400,500)

label = QLabel('имя,фамилия,возраст,полит. важность(например= президент, бомж, офисній работник, и тд.)')
text1 = QTextEdit("континент,в какой стране, месность,город")
text2 = QTextEdit()
ne= QLineEdit()


v= QVBoxLayout()
h= QHBoxLayout()
v.addWidget(text1)
h.addWidget(text2)
v.addWidget(label)
v.addWidget(ne)

r1 = QRadioButton("много охрані")
r2 = QRadioButton("охрана есть")
r3 = QRadioButton("нет/мало охрані")
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h1.addWidget(r1)
h1.addWidget(r2)
h1.addWidget(r3)
h4=QHBoxLayout()
ch1=QCheckBox("есть брат?")
ch2=QCheckBox("есть семья?")
ch3=QCheckBox("есть любовн-ик/-ца")
h2.addWidget(ch1)
h2.addWidget(ch2)
h2.addWidget(ch3)
rozglist= QComboBox()
rozglist.addItems(['богатій','средне богатій','в достатке данег','в недостатке денег','бомж',"кризис но деньги есть"])
h1.addWidget(rozglist)      
b1= QPushButton('начать')
h4.addWidget(b1)
v.addLayout(h1)
v.addLayout(h2)
v.addLayout(h3)
v.addLayout(h4)
window.setLayout(v)

def olleh():
    global index
    info_win=QMessageBox()
    info_win.setWindowTitle('o holero, chito fredi fasber(результ.)')
    info_win.setText('заполнено, информация отправлена киллеру \n' +ne.text())
    info_win.exec_()

def sus():
    global index
    virus=QMessageBox()
    virus.setWindowTitle('скачать вірус(;?')
    virus.setText('скачай ка вирус по братски а?')
    virus.exec_()
def konez():
    ha=QMessageBox()
    ha.setWindowTitle("так легко не уйдешь!!!")
    ha.setText("а хотя все равно(O\ _ /O)")
    ha.exec_()

def aaaaa():
    v1=QMessageBox()
    v1.setWindowTitle('ВІРУС')
    v1.setText("СПАААААААААААААААААААААААААМ!!!!!!!!!!!!!!")
    v2=QMessageBox()
    v2.setWindowTitle('ВІРУС')
    v2.setText("СПАААААААААААААААААААААААААМ!!!!!!!!!!!!!!")
    v3=QMessageBox()
    v3.setWindowTitle('ВІРУС')
    v3.setText("СПАААААААААААААААААААААААААМ!!!!!!!!!!!!!!")
    v1.exec_()
    v2.exec_()
    v3.exec_()













b1.clicked.connect(sus)
b1.clicked.connect(olleh)
b1.clicked.connect(konez)
b1.clicked.connect(aaaaa)
window.show()
app.exec()
