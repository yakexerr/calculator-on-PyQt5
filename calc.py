from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Windows = uic.loadUiType('calk.ui')
win = QApplication([])
windows = Windows()
form = Form()
form.setupUi(windows)

flag = False


def digit(dig):
    if not (form.rezult.text()): form.rezult.setText('0')

    if form.rezult.text()[-1] in "+-*/" and dig == ",": form.rezult.setText(form.rezult.text() + '0')
    if form.rezult.text() == "0" and dig != ",": form.rezult.clear()
    if 'Ошибка' in form.rezult.text(): form.rezult.setText('0')
    global flag
    if dig in "+-*/":
        flag = False
        if form.rezult.text()[-1] in "+-*/":
            form.rezult.setText(form.rezult.text()[:-1])

    if flag:
        form.rezult.clear()
        flag = False
    if not (form.rezult.text()) and dig == ",": form.rezult.setText('0')
    form.rezult.setText(form.rezult.text() + dig)


def coma():
    ''' надо узнать позицию последнего арифметического знака'''
    znac = [form.rezult.text().rfind(i) for i in '+-*/']
    pos = max(znac)
    if form.rezult.text()[pos] == "-":
        form.rezult.setText(form.rezult.text()[:pos] + '+' + form.rezult.text()[pos + 1:])
    else:
        form.rezult.setText(form.rezult.text()[:pos + 1] + '-' + form.rezult.text()[pos + 1:])


def rezult():
    try:
        global flag
        flag = True
        form.rezult.setText(str(eval(form.rezult.text().replace(",", '.'))).replace(".", ','))
    except ZeroDivisionError:
        form.rezult.setText("Ошибка!!! Деление на 0")

    except Exception as er:
        form.rezult.setText("Ошибка!!! " + str(er))


form.key0.clicked.connect(lambda: digit("0"))
form.key1.clicked.connect(lambda: digit(form.key1.text()))
form.key2.clicked.connect(lambda: digit(form.key2.text()))
form.key3.clicked.connect(lambda: digit(form.key3.text()))
form.key4.clicked.connect(lambda: digit(form.key4.text()))
form.key5.clicked.connect(lambda: digit(form.key5.text()))
form.key6.clicked.connect(lambda: digit(form.key6.text()))
form.key7.clicked.connect(lambda: digit(form.key7.text()))
form.key8.clicked.connect(lambda: digit(form.key8.text()))
form.key9.clicked.connect(lambda: digit(form.key9.text()))

form.keyPlus.clicked.connect(lambda: digit(form.keyPlus.text()))
form.keyMinus.clicked.connect(lambda: digit('-'))
form.keyDel.clicked.connect(lambda: digit('/'))
form.keyUm.clicked.connect(lambda: digit("*"))
form.keyComa.clicked.connect(lambda: digit(','))
form.keyPlusMinus.clicked.connect(coma)
form.keyBack.clicked.connect(lambda: form.rezult.setText(form.rezult.text()[:-1]))
form.keyRezult.clicked.connect(rezult)
form.keyUm_3.clicked.connect(lambda: form.rezult.setText('0'))
windows.show()
win.exec()
