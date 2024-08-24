from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle('Визначник переможця')
win.move (100, 200)
win.resize(400, 200)

button = QPushButton('згенерувати')
text = QLabel('Натисніть, щоб дізнатися переможця')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
win.setLayout(line)

def print_winner():
    num1 = randint(0, 99)
    winner.setText(str(num1))
    text.setText('Переможець')

button.clicked.connect(print_winner)
win.show()
app.exec_()






