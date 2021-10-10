# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Transferencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 291, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.conta = QtWidgets.QLineEdit(self.centralwidget)
        self.conta.setGeometry(QtCore.QRect(90, 240, 251, 41))
        self.conta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.conta.setObjectName("conta")
        self.buttonTransf = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTransf.setGeometry(QtCore.QRect(250, 340, 121, 41))
        self.buttonTransf.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.buttonTransf.setObjectName("buttonTransf")
        self.valorTransf = QtWidgets.QLineEdit(self.centralwidget)
        self.valorTransf.setGeometry(QtCore.QRect(90, 150, 251, 41))
        self.valorTransf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.valorTransf.setObjectName("valorTransf")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Transferência"))
        self.label_2.setText(_translate("MainWindow", "Qual é o valor da transferência?"))
        self.label_3.setText(_translate("MainWindow", "Conta"))
        self.buttonTransf.setText(_translate("MainWindow", "Transferir"))
        self.valorTransf.setPlaceholderText(_translate("MainWindow", "R$ 0,00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
