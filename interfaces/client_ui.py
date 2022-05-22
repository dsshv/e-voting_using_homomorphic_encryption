from PyQt5 import QtCore, QtGui, QtWidgets

import lib.server.keygen as keygen
import lib.client.encrypt as encrypt
import lib.server.decrypt as decrypt
import math

PRIME_NUMBER_p = 11460087211
PRIMITIVE_NUMBER_g = 2799360000000
PRIMITIVE_NUMBER_G = 60

server_keys = 'Null'
general_pub_key = 'Null'
cryptograms_matrix = 'Null'
num_of_servers = 2
possible_results_table = 'Null'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        MainWindow.setAcceptDrops(True)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("centralwidget")

        self.label_description = QtWidgets.QLabel(self.central_widget)
        self.label_description.setGeometry(QtCore.QRect(40, 0, 1033, 61))
        self.label_description.setAcceptDrops(True)
        self.label_description.setStyleSheet("background-color: rgb(153, 193, 241);\n"
                                             "\n"
                                             "")
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")

        self.label_margin_left = QtWidgets.QLabel(self.central_widget)
        self.label_margin_left.setGeometry(QtCore.QRect(-10, 0, 51, 841))
        self.label_margin_left.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_margin_left.setText("")
        self.label_margin_left.setObjectName("label_margin_left")

        self.label_generate_keys = QtWidgets.QLabel(self.central_widget)
        self.label_generate_keys.setGeometry(QtCore.QRect(40, 90, 1031, 71))
        self.label_generate_keys.setStyleSheet("\n"
                                               "background-color: rgb(153, 193, 241);")
        self.label_generate_keys.setObjectName("label_generate_keys")

        self.pushButton_generate_keys = QtWidgets.QPushButton(self.central_widget)
        self.pushButton_generate_keys.setGeometry(QtCore.QRect(790, 100, 161, 41))
        self.pushButton_generate_keys.setObjectName("pushButton_generate_keys")

        self.textBrowser_keys = QtWidgets.QTextBrowser(self.central_widget)
        self.textBrowser_keys.setGeometry(QtCore.QRect(40, 160, 911, 91))
        self.textBrowser_keys.setObjectName("textBrowser_keys")

        self.label_num_of_servers = QtWidgets.QLabel(self.central_widget)
        self.label_num_of_servers.setGeometry(QtCore.QRect(40, 60, 1031, 51))
        self.label_num_of_servers.setStyleSheet("background-color: rgb(153, 193, 241);\n"
                                                "\n"
                                                "")
        self.label_num_of_servers.setObjectName("label_num_of_servers")

        self.pushButton_general_key = QtWidgets.QPushButton(self.central_widget)
        self.pushButton_general_key.setGeometry(QtCore.QRect(790, 260, 161, 41))
        self.pushButton_general_key.setObjectName("pushButton_general_key")
        self.pushButton_general_key.setEnabled(False)

        self.label_general_pub_key = QtWidgets.QLabel(self.central_widget)
        self.label_general_pub_key.setGeometry(QtCore.QRect(40, 250, 1031, 61))
        self.label_general_pub_key.setStyleSheet("\n"
                                                 "background-color: rgb(153, 193, 241);")
        self.label_general_pub_key.setObjectName("label_general_pub_key")

        self.textBrowser_general_key = QtWidgets.QTextBrowser(self.central_widget)
        self.textBrowser_general_key.setGeometry(QtCore.QRect(40, 310, 911, 61))
        self.textBrowser_general_key.setObjectName("textBrowser_general_key")

        self.pushButton_encrypt = QtWidgets.QPushButton(self.central_widget)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(790, 380, 161, 41))
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.pushButton_encrypt.setEnabled(False)

        self.label_encrypt_votes = QtWidgets.QLabel(self.central_widget)
        self.label_encrypt_votes.setGeometry(QtCore.QRect(40, 370, 621, 61))
        self.label_encrypt_votes.setAcceptDrops(True)
        self.label_encrypt_votes.setStyleSheet("\n"
                                               "background-color: rgb(153, 193, 241);")
        self.label_encrypt_votes.setWordWrap(True)
        self.label_encrypt_votes.setObjectName("label_encrypt_votes")

        self.textBrowser_cryptograms = QtWidgets.QTextBrowser(self.central_widget)
        self.textBrowser_cryptograms.setGeometry(QtCore.QRect(40, 430, 911, 121))
        self.textBrowser_cryptograms.setObjectName("textBrowser_cryptograms")

        self.label_encr_vores_right = QtWidgets.QLabel(self.central_widget)
        self.label_encr_vores_right.setGeometry(QtCore.QRect(430, 370, 591, 61))
        self.label_encr_vores_right.setAcceptDrops(True)
        self.label_encr_vores_right.setStyleSheet("\n"
                                                  "background-color: rgb(153, 193, 241);")
        self.label_encr_vores_right.setText("")
        self.label_encr_vores_right.setWordWrap(True)
        self.label_encr_vores_right.setObjectName("label_encr_vores_right")

        self.pushButton_decrypt = QtWidgets.QPushButton(self.central_widget)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(790, 560, 161, 41))
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        self.pushButton_decrypt.setEnabled(False)

        self.label_decrypt_votes = QtWidgets.QLabel(self.central_widget)
        self.label_decrypt_votes.setGeometry(QtCore.QRect(40, 550, 1031, 71))
        self.label_decrypt_votes.setStyleSheet("\n"
                                               "background-color: rgb(153, 193, 241);")
        self.label_decrypt_votes.setObjectName("label_decrypt_votes")

        self.textBrowser_decrypt_votes = QtWidgets.QTextBrowser(self.central_widget)
        self.textBrowser_decrypt_votes.setGeometry(QtCore.QRect(40, 610, 911, 141))
        self.textBrowser_decrypt_votes.setObjectName("textBrowser_decrypt_votes")

        self.label_vote_result = QtWidgets.QLabel(self.central_widget)
        self.label_vote_result.setGeometry(QtCore.QRect(40, 750, 1031, 51))
        self.label_vote_result.setStyleSheet("\n"
                                             "background-color: rgb(153, 193, 241);")
        self.label_vote_result.setObjectName("label_vote_result")
        self.label_margin_right = QtWidgets.QLabel(self.central_widget)
        self.label_margin_right.setGeometry(QtCore.QRect(950, 0, 51, 841))
        self.label_margin_right.setAcceptDrops(True)
        self.label_margin_right.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_margin_right.setText("")
        self.label_margin_right.setObjectName("label_margin_right")

        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 60, 151, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.label_description.raise_()
        self.label_margin_left.raise_()
        self.label_generate_keys.raise_()
        self.label_num_of_servers.raise_()
        self.label_general_pub_key.raise_()
        self.label_encr_vores_right.raise_()
        self.label_decrypt_votes.raise_()
        self.label_vote_result.raise_()
        self.label_margin_right.raise_()
        self.textBrowser_keys.raise_()
        self.textBrowser_general_key.raise_()
        self.textBrowser_cryptograms.raise_()
        self.textBrowser_decrypt_votes.raise_()
        self.pushButton_generate_keys.raise_()
        self.pushButton_encrypt.raise_()
        self.pushButton_general_key.raise_()
        self.pushButton_decrypt.raise_()
        self.label_encrypt_votes.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # add functions
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Демонстрация работы распределенного дешифрования"))
        self.label_description.setText(_translate("MainWindow",
                                                  "Программа, использующая принципы гомоморфного шифрования с "
                                                  "распределенным дешифрованием"))
        self.label_generate_keys.setText(
            _translate("MainWindow", "Нажмите чтобы сгенерировать случайные числа и открытые ключи: "))
        self.pushButton_generate_keys.setText(_translate("MainWindow", "Генерировать"))
        self.textBrowser_keys.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                 "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                 "type=\"text/css\">\n "
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Cantarell\'; "
                                                 "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                 "margin-right:0px; -qt-block-indent:0; "
                                                 "text-indent:0px;\">Сгенерированы следующие ключи "
                                                 "серверов:</p></body></html>"))
        self.label_num_of_servers.setText(_translate("MainWindow", "Количество серверов:"))
        self.pushButton_general_key.setText(_translate("MainWindow", "Генерировать"))
        self.label_general_pub_key.setText(_translate("MainWindow", "Нажмите, чтобы сгенерировать общий ключ:"))
        self.textBrowser_general_key.setHtml(_translate("MainWindow",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                        "type=\"text/css\">\n "
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'Cantarell\'; "
                                                        "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">Общий публичный ключ h:</p>\n "
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                        "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                        "-qt-block-indent:0; text-indent:0px;\"><br "
                                                        "/></p></body></html>"))
        self.pushButton_encrypt.setText(_translate("MainWindow", "Зашифровать"))
        self.label_encrypt_votes.setText(_translate("MainWindow",
                                                    "<html><head/><body><p>Нажмите, чтобы зашифровать голоса "
                                                    "избирателей: <br/>(Голоса находятся в файле "
                                                    "votes.txt)</p></body></html>"))
        self.textBrowser_cryptograms.setHtml(_translate("MainWindow",
                                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                        "type=\"text/css\">\n "
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'Cantarell\'; "
                                                        "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                        "text-indent:0px;\">Сгенерированы следующие "
                                                        "криптограммы:</p>\n "
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                        "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                        "-qt-block-indent:0; text-indent:0px;\"><br "
                                                        "/></p></body></html>"))
        self.pushButton_decrypt.setText(_translate("MainWindow", "Расшифровать"))
        self.label_decrypt_votes.setText(_translate("MainWindow", "Нажмите, чтобы расшифровать голоса:"))
        self.textBrowser_decrypt_votes.setHtml(_translate("MainWindow",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                          "/><style type=\"text/css\">\n "
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'Cantarell\'; "
                                                          "font-size:11pt; font-weight:400; font-style:normal;\">\n "
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                          "text-indent:0px;\">Процесс дешифрования:</p>\n "
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                          "-qt-block-indent:0; text-indent:0px;\"><br "
                                                          "/></p></body></html>"))
        self.label_vote_result.setText(_translate("MainWindow", "Итоги голосования:"))
        self.lineEdit.setText(_translate("MainWindow", "2"))

    # functions to client

    def add_functions(self):
        self.pushButton_generate_keys.clicked.connect(lambda: self.button_generate_keys_func(
            int(self.lineEdit.text())
        ))
        self.pushButton_general_key.clicked.connect(lambda: self.button_general_key())
        self.pushButton_encrypt.clicked.connect(lambda: self.button_encrypt())
        self.pushButton_decrypt.clicked.connect(lambda: self.button_decrypt())

    def button_generate_keys_func(self, count_of_servers: int):
        global num_of_servers
        global server_keys
        num_of_servers = count_of_servers
        server_keys = keygen.init_servers_keys(num_of_servers, PRIME_NUMBER_p, PRIMITIVE_NUMBER_g)
        text_keys: str = 'Сгенерированы следующие ключи серверов:'
        for i in range(len(server_keys)):
            text_keys += f'\nСервер №{i + 1}: {server_keys[i].return_key()}'

        self.textBrowser_keys.setText(text_keys)
        self.textBrowser_general_key.setText('Общий публичный ключ h:')
        self.textBrowser_cryptograms.setText('Сгенерированы следующие криптограммы: ')
        self.textBrowser_decrypt_votes.setText('Процесс дешифрования: ')

        self.pushButton_general_key.setEnabled(True)
        self.pushButton_encrypt.setEnabled(False)
        self.pushButton_decrypt.setEnabled(False)

    def button_general_key(self):
        global general_pub_key
        general_pub_key = keygen.general_open_key(server_keys, PRIME_NUMBER_p)
        text_general_pub_key: str = f'Общий публичный ключ h: {general_pub_key}'

        self.textBrowser_general_key.setText(text_general_pub_key)
        self.textBrowser_cryptograms.setText('Сгенерированы следующие криптограммы: ')
        self.textBrowser_decrypt_votes.setText('Процесс дешифрования: ')

        self.pushButton_encrypt.setEnabled(True)
        self.pushButton_decrypt.setEnabled(False)

    def button_encrypt(self):
        global possible_results_table
        global cryptograms_matrix
        cryptograms_matrix = encrypt.auto_encrypt(
            PRIME_NUMBER_p, PRIMITIVE_NUMBER_g, PRIMITIVE_NUMBER_G, general_pub_key
        )
        cryptograms = open('cryptograms.txt', 'r')
        text_cryptograms: str = 'Сгенерированы следующие криптограммы:\n'
        while True:
            line = cryptograms.readline()
            if not line:
                break
            text_cryptograms += line
        cryptograms.close()

        self.textBrowser_cryptograms.setText(text_cryptograms)
        self.textBrowser_decrypt_votes.setText('Процесс дешифрования: ')

        possible_results_table = encrypt.possible_results(PRIME_NUMBER_p, PRIMITIVE_NUMBER_G)
        self.pushButton_decrypt.setEnabled(True)

    def button_decrypt(self):
        part_matrix = decrypt.all_servers_partial(PRIME_NUMBER_p, num_of_servers, server_keys, cryptograms_matrix)
        full_x = decrypt.compute_full_x(PRIME_NUMBER_p, part_matrix)
        full_y = decrypt.compute_full_y(PRIME_NUMBER_p, cryptograms_matrix)
        votes_sum_log = decrypt.compute_votes_sum(PRIME_NUMBER_p, full_x, full_y, PRIMITIVE_NUMBER_G)
        print(votes_sum_log)

        vote_ratio = 0
        for i in range(len(possible_results_table)):
            if possible_results_table[i][1] == votes_sum_log:
                print(possible_results_table[i][2])
                vote_ratio = possible_results_table[i][2]
                break

        out_text = str(vote_ratio) + '\n'
        out_text += 'Выполненная на серверах частичная расшифровка:\n'
        for i in range(len(part_matrix)):
            for j in range(len(part_matrix[i])):
                out_text += f'W[{j + 1}][{i + 1}] = {part_matrix[i][j]}; '
            out_text += '\n'
        out_text += f'Вычисленный полный X: {full_x}\n' \
                    f'Вычисленный полный Y: {full_y}\nlog(G)G^sum(votes) = {votes_sum_log}'
        self.textBrowser_decrypt_votes.setText(out_text)
