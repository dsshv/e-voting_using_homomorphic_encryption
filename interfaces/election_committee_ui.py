from PyQt5 import QtCore, QtGui, QtWidgets
import election_committee.ik_script as ik

count_of_voters = sum(1 for line in open('cryptograms.txt', 'r'))
count_of_keys = sum(1 for l in open('open_keys.txt', 'r'))

PRIME_NUMBER_p = 11460087211
PRIMITIVE_NUMBER_g = 2799360000000
PRIMITIVE_NUMBER_G = 60


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
        self.label_cryptograms = QtWidgets.QLabel(self.centralwidget)
        self.label_cryptograms.setGeometry(QtCore.QRect(60, 70, 901, 71))
        self.label_cryptograms.setAcceptDrops(True)
        self.label_cryptograms.setStyleSheet("\n"
                                             "background-color: rgb(222, 221, 218);")
        self.label_cryptograms.setWordWrap(True)
        self.label_cryptograms.setObjectName("label_cryptograms")
        self.textBrowser_cryptograms = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_cryptograms.setGeometry(QtCore.QRect(610, 90, 211, 31))
        self.textBrowser_cryptograms.setObjectName("textBrowser_cryptograms")
        self.label_compute = QtWidgets.QLabel(self.centralwidget)
        self.label_compute.setGeometry(QtCore.QRect(60, 210, 901, 131))
        self.label_compute.setAcceptDrops(True)
        self.label_compute.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_compute.setAlignment(QtCore.Qt.AlignCenter)
        self.label_compute.setWordWrap(True)
        self.label_compute.setObjectName("label_compute")
        self.label_decrypted = QtWidgets.QLabel(self.centralwidget)
        self.label_decrypted.setGeometry(QtCore.QRect(60, 340, 900, 151))
        self.label_decrypted.setAcceptDrops(True)
        self.label_decrypted.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_decrypted.setAlignment(QtCore.Qt.AlignCenter)
        self.label_decrypted.setWordWrap(True)
        self.label_decrypted.setObjectName("label_decrypted")
        self.pushButton_send_yes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send_yes.setGeometry(QtCore.QRect(410, 310, 201, 61))
        self.pushButton_send_yes.setObjectName("pushButton_send_yes")
        self.label_results = QtWidgets.QLabel(self.centralwidget)
        self.label_results.setGeometry(QtCore.QRect(60, 490, 900, 271))
        self.label_results.setAcceptDrops(True)
        self.label_results.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_results.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_results.setWordWrap(True)
        self.label_results.setObjectName("label_results")
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
        self.textBrowser_keys = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_keys.setGeometry(QtCore.QRect(610, 160, 211, 31))
        self.textBrowser_keys.setObjectName("textBrowser_keys")
        self.label_keys = QtWidgets.QLabel(self.centralwidget)
        self.label_keys.setGeometry(QtCore.QRect(60, 140, 901, 71))
        self.label_keys.setAcceptDrops(True)
        self.label_keys.setStyleSheet("\n"
                                      "background-color: rgb(222, 221, 218);")
        self.label_keys.setWordWrap(True)
        self.label_keys.setObjectName("label_keys")
        self.textBrowser_results = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_results.setGeometry(QtCore.QRect(80, 530, 861, 211))
        self.textBrowser_results.setObjectName("textBrowser_results")
        self.label_bottom.raise_()
        self.label_left.raise_()
        self.label_wellcome.raise_()
        self.label_cryptograms.raise_()
        self.textBrowser_cryptograms.raise_()
        self.label_results.raise_()
        self.label_compute.raise_()
        self.label_keys.raise_()
        self.textBrowser_keys.raise_()
        self.label_decrypted.raise_()
        self.textBrowser_results.raise_()
        self.pushButton_send_yes.raise_()
        self.label_right.raise_()
        Evote_server.setCentralWidget(self.centralwidget)

        self.retranslateUi(Evote_server)
        QtCore.QMetaObject.connectSlotsByName(Evote_server)

        self.add_functions()

    def retranslateUi(self, Evote_server):
        _translate = QtCore.QCoreApplication.translate
        Evote_server.setWindowTitle(_translate("Evote_server", "E-vote Comission Panel v0.1"))

        self.label_wellcome.setText(_translate("Evote_server",
                                               "Добро пожаловать! Вы находитесь в приложении для голосования "
                                               "избирательной комиссии. Электронное голосование происходит на основе "
                                               "гомоморфной криптосистемы с распределенным дешифрованием"))

        self.label_cryptograms.setText(
            _translate("Evote_server", "   Считывание криптограмм произошло успешно. Количество избирателей:"))

        self.textBrowser_cryptograms.setHtml(_translate("Evote_server",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                        "type=\"text/css\">\n "
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'Cantarell\'; "
                                                        "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\"></p></body></html>"))
        self.textBrowser_cryptograms.setText(str(count_of_voters))

        self.label_compute.setText(_translate("Evote_server", "Нажмите для вычисления результатов голосования:"))

        self.label_decrypted.setText(_translate("Evote_server", ""))

        self.pushButton_send_yes.setText(_translate("Evote_server", "Расшифровать"))

        self.label_results.setText(_translate("Evote_server", "Результаты голосования:"))

        self.textBrowser_keys.setHtml(_translate("Evote_server",
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
        self.textBrowser_keys.setText(str(count_of_keys))

        self.label_keys.setText(
            _translate("Evote_server", "   Считывание ключей серверов произошло успешно. Количество пар ключей:"))

        self.textBrowser_results.setHtml(_translate("Evote_server",
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

    def add_functions(self):
        self.pushButton_send_yes.clicked.connect(lambda: self.button_decrypt())

    def button_decrypt(self):
        parts_matrix = ik.get_parts()
        cryptograms_matrix = ik.get_cryptograms()
        possible_results = ik.possible_results(PRIME_NUMBER_p, PRIMITIVE_NUMBER_G)
        full_x = ik.compute_full_x(PRIME_NUMBER_p, parts_matrix)
        full_y = ik.compute_full_y(PRIME_NUMBER_p, cryptograms_matrix)
        votes_sum_log = ik.compute_votes_sum(PRIME_NUMBER_p, full_x, full_y, PRIMITIVE_NUMBER_G)
        print(votes_sum_log)

        vote_ratio = 0
        for i in range(len(possible_results)):
            if possible_results[i][1] == votes_sum_log:
                print(possible_results[i][2])
                vote_ratio = possible_results[i][2]
                break

        out_text = str(vote_ratio) + '\n'
        out_text += 'Выполненная на серверах частичная расшифровка:\n'
        for i in range(len(parts_matrix)):
            for j in range(len(parts_matrix[i])):
                out_text += f'W[{j + 1}][{i + 1}] = {parts_matrix[i][j]}; '
            out_text += '\n'
        out_text += f'Вычисленный полный X: {full_x}\n' \
                    f'Вычисленный полный Y: {full_y}\nlog(G)G^sum(votes) = {votes_sum_log}'
        self.textBrowser_results.setText(out_text)


def ik_main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evote_server = QtWidgets.QMainWindow()
    ui = Ui_Evote_server()
    ui.setupUi(Evote_server)
    Evote_server.show()
    sys.exit(app.exec_())
