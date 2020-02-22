# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from xlrd import *
from xlsxwriter import *
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 71, 61))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/today.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 120, 71, 61))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 270, 71, 71))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/flat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 350, 71, 71))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 430, 71, 71))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/themes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(140, 0, 1031, 551))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 120, 1011, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(780, 40, 113, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 191, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(490, 40, 91, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(650, 40, 83, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(441, 45, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(600, 46, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_29.setGeometry(QtCore.QRect(230, 40, 191, 41))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab)
        self.pushButton_29.setGeometry(QtCore.QRect(630, 460, 371, 41))
        self.pushButton_29.setObjectName("pushButton_29")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1021, 511))
        self.tabWidget_2.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_10)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 1011, 421))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setStyleSheet("font: 9pt \"Segoe UI\";")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(7)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_27.setGeometry(QtCore.QRect(630, 422, 371, 41))
        self.pushButton_27.setObjectName("pushButton_27")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 60, 281, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(690, 60, 291, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_3.setGeometry(QtCore.QRect(690, 130, 291, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_4.setGeometry(QtCore.QRect(690, 190, 291, 41))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_5.setGeometry(QtCore.QRect(690, 240, 291, 41))
        self.comboBox_5.setObjectName("comboBox_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 300, 291, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 400, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(51, 61, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(542, 62, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(542, 300, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(544, 122, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(545, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(541, 242, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit.setGeometry(QtCore.QRect(50, 130, 411, 261))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_6.setGeometry(QtCore.QRect(680, 280, 291, 41))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(537, 109, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_7.setGeometry(QtCore.QRect(680, 166, 291, 41))
        self.comboBox_7.setObjectName("comboBox_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 30, 281, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(538, 159, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_6)
        self.label_11.setGeometry(QtCore.QRect(539, 222, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_6)
        self.label_12.setGeometry(QtCore.QRect(536, 279, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_8.setGeometry(QtCore.QRect(680, 224, 291, 41))
        self.comboBox_8.setObjectName("comboBox_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_6.setGeometry(QtCore.QRect(680, 340, 291, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_13 = QtWidgets.QLabel(self.tab_6)
        self.label_13.setGeometry(QtCore.QRect(537, 339, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        self.label_14.setGeometry(QtCore.QRect(50, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(680, 110, 291, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_8.setGeometry(QtCore.QRect(710, 412, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 100, 281, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_15 = QtWidgets.QLabel(self.tab_6)
        self.label_15.setGeometry(QtCore.QRect(50, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_9.setGeometry(QtCore.QRect(530, 30, 311, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 410, 161, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 150, 411, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_11)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 1021, 511))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_12)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 1011, 421))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_28.setGeometry(QtCore.QRect(630, 430, 351, 41))
        self.pushButton_28.setObjectName("pushButton_28")
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_22.setGeometry(QtCore.QRect(330, 60, 281, 41))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_22.setGeometry(QtCore.QRect(360, 330, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.label_31 = QtWidgets.QLabel(self.tab_13)
        self.label_31.setGeometry(QtCore.QRect(140, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_23.setGeometry(QtCore.QRect(330, 130, 281, 41))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_32 = QtWidgets.QLabel(self.tab_13)
        self.label_32.setGeometry(QtCore.QRect(140, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_24.setGeometry(QtCore.QRect(330, 200, 281, 41))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_33 = QtWidgets.QLabel(self.tab_13)
        self.label_33.setGeometry(QtCore.QRect(73, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.tabWidget_4.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_25.setGeometry(QtCore.QRect(220, 30, 251, 41))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_42 = QtWidgets.QLabel(self.tab_14)
        self.label_42.setGeometry(QtCore.QRect(40, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_23.setGeometry(QtCore.QRect(400, 400, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_24.setGeometry(QtCore.QRect(530, 24, 311, 51))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_25.setGeometry(QtCore.QRect(40, 390, 161, 51))
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_36 = QtWidgets.QLabel(self.tab_14)
        self.label_36.setGeometry(QtCore.QRect(221, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_28.setGeometry(QtCore.QRect(400, 140, 281, 41))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_27.setGeometry(QtCore.QRect(400, 210, 281, 41))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_34 = QtWidgets.QLabel(self.tab_14)
        self.label_34.setGeometry(QtCore.QRect(160, 280, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_14)
        self.label_35.setGeometry(QtCore.QRect(223, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_14)
        self.lineEdit_26.setGeometry(QtCore.QRect(400, 280, 281, 41))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.tabWidget_4.addTab(self.tab_14, "")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 471, 491))
        self.groupBox.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.groupBox.setObjectName("groupBox")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(52, 112, 141, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(52, 213, 111, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(52, 257, 191, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(52, 170, 81, 21))
        self.label_19.setObjectName("label_19")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 110, 251, 41))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(200, 160, 251, 41))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(200, 210, 251, 41))
        self.lineEdit_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(200, 260, 251, 41))
        self.lineEdit_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 380, 201, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(530, 10, 461, 191))
        self.groupBox_2.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(170, 88, 241, 41))
        self.lineEdit_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_13.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(30, 92, 111, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(30, 40, 131, 31))
        self.label_21.setObjectName("label_21")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(170, 38, 241, 41))
        self.lineEdit_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(170, 140, 201, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(530, 210, 461, 291))
        self.groupBox_4.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(198, 130, 231, 41))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_16.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_18.setGeometry(QtCore.QRect(198, 180, 231, 41))
        self.lineEdit_18.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_18.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(10, 135, 121, 31))
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(10, 40, 141, 31))
        self.label_25.setObjectName("label_25")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_17.setGeometry(QtCore.QRect(198, 30, 231, 41))
        self.lineEdit_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(198, 80, 231, 41))
        self.lineEdit_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 230, 201, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(10, 180, 191, 41))
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(10, 87, 81, 31))
        self.label_24.setObjectName("label_24")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 1021, 511))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 120, 1011, 361))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("font: 9pt \"Segoe UI\";")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_14.setGeometry(QtCore.QRect(652, 40, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_19.setGeometry(QtCore.QRect(310, 50, 271, 41))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_26 = QtWidgets.QLabel(self.tab_7)
        self.label_26.setGeometry(QtCore.QRect(40, 40, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_15.setGeometry(QtCore.QRect(662, 50, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_20.setGeometry(QtCore.QRect(320, 50, 271, 41))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_27 = QtWidgets.QLabel(self.tab_8)
        self.label_27.setGeometry(QtCore.QRect(120, 44, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 120, 1011, 361))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_16.setGeometry(QtCore.QRect(652, 46, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_21.setGeometry(QtCore.QRect(310, 50, 271, 41))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_28 = QtWidgets.QLabel(self.tab_9)
        self.label_28.setGeometry(QtCore.QRect(30, 44, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 120, 1011, 361))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(40, 190, 71, 71))
        self.pushButton_26.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon5)
        self.pushButton_26.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_26.setObjectName("pushButton_26")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(780, -20, 411, 581))
        self.groupBox_3.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(80, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_18.setGeometry(QtCore.QRect(200, 190, 131, 121))
        self.pushButton_18.setStyleSheet("background-color: rgb(48, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_19.setGeometry(QtCore.QRect(60, 190, 131, 121))
        self.pushButton_19.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_20.setGeometry(QtCore.QRect(200, 320, 131, 121))
        self.pushButton_20.setStyleSheet("background-color: rgb(25, 35, 45);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_21.setGeometry(QtCore.QRect(60, 320, 131, 121))
        self.pushButton_21.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 250, 21, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.groupBox_3.hide()
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_17.clicked.connect(self.Hiding_Themes)

        self.tabWidget.tabBar().setVisible(False)
        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_26.clicked.connect(self.Open_CLients_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_9.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Books)
        self.pushButton_10.clicked.connect(self.Delete_Books)

        self.Show_Author()
        self.Show_Category()
        self.Show_Publisher()

        self.Show_Category_Combobox()
        self.Show_Author_Combobox()
        self.Show_Publisher_Combobox()

        self.Show_All_Clients()
        self.Show_All_Books()

        self.pushButton_14.clicked.connect(self.Add_Category)
        self.pushButton_15.clicked.connect(self.Add_Author)
        self.pushButton_16.clicked.connect(self.Add_Publisher)

        self.pushButton_11.clicked.connect(self.Add_New_User)
        self.pushButton_12.clicked.connect(self.Login)
        self.pushButton_13.clicked.connect(self.Edit_User)

##        style = open('themes/darkblue.css' , 'r')
##        style = style.read()
##        self.setStyleSheet(style)

        self.pushButton_19.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_18.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_21.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton_20.clicked.connect(self.QDark_Theme)

        self.pushButton_22.clicked.connect(self.Add_New_Client)
        self.pushButton_24.clicked.connect(self.Search_Client)
        self.pushButton_23.clicked.connect(self.Edit_Client)
        self.pushButton_25.clicked.connect(self.Delete_Client)

        self.Show_All_Operations()
        self.pushButton_6.clicked.connect(self.Handel_Day_Operations)

        self.pushButton_29.clicked.connect(self.Export_Day_Operations)
        self.pushButton_27.clicked.connect(self.Export_Books)
        self.pushButton_28.clicked.connect(self.Export_Clients)

    def MessageBox(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()

    ########################################
    ######### opening tabs #################
    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_CLients_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(4)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Client Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "From"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "To"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Book Title"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Retrieve"))
        self.comboBox.setItemText(1, _translate("MainWindow", "rent"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "Type"))
        self.label_2.setText(_translate("MainWindow", "Days"))
        self.lineEdit_29.setPlaceholderText(_translate("MainWindow", "Enter Client Name"))
        self.pushButton_29.setText(_translate("MainWindow", "Export Today Operations To Excel File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Code"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Title"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book Description"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Book Category"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Book Author"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Book Publisher"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Book Price"))
        self.pushButton_27.setText(_translate("MainWindow", "Export Book To Excel File"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "All Books"))
        self.pushButton_7.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "Book Title"))
        self.label_4.setText(_translate("MainWindow", "Book Code"))
        self.label_5.setText(_translate("MainWindow", "Book Price"))
        self.label_6.setText(_translate("MainWindow", "Category"))
        self.label_7.setText(_translate("MainWindow", "Author"))
        self.label_8.setText(_translate("MainWindow", "Publisher"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Add New Book"))
        self.label_9.setText(_translate("MainWindow", "Book Code"))
        self.label_10.setText(_translate("MainWindow", "Category"))
        self.label_11.setText(_translate("MainWindow", "Author"))
        self.label_12.setText(_translate("MainWindow", "Publisher"))
        self.label_13.setText(_translate("MainWindow", "Book Price"))
        self.label_14.setText(_translate("MainWindow", "Book Title"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.label_15.setText(_translate("MainWindow", "Book Title"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.pushButton_10.setText(_translate("MainWindow", "Delete"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Edit Or Delete A Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Client Name"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Client Email"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Client National Id"))
        self.pushButton_28.setText(_translate("MainWindow", "Export Clients To Excel File"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("MainWindow", "All Clients"))
        self.pushButton_22.setText(_translate("MainWindow", "Add New Client"))
        self.label_31.setText(_translate("MainWindow", "Client Name"))
        self.label_32.setText(_translate("MainWindow", "Client Email"))
        self.label_33.setText(_translate("MainWindow", "Client National Id"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), _translate("MainWindow", "Add New CLient"))
        self.label_42.setText(_translate("MainWindow", "CLient National Id"))
        self.pushButton_23.setText(_translate("MainWindow", "Save CLient Data"))
        self.pushButton_24.setText(_translate("MainWindow", "Search"))
        self.pushButton_25.setText(_translate("MainWindow", "Delete"))
        self.label_36.setText(_translate("MainWindow", "Client Name"))
        self.label_34.setText(_translate("MainWindow", "Client National Id"))
        self.label_35.setText(_translate("MainWindow", "Client Email"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MainWindow", "Edit Or Delete A Client"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Page"))
        self.groupBox.setTitle(_translate("MainWindow", "Add New User"))
        self.label_16.setText(_translate("MainWindow", "User Name"))
        self.label_17.setText(_translate("MainWindow", "Password"))
        self.label_18.setText(_translate("MainWindow", "Password Again"))
        self.label_19.setText(_translate("MainWindow", "Email"))
        self.pushButton_11.setText(_translate("MainWindow", "Add User"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Edit User Information"))
        self.label_20.setText(_translate("MainWindow", "Password"))
        self.label_21.setText(_translate("MainWindow", "User Name"))
        self.pushButton_12.setText(_translate("MainWindow", "Login"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Edit Your Data"))
        self.label_23.setText(_translate("MainWindow", "Password"))
        self.label_25.setText(_translate("MainWindow", "User Name"))
        self.pushButton_13.setText(_translate("MainWindow", "Edit User Data"))
        self.label_22.setText(_translate("MainWindow", "Password Again"))
        self.label_24.setText(_translate("MainWindow", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category Name"))
        self.pushButton_14.setText(_translate("MainWindow", "Add New Category"))
        self.label_26.setText(_translate("MainWindow", "New Category Name"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "Categories"))
        self.pushButton_15.setText(_translate("MainWindow", "Add New Author"))
        self.label_27.setText(_translate("MainWindow", "New  Author"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author Name"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "Author"))
        self.pushButton_16.setText(_translate("MainWindow", "Add New Publisher"))
        self.label_28.setText(_translate("MainWindow", "New Publisher Name"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Publisher Name"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Publisher"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.label_29.setText(_translate("MainWindow", "Apply New Theme ^_^"))
        self.pushButton_18.setText(_translate("MainWindow", "Dark Blue"))
        self.pushButton_19.setText(_translate("MainWindow", "Dark Orange"))
        self.pushButton_20.setText(_translate("MainWindow", "QDark"))
        self.pushButton_21.setText(_translate("MainWindow", "Dark Gray"))
        self.pushButton_17.setText(_translate("MainWindow", ">"))



        ########################################
    ######### Day Operations #################
    def Handel_Day_Operations(self):
        book_title = self.lineEdit.text()
        client_name = self.lineEdit_29.text()
        type = self.comboBox.currentText()
        days_number = self.comboBox_2.currentIndex() + 1
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=days_number)

        #print(today_date)
        #print(to_date)
        query = "INSERT INTO dayoperation(book_name, client, type , days , date , to_date) " \
          "VALUES (%s , %s , %s , %s , %s , %s) " 
        args = (book_title ,client_name, type , days_number , today_date  , to_date,)
   
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query, args)
     
            self.MessageBox('Successful', 'New Operation Addedd')
            conn.commit()
            self.Show_All_Operations()
            
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()


    def Show_All_Operations(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT book_name , client , type , date , to_date FROM dayoperation")
        data = mycursor.fetchall()

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)


    ########################################
    ######### Books #################

    def Show_All_Books(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT book_code,book_name,book_desc,book_category,book_author,book_publisher,book_price FROM book")
        data = mycursor.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)
            
        #self.db.close()


    def Add_New_Book(self):
        self.Show_All_Books()
        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        #query = "INSERT INTO book(book_name,book_desc,book_code,book_category,book_author,book_publisher,book_price) VALUES('"+ book_title +"' , '"+ book_description +"' , '"+ book_code +"' , "+ book_category +" , "+ book_author +" , "+ book_publisher +" , '"+ book_price +"')"     
        #query = '''INSERT INTO book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            #VALUES (%s , %s , %s , %s , %s , %s , %s) ''' ,(book_title , book_description , book_code , book_category , book_author , book_publisher , book_price,)
        query = "INSERT INTO book(book_name,book_desc,book_code,book_category,book_author,book_publisher,book_price) " \
          "VALUES (%s , %s , %s , %s , %s , %s , %s) " 
        args = (book_title , book_description , book_code , book_category , book_author , book_publisher , book_price,)
   
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query, args)
     
            self.MessageBox('Successful', 'New Book Addedd')
            conn.commit()
            self.lineEdit_2.setText('')
            self.textEdit.setPlainText('')
            self.lineEdit_3.setText('')
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_5.setCurrentIndex(0)
            self.lineEdit_4.setText('')
            self.Show_All_Books()
            
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()

    def Search_Books(self):
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        book_title = self.lineEdit_5.text()

        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM book WHERE book_name = '"+ book_title +"'")
        data = mycursor.fetchone()

        if data:
            #print(data)
            self.lineEdit_8.setText(data[2])
            self.textEdit_2.setPlainText(data[3])
            self.lineEdit_7.setText(data[1])
            self.comboBox_7.setCurrentText(data[4])
            self.comboBox_8.setCurrentText(data[5])
            self.comboBox_6.setCurrentText(data[6])
            self.lineEdit_6.setText(str(data[7]))
        else:
            self.MessageBox('Error','No Record found!')

    def Edit_Books(self):
        book_title = self.lineEdit_8.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_7.currentText()
        book_author = self.comboBox_8.currentText()
        book_publisher = self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()

        search_book_title = self.lineEdit_5.text()
        
        query = "UPDATE book SET book_name=%s ,book_desc=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name = %s"
        data = (book_title,book_description,book_code,book_category,book_author,book_publisher , book_price , search_book_title,)
     
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query, data)
            self.MessageBox('Successful','book updated')
            conn.commit()
            self.Show_All_Books()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()

    def Delete_Books(self):
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
         
        cursor = conn.cursor()
        book_title = self.lineEdit_5.text()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setInformativeText("Are you sure you want to delete this book")
        msg.setWindowTitle("Delete book")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        warning = retval = msg.exec_()
        sql = "DELETE FROM book WHERE book_name = '"+ book_title +"' "
        #data = (book_title)
        try:
            if warning == QMessageBox.Yes:
                cursor.execute(sql)
                self.MessageBox('Successful','Book Deleted')
                conn.commit()
                self.Show_All_Books()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()


    ########################################
    ######### Clients #################
    def Show_All_Clients(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT client_name , client_email ,client_nationalid FROM clients")
        data = mycursor.fetchall()
        
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)
    
    def Add_New_Client(self):
        client_name = self.lineEdit_22.text()
        client_email = self.lineEdit_23.text()
        client_nationalid = self.lineEdit_24.text()

        query = "INSERT INTO clients(client_name , client_email , client_nationalid) " \
          "VALUES (%s , %s , %s ) " 
        args = (client_name , client_email , client_nationalid,)
   
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query, args)
            self.MessageBox('Successful', 'New CLient Added')
            self.lineEdit_22.setText(' ')
            self.lineEdit_23.setText(' ')
            self.lineEdit_24.setText(' ')
            conn.commit()
            self.Show_All_Clients()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()

    def Search_Client(self):
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        client_national_id = self.lineEdit_25.text()

        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM clients WHERE client_nationalid = '"+ client_national_id +"'")
        data = mycursor.fetchone()

        if data:
            #print(data)
            self.lineEdit_28.setText(data[1])
            self.lineEdit_27.setText(data[2])
            self.lineEdit_26.setText(data[3])
        else:
            self.MessageBox('Error','No Record found!')


    def Edit_Client(self):
        client_original_national_id = self.lineEdit_25.text()
        client_name = self.lineEdit_28.text()
        client_email = self.lineEdit_27.text()
        client_national_id = self.lineEdit_26.text()

        
        query = "UPDATE clients SET client_name = %s , client_email = %s , client_nationalid = %s WHERE client_nationalid = %s"
        data = (client_name , client_email , client_national_id , client_original_national_id,)
     
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query, data)
            self.MessageBox('Successful','CLient Data Updated')
            conn.commit()
            self.Show_All_Clients()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()

    def Delete_Client(self):
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
         
        cursor = conn.cursor()
        client_original_national_id = self.lineEdit_25.text()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setInformativeText("Are you sure you want to delete this client")
        msg.setWindowTitle("Delete CLient")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        warning = retval = msg.exec_()
        sql = "DELETE FROM clients WHERE client_nationalid = '"+ client_original_national_id +"' "
        #data = (book_title)
        try:
            if warning == QMessageBox.Yes:
                cursor.execute(sql)
                self.MessageBox('Successful','CLient Deleted')
                conn.commit()
                self.Show_All_Clients()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()



    ########################################
    ######### users #################

    def Add_New_User(self):

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()

        query = "INSERT INTO users(user_name , user_email , user_password) " \
          "VALUES (%s , %s , %s ) " 
        args = (username , email , password,)
   
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            if password == password2:
                cursor.execute(query, args)
                self.MessageBox('Successful', 'New User Addedd')
            else:
                self.MessageBox('Password Mismatch','please add a valid password twice')
            
            conn.commit()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()


    def Login(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        
        mycursor = conn.cursor()
        username = self.lineEdit_14.text()
        password = self.lineEdit_13.text()
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()

        for row in myresult:
            if username == row[1] and password == row[3]:
                #print('user match')
                self.MessageBox('Login', 'Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_17.setText(row[1])
                self.lineEdit_15.setText(row[2])
                self.lineEdit_16.setText(row[3])


    def Edit_User(self):

        username = self.lineEdit_17.text()
        email = self.lineEdit_15.text()
        password = self.lineEdit_16.text()
        password2 = self.lineEdit_18.text()

        original_name = self.lineEdit_14.text()

        if password == password2 :
            dbconfig = read_db_config()
            conn = MySQLConnection(**dbconfig)
            
            mycursor = conn.cursor()

            print(username)
            print(email)
            print(password)

            query = "UPDATE users SET user_name=%s , user_email=%s , user_password=%s WHERE user_name=%s"
            data = (username , email , password , original_name)
            mycursor .execute(query, data)
            self.MessageBox('Successful','User Data Updated Successfully')
            conn.commit()
        else:
            self.MessageBox('Error','make sure you entered you password correctly')


   ########################################
    ######### settings #################

    def Add_Category(self):
        category_name = self.lineEdit_19.text()
        query = "INSERT INTO category(category_name) VALUES('"+ category_name +"')"     
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query)
     
            self.MessageBox('Successful', 'New Category Addedd')
            self.lineEdit_19.setText('')
            self.Show_Category()
            self.Show_Category_Combobox()
            
            conn.commit()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()


    def Show_Category(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT category_name FROM category")
        data = mycursor.fetchall()
        #print(data)
        
        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form) :
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)


    def Add_Author(self):
        
        author_name = self.lineEdit_20.text()
        query = "INSERT INTO authors(author_name) VALUES('"+ author_name +"')"     
        #query = "INSERT INTO authors(author_name) VALUES (%s)", (author_name,)    
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query)
     
            self.MessageBox('Successful', 'New Author Addedd')
            self.lineEdit_20.setText('')
            self.Show_Author()
            self.Show_Author_Combobox()
            
            conn.commit()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()


    def Show_Author(self):

        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT author_name FROM authors")
        data = mycursor.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Publisher(self):

        publisher_name = self.lineEdit_21.text()
        query = "INSERT INTO publisher(publisher_name) VALUES('"+ publisher_name +"')"     
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
     
            cursor = conn.cursor()
            cursor.execute(query)
     
            self.MessageBox('Successful', 'New Publisher Addedd')
            self.lineEdit_21.setText('')
            self.Show_Publisher()
            self.Show_Publisher_Combobox()
            
            conn.commit()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()

    def Show_Publisher(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT publisher_name FROM publisher")
        data = mycursor.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


   ########################################
    ######### show settings data in UI #################
    def Show_Category_Combobox(self):
        
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT category_name FROM category")
        data = mycursor.fetchall()

        self.comboBox_3.clear()
        for category in data :
            self.comboBox_3.addItem(category[0])
            self.comboBox_7.addItem(category[0])



    def Show_Author_Combobox(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT author_name FROM authors")
        data = mycursor.fetchall()

        self.comboBox_4.clear()
        for author in data :
            self.comboBox_4.addItem(author[0])
            self.comboBox_8.addItem(author[0])


    def Show_Publisher_Combobox(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT publisher_name FROM publisher")
        data = mycursor.fetchall()
        
        self.comboBox_5.clear()
        for publisher in data :
            self.comboBox_5.addItem(publisher[0])
            self.comboBox_6.addItem(publisher[0])

    ########################################
    ######### Export Data #################
    def Export_Day_Operations(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT book_name , client , type , date , to_date FROM dayoperation")
        data = mycursor.fetchall()
        
        wb = Workbook('day_operations.xlsx')
        sheet1  = wb.add_worksheet()

        sheet1.write(0,0,'book title')
        sheet1.write(0,1,'cliant name')
        sheet1.write(0,2,'type')
        sheet1.write(0,3,'from - date')
        sheet1.write(0,4,'to - date')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.MessageBox('Exported','Report Created Successfully')



    def Export_Books(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT book_code,book_name,book_desc,book_category,book_author,book_publisher,book_price FROM book")
        data = mycursor.fetchall()

        wb = Workbook('all_books.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Book Code')
        sheet1.write(0,1 , 'Book Name')
        sheet1.write(0,2 , 'Book Description')
        sheet1.write(0,3 , 'Book Category')
        sheet1.write(0,4 , 'Book Author')
        sheet1.write(0,5 , 'Book publisher')
        sheet1.write(0,6 , 'Book Price')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.MessageBox('Exported','Book Report Created Successfully')


    def Export_Clients(self):
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)

        mycursor = conn.cursor()
        mycursor.execute("SELECT client_name , client_email ,client_nationalid FROM clients")
        data = mycursor.fetchall()

        wb = Workbook('all_CLients.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'Client Name')
        sheet1.write(0,1 , 'CLient Email')
        sheet1.write(0,2 , 'CLient NationalID')


        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.MessageBox('Exported','CLients Report Created Successfully')

    ########################################
    #########  UI Themes #################

    def Dark_Blue_Theme(self):
        self.MessageBox('Theme','Theme in use')
##        style = open('themes/darkblue.css' , 'r')
##        style = style.read()
##        app.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        self.MessageBox('Theme Error','Cannot apply Theme')
##        style = open('themes/darkgray.css' , 'r')
##        style = style.read()
##        app.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        self.MessageBox('Theme Error','Cannot apply Theme')
##        style = open('themes/darkorange.css' , 'r')
##        style = style.read()
##        app.setStyleSheet(style)

    def QDark_Theme(self):
        self.MessageBox('Theme Error','Cannot apply Theme')
##        style = open('themes/qdark.css' , 'r')
##        style = style.read()
##        app.setStyleSheet(style)





import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

