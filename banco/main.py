import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog, QMainWindow
from PyQt5.QtCore import QCoreApplication

from t_deposito import T_Deposito
from t_cadastro import T_Cadastro
from t_extrato import T_Extrato
from t_login import T_Login
from t_saque import T_Saque
from t_transferencia import T_Transferencia
from t_usuario import T_Usuario
from banco import Banco


class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.t_login = T_Login()
        self.t_login.setupUi(self.stack0)

        self.t_cadastro = T_Cadastro()
        self.t_cadastro.setupUi(self.stack1)

        self.t_deposito = T_Deposito()
        self.t_deposito.setupUi(self.stack2)

        self.t_extrato = T_Extrato()
        self.t_extrato.setupUi(self.stack3)

        self.t_saque = T_Saque()
        self.t_saque.setupUi(self.stack4)

        self.t_transferencia = T_Transferencia()
        self.t_transferencia.setupUi(self.stack5)

        self.t_usuario = T_Usuario()
        self.t_usuario.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.b = Banco()

        self.t_login.entrar.clicked.connect(self.logar)
        self.t_login.pushButton_2.clicked.connect(self.abrir_cadastrar)

        self.t_deposito.buttonDepositar.clicked.connect(self.depositar)
        self.t_deposito.buttonMenu.clicked.connect(self.abrirTInicial)

        self.t_cadastro.buttonVolta.clicked.connect(self.abrirTInicial())
        self.t_cadastro.buttonCadastrar.clicked.connect(self.abrir_cadastrar)

        self.t_extrato.entrar.clicked.connect(self.logar)
        self.t_login.pushButton_2.clicked.connect(self.abrir_cadastrar)

        self.t_deposito.buttonDepositar.clicked.connect(self.depositar)
        self.t_deposito.buttonMenu.clicked.connect(self.abrirTInicial)

        self.t_cadastro.buttonVolta.clicked.connect(self.abrirTInicial())
        self.t_cadastro.buttonCadastrar.clicked.connect(self.abrir_cadastrar)

    def busca(self):
        cpf = self.t_buscar.lineEdit_5.text()
        if cpf == '':
            QMessageBox.information(None, 'Atenção!', 'Preencha o campo do CPF')
        else:
            if self.c.jaexiste(cpf):
                p = self.c.buscar(cpf)
                self.t_buscar.lineEdit_8.setText(p.nome)
                self.t_buscar.lineEdit_7.setText(p.endereco)
                self.t_buscar.lineEdit_6.setText(p.nasc)
                QMessageBox.information(None, 'Atenção!', 'Operação realizada com sucesso!')
                # self.limpa()
            else:
                QMessageBox.information(None, 'Atenção!', 'Pessoa não cadastrada!')
                self.limpaBus()

    def cadastramento(self):
        cpf = self.t_cadastrar.lineEdit.text()
        nome = self.t_cadastrar.lineEdit_2.text()
        endereco = self.t_cadastrar.lineEdit_3.text()
        nasc = self.t_cadastrar.lineEdit_4.text()
        if cpf == '' or nome == '' or endereco == '' or nasc == '':
            QMessageBox.information(None, 'Atenção!', 'Preencha todos os campos')
        else:
            p = Pessoa(nome, endereco, cpf, nasc)
            if self.c.jaexiste(p.cpf):
                QMessageBox.information(None, 'Atenção!', 'Pessoa já cadastrada!')
                self.limpaCad()
            else:
                self.c.adicionar(p)
                QMessageBox.information(None, 'Atenção!', 'Pessoa cadastrada com sucesso!')
                self.limpaCad()
        self.QtStack.setCurrentIndex(0)

    def limpaCad(self):
        self.t_cadastrar.lineEdit.setText('')
        self.t_cadastrar.lineEdit_2.setText('')
        self.t_cadastrar.lineEdit_3.setText('')
        self.t_cadastrar.lineEdit_4.setText('')

    def limpaBus(self):

        self.t_buscar.lineEdit_5.setText('')
        self.t_buscar.lineEdit_6.setText('')
        self.t_buscar.lineEdit_7.setText('')
        self.t_buscar.lineEdit_8.setText('')

    def abrirTCadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTBuscar(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTInicial(self):
        self.QtStack.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())