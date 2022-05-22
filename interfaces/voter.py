from PyQt5 import QtCore, QtGui, QtWidgets
import client.client_script as cli
import sys

keys = cli.got_keys('open_keys.txt')
mod = int(keys[0][2])
g = int(keys[0][1])
PRIMITIVE_NUMBER_G = 60
keys_count = len(keys)
general_h = cli.general_open_key(keys, mod)
question = 'Добавить сахар во все кружки чая?'
current_vote = 'null'


class Ui_Evote_server(object):

    def setupUi(self, Evote_server):
        Evote_server.setObjectName("Evote_server")
        Evote_server.resize(1000, 800)
        Evote_server.setMinimumSize(QtCore.QSize(1000, 800))
        Evote_server.setMaximumSize(QtCore.QSize(1000, 800))

        self.centralwidget = QtWidgets.QWidget(Evote_server)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget.setObjectName("centralwidget")

        self.label_wellcome = QtWidgets.QLabel(self.centralwidget)
        self.label_wellcome.setGeometry(QtCore.QRect(60, 0, 900, 71))
        self.label_wellcome.setAcceptDrops(True)
        self.label_wellcome.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.label_wellcome.setWordWrap(True)
        self.label_wellcome.setObjectName("label_wellcome")

        self.label_keys_num = QtWidgets.QLabel(self.centralwidget)
        self.label_keys_num.setGeometry(QtCore.QRect(60, 70, 901, 71))
        self.label_keys_num.setAcceptDrops(True)
        self.label_keys_num.setStyleSheet("\n"
                                          "background-color: rgb(222, 221, 218);")
        self.label_keys_num.setWordWrap(True)
        self.label_keys_num.setObjectName("label_keys_num")

        self.textBrowser_keys_num = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_keys_num.setGeometry(QtCore.QRect(610, 90, 211, 31))
        self.textBrowser_keys_num.setObjectName("textBrowser_keys_num")

        self.label_question = QtWidgets.QLabel(self.centralwidget)
        self.label_question.setGeometry(QtCore.QRect(60, 140, 900, 71))
        self.label_question.setAcceptDrops(True)
        self.label_question.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_question.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_question.setWordWrap(True)
        self.label_question.setObjectName("label_question")

        self.label_vote = QtWidgets.QLabel(self.centralwidget)
        self.label_vote.setGeometry(QtCore.QRect(60, 280, 901, 111))
        self.label_vote.setAcceptDrops(True)
        self.label_vote.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_vote.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vote.setWordWrap(True)
        self.label_vote.setObjectName("label_vote")

        self.textBrowser_question = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_question.setGeometry(QtCore.QRect(70, 200, 871, 101))
        self.textBrowser_question.setObjectName("textBrowser_question")

        self.label_question_down = QtWidgets.QLabel(self.centralwidget)
        self.label_question_down.setGeometry(QtCore.QRect(60, 210, 900, 111))
        self.label_question_down.setAcceptDrops(True)
        self.label_question_down.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_question_down.setFrameShape(QtWidgets.QFrame.Box)
        self.label_question_down.setLineWidth(0)
        self.label_question_down.setText("")
        self.label_question_down.setWordWrap(True)
        self.label_question_down.setObjectName("label_question_down")

        self.label_yes = QtWidgets.QLabel(self.centralwidget)
        self.label_yes.setGeometry(QtCore.QRect(60, 390, 451, 101))
        self.label_yes.setAcceptDrops(True)
        self.label_yes.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_yes.setText("")
        self.label_yes.setWordWrap(True)
        self.label_yes.setObjectName("label_yes")

        self.label_send_open = QtWidgets.QLabel(self.centralwidget)
        self.label_send_open.setGeometry(QtCore.QRect(60, 490, 900, 91))
        self.label_send_open.setAcceptDrops(True)
        self.label_send_open.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_send_open.setAlignment(QtCore.Qt.AlignCenter)
        self.label_send_open.setWordWrap(True)
        self.label_send_open.setObjectName("label_send_open")

        self.pushButton_send_yes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send_yes.setGeometry(QtCore.QRect(170, 400, 201, 61))
        self.pushButton_send_yes.setObjectName("pushButton_send_yes")

        self.label_send = QtWidgets.QLabel(self.centralwidget)
        self.label_send.setGeometry(QtCore.QRect(60, 580, 900, 91))
        self.label_send.setAcceptDrops(True)
        self.label_send.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_send.setWordWrap(True)
        self.label_send.setObjectName("label_send")

        self.label_bottom = QtWidgets.QLabel(self.centralwidget)
        self.label_bottom.setGeometry(QtCore.QRect(60, 650, 900, 171))
        self.label_bottom.setAcceptDrops(True)
        self.label_bottom.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.label_bottom.setText("")
        self.label_bottom.setWordWrap(True)
        self.label_bottom.setObjectName("label_bottom")

        self.label_left = QtWidgets.QLabel(self.centralwidget)
        self.label_left.setGeometry(QtCore.QRect(-20, 0, 81, 811))
        self.label_left.setAcceptDrops(True)
        self.label_left.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.label_left.setText("")
        self.label_left.setWordWrap(True)
        self.label_left.setObjectName("label_left")

        self.label_right = QtWidgets.QLabel(self.centralwidget)
        self.label_right.setGeometry(QtCore.QRect(960, 0, 71, 811))
        self.label_right.setAcceptDrops(True)
        self.label_right.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.label_right.setText("")
        self.label_right.setWordWrap(True)
        self.label_right.setObjectName("label_right")

        self.pushButton_send_no = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send_no.setGeometry(QtCore.QRect(620, 400, 201, 61))
        self.pushButton_send_no.setObjectName("pushButton_send_no")

        self.label_no = QtWidgets.QLabel(self.centralwidget)
        self.label_no.setGeometry(QtCore.QRect(510, 390, 451, 101))
        self.label_no.setAcceptDrops(True)
        self.label_no.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_no.setText("")
        self.label_no.setWordWrap(True)
        self.label_no.setObjectName("label_no")

        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(790, 600, 151, 51))
        self.pushButton_send.setObjectName("pushButton_send")

        self.label_send_sucsessfull = QtWidgets.QLabel(self.centralwidget)
        self.label_send_sucsessfull.setGeometry(QtCore.QRect(60, 670, 900, 81))
        self.label_send_sucsessfull.setAcceptDrops(True)
        self.label_send_sucsessfull.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_send_sucsessfull.setWordWrap(True)
        self.label_send_sucsessfull.setObjectName("label_send_sucsessfull")

        self.label_bottom.raise_()
        self.label_left.raise_()
        self.label_wellcome.raise_()
        self.label_keys_num.raise_()
        self.textBrowser_keys_num.raise_()
        self.label_question.raise_()
        self.label_question_down.raise_()
        self.label_send.raise_()
        self.label_send_open.raise_()
        self.label_yes.raise_()
        self.label_vote.raise_()
        self.textBrowser_question.raise_()
        self.pushButton_send_yes.raise_()
        self.label_right.raise_()
        self.label_no.raise_()
        self.pushButton_send_no.raise_()
        self.pushButton_send.raise_()
        self.label_send_sucsessfull.raise_()
        Evote_server.setCentralWidget(self.centralwidget)

        self.retranslateUi(Evote_server)
        QtCore.QMetaObject.connectSlotsByName(Evote_server)

        self.add_functions()

    def retranslateUi(self, Evote_server):
        _translate = QtCore.QCoreApplication.translate
        Evote_server.setWindowTitle(_translate("Evote_server", "E-vote Client v0.2"))

        self.label_wellcome.setText(_translate("Evote_server", "Добро пожаловать! Вы находитесь в приложении для "
                                                               "голосования избирателя. Электронное голосование "
                                                               "происходит на основе гомоморфной криптосистемы с "
                                                               "распределенным дешифрованием"))

        self.label_keys_num.setText(_translate("Evote_server", "  Считывание открытых ключей произошло успешно. "
                                                               "Количество ключей:"))

        self.textBrowser_keys_num.setHtml(_translate("Evote_server", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML "
                                                                     "4.0//EN\" "
                                                                     "\"http://www.w3.org/TR/REC-html40/strict.dtd"
                                                                     "\">\n "
                                                                     "<html><head><meta name=\"qrichtext\" "
                                                                     "content=\"1\" /><style type=\"text/css\">\n "
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "</style></head><body style=\" "
                                                                     "font-family:\'Cantarell\'; font-size:11pt; "
                                                                     "font-weight:400; font-style:normal;\">\n "
                                                                     "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                                     "margin-left:0px; margin-right:0px; "
                                                                     "-qt-block-indent:0; "
                                                                     f"text-indent:0px;\"></p></body"
                                                                     f"></html>"))
        self.textBrowser_keys_num.setText(str(keys_count))

        self.label_question.setText(_translate("Evote_server", "Идет голосование по вопросу:"))

        self.label_vote.setText(_translate("Evote_server", "Ваш голос:"))

        self.textBrowser_question.setHtml(_translate("Evote_server",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                     "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                     "type=\"text/css\">\n "
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Cantarell\'; "
                                                     "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                     "margin-right:0px; -qt-block-indent:0; "
                                                     "text-indent:0px;\">123</p></body></html>"))
        self.textBrowser_question.setText(question)

        self.label_send_open.setText(_translate("Evote_server", "Ваш голос: \"ЗА\""))

        self.pushButton_send_yes.setText(_translate("Evote_server", "За"))

        self.label_send.setText(_translate("Evote_server", "   Нажмите для отправки вашего голоса:"))

        self.pushButton_send_no.setText(_translate("Evote_server", "Против"))

        self.pushButton_send.setText(_translate("Evote_server", "Отправить"))
        self.pushButton_send.setEnabled(False)

        self.label_send_sucsessfull.setText(_translate("Evote_server", ""))

    def add_functions(self):
        self.pushButton_send_yes.clicked.connect(lambda: self.button_vote_yes())
        self.pushButton_send_no.clicked.connect(lambda: self.button_vote_no())
        self.pushButton_send.clicked.connect(lambda: self.send_cryptogram())

    def button_vote_yes(self):
        self.pushButton_send.setEnabled(False)
        vote = 1
        global current_vote
        current_vote = cli.EncryptedMessage(int(general_h), int(g), int(mod), int(PRIMITIVE_NUMBER_G), int(vote))
        self.label_send_open.setText(str('Ваш голос: "ЗА"'))
        print('voter said yes!')
        self.pushButton_send.setEnabled(True)
        return current_vote

    def button_vote_no(self):
        self.pushButton_send.setEnabled(False)
        vote = -1
        global current_vote
        current_vote = cli.EncryptedMessage(int(general_h), int(g), int(mod), int(PRIMITIVE_NUMBER_G), int(vote))
        self.label_send_open.setText(str('Ваш голос: "ПРОТИВ"'))
        print('voter said no...')
        self.pushButton_send.setEnabled(True)
        return current_vote

    def send_cryptogram(self):
        cryptograms = open('cryptograms.txt', 'a')
        self.label_send_sucsessfull.setText("  Ваш голос успешно отправлен!")
        encrypted_vote = current_vote.return_encrypted_message()
        cryptograms.write(str(encrypted_vote)+'\n')
        cryptograms.close()

def voter_main():
    cryptograms = open('cryptograms.txt', 'w')
    cryptograms.close()
    app = QtWidgets.QApplication(sys.argv)
    e_vote_server = QtWidgets.QMainWindow()
    ui = Ui_Evote_server()
    ui.setupUi(e_vote_server)
    e_vote_server.show()
    sys.exit(app.exec_())
