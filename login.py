# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from library import Ui_MainWindow

class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 337)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"font: 75 18pt \"Segoe UI\";")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 381, 41))
        self.label_2.setStyleSheet("font: 75 22pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(135, 75, 311, 51))
        self.label_3.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.username_2 = QtWidgets.QLineEdit(Form)
        self.username_2.setGeometry(QtCore.QRect(140, 80, 301, 41))
        self.username_2.setObjectName("username_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(134, 145, 311, 51))
        self.label_4.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.username_3 = QtWidgets.QLineEdit(Form)
        self.username_3.setGeometry(QtCore.QRect(140, 150, 301, 41))
        self.username_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username_3.setObjectName("username_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(214, 290, 181, 31))
        self.label.setStyleSheet("font: 75 12pt \"Tw Cen MT Condensed\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.loginuser)   
        
    def showRest(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def MessageBox(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def loginuser(self):
        
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        
        mycursor = conn.cursor()
        username = self.username_2.text()
        password = self.username_3.text()
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()

        for row in myresult:
            if username == row[1] and password == row[3]:
                style = open('themes/qdark.css' , 'r')
                style = style.read()
                app.setStyleSheet(style)
                self.MessageBox('Login', 'Login Successfully')
                self.showRest()
                MainWindow.close()
            else:
                pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "NH LIBRARY MANAGMENT"))
        self.username_2.setToolTip(_translate("Form", "<html><head/><body><p>Enter Username</p></body></html>"))
        self.username_2.setPlaceholderText(_translate("Form", "Enter User Name"))
        self.username_3.setToolTip(_translate("Form", "<html><head/><body><p>Enter Password</p></body></html>"))
        self.username_3.setPlaceholderText(_translate("Form", "Enter Password"))
        self.label.setText(_translate("Form", "DESIGNED BY DR OMOH"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

