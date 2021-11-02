# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class T_Usuario(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(400, 140, 201, 111))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background-color: rgb(32, 74, 135);\n"
                                 "    border-radius: 10px;\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.saldo = QtWidgets.QLabel(self.frame)
        self.saldo.setGeometry(QtCore.QRect(50, 50, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.saldo.setFont(font)
        self.saldo.setStyleSheet("color: rgb(255, 255, 255);")
        self.saldo.setObjectName("saldo")
        self.buttonTransf = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTransf.setGeometry(QtCore.QRect(30, 140, 311, 31))
        self.buttonTransf.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonTransf.setStyleSheet("color: rgb(255, 255, 255);")
        self.buttonTransf.setObjectName("buttonTransf")
        self.buttonDepos = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDepos.setGeometry(QtCore.QRect(30, 190, 311, 31))
        self.buttonDepos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonDepos.setStyleSheet("color: rgb(255, 255, 255);")
        self.buttonDepos.setObjectName("buttonDepos")
        self.buttonSaque = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSaque.setGeometry(QtCore.QRect(30, 240, 311, 31))
        self.buttonSaque.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSaque.setStyleSheet("color: rgb(255, 255, 255);")
        self.buttonSaque.setObjectName("buttonSaque")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 40, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.buttonExtra = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtra.setGeometry(QtCore.QRect(30, 290, 311, 31))
        self.buttonExtra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonExtra.setStyleSheet("color: rgb(255, 255, 255);")
        self.buttonExtra.setObjectName("buttonExtra")
        self.buttonSair = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSair.setGeometry(QtCore.QRect(30, 340, 311, 31))
        self.buttonSair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSair.setStyleSheet("color: rgb(255, 255, 255);")
        self.buttonSair.setObjectName("buttonSair")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 260, 201, 111))
        self.frame_2.setStyleSheet("QFrame{\n"
                                   "    background-color: rgb(32, 74, 135);\n"
                                   "    border-radius: 10px;\n"
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.limite = QtWidgets.QLabel(self.frame_2)
        self.limite.setGeometry(QtCore.QRect(50, 50, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.limite.setFont(font)
        self.limite.setStyleSheet("color: rgb(255, 255, 255);")
        self.limite.setObjectName("limite")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Usuário"))
        self.label.setText(_translate("MainWindow", "Saldo"))
        self.saldo.setText(_translate("MainWindow", "R$ 0,00"))
        self.buttonTransf.setText(_translate("MainWindow", "Transferência"))
        self.buttonDepos.setText(_translate("MainWindow", "Depósito"))
        self.buttonSaque.setText(_translate("MainWindow", "Saque"))
        self.label_3.setText(_translate("MainWindow", "Bem vindo(a)!"))
        self.buttonExtra.setText(_translate("MainWindow", "Extrato"))
        self.buttonSair.setText(_translate("MainWindow", "Sair"))
        self.label_4.setText(_translate("MainWindow", "Limite"))
        self.limite.setText(_translate("MainWindow", "R$ 0,00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = T_Usuario()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
