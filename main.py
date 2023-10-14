from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 471)
        MainWindow.setStyleSheet("background-color: grey;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 100, 81, 81))
        self.pushButton_1.setStyleSheet("background-color: white\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 100, 81, 81))
        self.pushButton_2.setStyleSheet("background-color: white\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 100, 81, 81))
        self.pushButton_3.setStyleSheet("background-color: white\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(250, 100, 81, 81))
        self.pushButton_plus.setStyleSheet("background-color: orange")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 180, 81, 81))
        self.pushButton_4.setStyleSheet("background-color: white\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 180, 81, 81))
        self.pushButton_6.setStyleSheet("background-color: white\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(250, 180, 81, 81))
        self.pushButton_minus.setStyleSheet("background-color: orange")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 180, 81, 81))
        self.pushButton_5.setStyleSheet("background-color: white\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 260, 81, 81))
        self.pushButton_7.setStyleSheet("background-color: white\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 260, 81, 81))
        self.pushButton_9.setStyleSheet("background-color: white\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiplication.setGeometry(QtCore.QRect(250, 260, 81, 81))
        self.pushButton_multiplication.setStyleSheet("background-color: orange")
        self.pushButton_multiplication.setObjectName("pushButton_multiplication")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 260, 81, 81))
        self.pushButton_8.setStyleSheet("background-color: white\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Clear.setGeometry(QtCore.QRect(10, 340, 81, 81))
        self.pushButton_Clear.setStyleSheet("background-color: red")
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(170, 340, 81, 81))
        self.pushButton_equal.setStyleSheet("background-color: orange")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_division = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_division.setGeometry(QtCore.QRect(250, 340, 81, 81))
        self.pushButton_division.setStyleSheet("background-color: orange")
        self.pushButton_division.setObjectName("pushButton_division")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(90, 340, 81, 81))
        self.pushButton_0.setStyleSheet("background-color: white\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 321, 71))
        self.textEdit.setStyleSheet("background-color: rgb(208, 208, 208)\n"
"")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_multiplication.setText(_translate("MainWindow", "*"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_Clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_division.setText(_translate("MainWindow", "/"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
