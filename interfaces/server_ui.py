from PyQt5 import QtCore, QtGui, QtWidgets

import server.server_script as srv

PRIME_NUMBER_p = 11460087211
PRIMITIVE_NUMBER_g = 2799360000000
PRIMITIVE_NUMBER_G = 60
key = 'Null'
secret_keys = []
parts_stack = 'Null'

class Ui_Evote_server(object):
    def setupUi(self, Evote_server):
        Evote_server.setObjectName("Evote_server")
        Evote_server.resize(1000, 800)
        Evote_server.setMinimumSize(QtCore.QSize(1000, 800))
        Evote_server.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(Evote_server)
        self.centralwidget.setObjectName("centralwidget")
        self.label_wellcome = QtWidgets.QLabel(self.centralwidget)
        self.label_wellcome.setGeometry(QtCore.QRect(60, 0, 900, 71))
        self.label_wellcome.setAcceptDrops(True)
        self.label_wellcome.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.label_wellcome.setWordWrap(True)
        self.label_wellcome.setObjectName("label_wellcome")

        self.label_num_p = QtWidgets.QLabel(self.centralwidget)
        self.label_num_p.setGeometry(QtCore.QRect(60, 70, 300, 71))
        self.label_num_p.setAcceptDrops(True)
        self.label_num_p.setStyleSheet("\n"
                                       "background-color: rgb(222, 221, 218);")
        self.label_num_p.setWordWrap(True)
        self.label_num_p.setObjectName("label_num_p")

        self.textBrowser_num_p = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_num_p.setGeometry(QtCore.QRect(140, 90, 211, 31))
        self.textBrowser_num_p.setObjectName("textBrowser_num_p")

        self.label_num_g = QtWidgets.QLabel(self.centralwidget)
        self.label_num_g.setGeometry(QtCore.QRect(360, 70, 300, 71))
        self.label_num_g.setAcceptDrops(True)
        self.label_num_g.setStyleSheet("\n"
                                       "background-color: rgb(222, 221, 218);")
        self.label_num_g.setWordWrap(True)
        self.label_num_g.setObjectName("label_num_g")

        self.textBrowser_num_g = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_num_g.setGeometry(QtCore.QRect(440, 90, 211, 31))
        self.textBrowser_num_g.setObjectName("textBrowser_num_g")

        self.label_num_G = QtWidgets.QLabel(self.centralwidget)
        self.label_num_G.setGeometry(QtCore.QRect(660, 70, 300, 71))
        self.label_num_G.setAcceptDrops(True)
        self.label_num_G.setStyleSheet("\n"
                                       "background-color: rgb(222, 221, 218);")
        self.label_num_G.setWordWrap(True)
        self.label_num_G.setObjectName("label_num_G")

        self.textBrowser_num_G = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_num_G.setGeometry(QtCore.QRect(740, 90, 211, 31))
        self.textBrowser_num_G.setObjectName("textBrowser_num_G")

        self.label_keygen = QtWidgets.QLabel(self.centralwidget)
        self.label_keygen.setGeometry(QtCore.QRect(60, 140, 900, 71))
        self.label_keygen.setAcceptDrops(True)
        self.label_keygen.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_keygen.setWordWrap(True)
        self.label_keygen.setObjectName("label_keygen")

        self.pushButton_keygen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_keygen.setGeometry(QtCore.QRect(780, 150, 161, 41))
        self.pushButton_keygen.setObjectName("pushButton_keygen")

        self.label_openkey = QtWidgets.QLabel(self.centralwidget)
        self.label_openkey.setGeometry(QtCore.QRect(60, 280, 450, 161))
        self.label_openkey.setAcceptDrops(True)
        self.label_openkey.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_openkey.setWordWrap(True)
        self.label_openkey.setObjectName("label_openkey")

        self.textBrowser_open = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_open.setGeometry(QtCore.QRect(90, 390, 351, 101))
        self.textBrowser_open.setObjectName("textBrowser_open")

        self.label_close_key = QtWidgets.QLabel(self.centralwidget)
        self.label_close_key.setGeometry(QtCore.QRect(510, 280, 450, 161))
        self.label_close_key.setAcceptDrops(True)
        self.label_close_key.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_close_key.setWordWrap(True)
        self.label_close_key.setObjectName("label_closekey")

        self.textBrowser_close = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_close.setGeometry(QtCore.QRect(540, 390, 351, 101))
        self.textBrowser_close.setObjectName("textBrowser_close")

        self.label_keygen_sucsessfull = QtWidgets.QLabel(self.centralwidget)
        self.label_keygen_sucsessfull.setGeometry(QtCore.QRect(60, 210, 900, 71))
        self.label_keygen_sucsessfull.setAcceptDrops(True)
        self.label_keygen_sucsessfull.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_keygen_sucsessfull.setFrameShape(QtWidgets.QFrame.Box)
        self.label_keygen_sucsessfull.setLineWidth(0)
        self.label_keygen_sucsessfull.setWordWrap(True)
        self.label_keygen_sucsessfull.setObjectName("label_keygen_sucsessfull")

        self.label_browsersback = QtWidgets.QLabel(self.centralwidget)
        self.label_browsersback.setGeometry(QtCore.QRect(60, 440, 900, 71))
        self.label_browsersback.setAcceptDrops(True)
        self.label_browsersback.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_browsersback.setText("")
        self.label_browsersback.setWordWrap(True)
        self.label_browsersback.setObjectName("label_browsersback")

        self.label_send_open = QtWidgets.QLabel(self.centralwidget)
        self.label_send_open.setGeometry(QtCore.QRect(60, 510, 900, 71))
        self.label_send_open.setAcceptDrops(True)
        self.label_send_open.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_send_open.setWordWrap(True)
        self.label_send_open.setObjectName("label_send_open")

        self.pushButton_send_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send_open.setGeometry(QtCore.QRect(780, 520, 161, 41))
        self.pushButton_send_open.setObjectName("pushButton_send_open")

        self.label_send_close = QtWidgets.QLabel(self.centralwidget)
        self.label_send_close.setGeometry(QtCore.QRect(60, 580, 900, 181))
        self.label_send_close.setAcceptDrops(True)
        self.label_send_close.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_send_close.setWordWrap(True)
        self.label_send_close.setObjectName("label_send_close")

        self.pushButton_send_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send_close.setGeometry(QtCore.QRect(780, 650, 161, 41))
        self.pushButton_send_close.setObjectName("pushButton_send_close")

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
        self.label_right.setGeometry(QtCore.QRect(950, 0, 81, 811))
        self.label_right.setAcceptDrops(True)
        self.label_right.setStyleSheet("background-color: rgb(255, 190, 111);")
        self.label_right.setText("")
        self.label_right.setWordWrap(True)
        self.label_right.setObjectName("label_right")

        self.label_bottom.raise_()
        self.label_left.raise_()
        self.label_right.raise_()
        self.label_wellcome.raise_()
        self.label_num_g.raise_()
        self.label_num_G.raise_()
        self.label_num_p.raise_()
        self.textBrowser_num_p.raise_()
        self.textBrowser_num_g.raise_()
        self.textBrowser_num_G.raise_()
        self.label_keygen.raise_()
        self.label_keygen_sucsessfull.raise_()
        self.label_send_close.raise_()
        self.pushButton_send_close.raise_()
        self.label_send_open.raise_()
        self.label_close_key.raise_()
        self.label_browsersback.raise_()
        self.label_openkey.raise_()
        self.textBrowser_open.raise_()
        self.textBrowser_close.raise_()
        self.pushButton_keygen.raise_()
        self.pushButton_send_open.raise_()
        Evote_server.setCentralWidget(self.centralwidget)

        self.retranslateUi(Evote_server)
        QtCore.QMetaObject.connectSlotsByName(Evote_server)

        self.add_functions()

    def retranslateUi(self, Evote_server):
        _translate = QtCore.QCoreApplication.translate
        Evote_server.setWindowTitle(_translate("Evote_server", "E-vote Server v0.1"))
        self.label_wellcome.setText(_translate("Evote_server",
                                               "Добро пожаловать! Вы находитесь в приложении для генерации ключей на "
                                               "Сервере. Электронное голосование происходит на основе гомоморфной "
                                               "криптосистемы с распределенным дешифрованием"))
        self.label_num_p.setText(_translate("Evote_server", "  Число p = "))

        self.textBrowser_num_p.setHtml(_translate("Evote_server",
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
        self.textBrowser_num_p.setText(str(PRIME_NUMBER_p))

        self.label_num_g.setText(_translate("Evote_server", "Число g = "))

        self.textBrowser_num_g.setHtml(_translate("Evote_server",
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
        self.textBrowser_num_g.setText(str(PRIMITIVE_NUMBER_g))

        self.label_num_G.setText(_translate("Evote_server", "Число G = "))

        self.textBrowser_num_G.setHtml(_translate("Evote_server",
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
        self.textBrowser_num_G.setText(str(PRIMITIVE_NUMBER_G))

        self.label_keygen.setText(_translate("Evote_server", "   Нажмите для генерации пары открытый/закрытый ключ:"))

        self.pushButton_keygen.setText(_translate("Evote_server", "Генерировать"))

        self.label_openkey.setText(_translate("Evote_server", "   Сгенерирован следующий открытый ключ:"))

        self.textBrowser_open.setHtml(_translate("Evote_server",
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
        self.textBrowser_open.setText("")

        self.label_close_key.setText(_translate("Evote_server", "   Сгенерирован следующий закрытый ключ:"))

        self.textBrowser_close.setHtml(_translate("Evote_server",
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
        self.textBrowser_close.setText("")

        self.label_keygen_sucsessfull.setText(_translate("Evote_server", "   Генерация ключа успешно завершена!"))

        self.label_send_open.setText(_translate("Evote_server", "   Нажмите для отправки открытого ключа:"))

        self.pushButton_send_open.setText(_translate("Evote_server", "Отправить"))

        self.label_send_close.setText(_translate("Evote_server", "   Нажмите для отправки закрытого ключа:"))

        self.pushButton_send_close.setText(_translate("Evote_server", "Отправить"))

    def add_functions(self):
        self.pushButton_keygen.clicked.connect(lambda: self.button_generate())
        self.pushButton_send_open.clicked.connect(lambda: self.send_key())
        self.pushButton_send_close.clicked.connect(lambda: self.send_secret_keys())

    def button_generate(self):
        global key
        key = srv.init_server_key(PRIME_NUMBER_p, PRIMITIVE_NUMBER_g)
        self.textBrowser_open.setText(str(key.return_key()))
        self.textBrowser_close.setText(str(key.random_num_s))

    def send_key(self):
        global key
        key.send_open_keys()
        self.label_send_open.setText("  Нажмите для отправки открытого ключа:\n"
                                     f"  Успешно отправлен ключ: {str(key.return_key())}")
        self.label_send_close.setText("  Нажмите для отправки закрытого ключа: "
                                      f"{str(key.random_num_s)}")

    def send_secret_keys(self):
        global parts_stack
        parts_stack = srv.all_servers_partial(PRIME_NUMBER_p)
        print('succesfull compute W')
        srv.send_close_keys()
        self.label_send_close.setText("  Нажмите для отправки закрытого ключа: "
                                      f"{str(key.random_num_s)}\n"
                                      "  Успешно отправлено!\n"
                                      "  Частичные расшифровки выполнены!")

