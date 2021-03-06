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
import socket

'''
    ORDEM DAS BENDITAS VARIÁVEIS:
    
    id_conta - numero - saldo - limite - historico - nome - endereco - cpf - senha
'''


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

        self.cpf_usuario_atual = ''

        self.b = Banco()

        self.t_login.entrar.clicked.connect(self.logar)
        self.t_login.pushButton_2.clicked.connect(self.abrir_cadastrar)

        self.t_deposito.buttonDepositar.clicked.connect(self.depositar)
        self.t_deposito.buttonMenu.clicked.connect(self.abrir_usuario)

        self.t_cadastro.buttonVolta.clicked.connect(self.abrir_login)
        self.t_cadastro.buttonCadastrar.clicked.connect(self.cadastrar)

        self.t_extrato.buttonVoltar.clicked.connect(self.abrir_usuario)

        self.t_saque.buttonSacar.clicked.connect(self.sacar)
        self.t_saque.buttonVolta.clicked.connect(self.abrir_usuario)

        self.t_transferencia.buttonTransf.clicked.connect(self.transferencia)
        self.t_transferencia.buttonVolta.clicked.connect(self.abrir_usuario)

        self.t_usuario.buttonTransf.clicked.connect(self.abrir_transferencia)
        self.t_usuario.buttonSaque.clicked.connect(self.abrir_saque)
        self.t_usuario.buttonDepos.clicked.connect(self.abrir_depositar)
        self.t_usuario.buttonExtra.clicked.connect(self.abrir_extrato)
        self.t_usuario.buttonSair.clicked.connect(self.abrir_login)

        self.conectar()

    def conectar(self):
        host = 'localhost'
        port = 8055
        addr = ((host, port))  # Tupla de endereço
        # AF_INET parametro da familia do protocolo
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)  # conectando
        self.conexao = client_socket

    def enviar_msg(self, msg):
        self.conexao.send(msg.encode())
        print("msg enviada!")

    def receber_msg(self):
        msg = self.conexao.recv(1024).decode()
        dados = list(msg.split(','))
        return dados

    def cadastrar(self):
        cpf = self.t_cadastro.cpf.text()
        nome = self.t_cadastro.nome.text()
        endereco = self.t_cadastro.endereco.text()
        nasc = self.t_cadastro.nasc.text()
        senha = self.t_cadastro.senha.text()

        if cpf == '' or nome == '' or endereco == '' or senha == '':
            QMessageBox.information(
                None, 'Atenção!', 'Preencha todos os campos')
        else:
            # msg = f'{cadastrar}//' + nome + '//' + endereco + '//' + cpf + '//' + nasc + '//' + senha
            msg = f'cadastrar//{nome}//{endereco}//{cpf}//{nasc}//{senha}'
            self.enviar_msg(msg)
            resposta = self.receber_msg()
            # ve se funciona ou tem que ser booleano
            if resposta[0]:
                QMessageBox.information(
                    None, 'Ok!', 'Pessoa cadastrada com sucesso!')
                self.limpa_t_cadastro()
                self.abrir_login()
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'CPF já cadastrado!\nVerifique e tente novamente!')
                self.t_cadastro.cpf.setText('')

    def logar(self):
        cpf = self.t_login.cpf.text()
        senha = self.t_login.senha.text()
        if cpf == '' or senha == '':
            QMessageBox.information(
                None, 'Atenção!', 'Preencha todos os campos')
        else:
            msg = f'login//{cpf}//{senha}'
            self.enviar_msg(msg)
            resposta = self.receber_msg()
            print(resposta)
            if resposta[0] == 'True':
                self.t_usuario.saldo.setText('R$ ' + resposta[1])
                self.t_usuario.limite.setText('R$ ' + resposta[2])
                self.t_login.cpf.setText('')
                self.t_login.senha.setText('')
                self.abrir_usuario()
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Senha e/ou Cliente inválido(s)!\nVerifique e tente novamente!')
                self.t_login.cpf.setText('')
                self.t_login.senha.setText('')

    def depositar(self):
        valor = self.t_deposito.valor.text()
        if valor == '':
            QMessageBox.information(
                None, 'Atenção!', 'Preencha todos os campos')
        else:
            msg = f'depositar//{valor}'
            self.enviar_msg(msg)
            resposta = self.receber_msg()
            print(resposta)
            # RETORNAR SALDO ATUAL E LIMITE
            if resposta[0] == 'True':
                QMessageBox.information(
                    None, 'Atenção!', 'Depósito realizado com sucesso!')
                self.t_usuario.saldo.setText('R$ ' + resposta[1])
                self.t_usuario.limite.setText('R$ ' + resposta[2])
                self.abrir_usuario()
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Operação Inválida!\nVerifique e tente novamente!')
            self.t_deposito.valor.setText('')

    def extrato(self):
        msg = f'extrato'
        self.enviar_msg(msg)
        resposta = self.receber_msg()
        self.t_extrato.extrato.setText(resposta[0])

    def sacar(self):
        valor = self.t_saque.lineEdit.text()
        msg = f'sacar//{valor}'
        self.enviar_msg(msg)
        resposta = self.receber_msg()
        print(resposta)

        # deu certo? SALDO  LIMITE
        if resposta[0] == 'True':
            QMessageBox.information(
                None, 'Atenção!', 'Saque realizado com sucesso!')
            self.t_usuario.saldo.setText('R$ ' + resposta[1])
            self.t_usuario.limite.setText('R$ ' + resposta[2])
            self.abrir_usuario()
        else:
            QMessageBox.information(
                None, 'Atenção!', 'Saldo Insuficiente!\nVerifique e tente novamente!')
        self.t_saque.lineEdit.setText('')

    def transferencia(self):
        valor = self.t_transferencia.valor.text()
        cpf = self.t_transferencia.conta.text()
        if valor == '' or cpf == '':
            QMessageBox.information(
                None, 'Atenção!', 'Preencha todos os campos')
        else:
            # PRECISA ACRESCENTAR // NO FINAL
            msg = f'transferir//{cpf}//{valor}'
            self.enviar_msg(msg)
            resposta = self.receber_msg()
            if resposta[0] == 'True':
                QMessageBox.information(
                    None, 'Atenção!', 'Transferência realizada com sucesso!')
                self.t_usuario.saldo.setText(
                    'R$ ' + resposta[1])
                self.t_usuario.limite.setText(
                    'R$ ' + resposta[2])
                self.abrir_usuario()
            else:
                QMessageBox.information(
                    None, 'Atenção!', 'Operação Inválida!\nVerifique e tente novamente!')
        self.t_transferencia.valor.setText('')
        self.t_transferencia.conta.setText('')

    def limpa_t_cadastro(self):
        self.t_cadastro.nome.setText('')
        self.t_cadastro.cpf.setText('')
        self.t_cadastro.senha.setText('')
        self.t_cadastro.endereco.setText('')

    def abrir_login(self):
        self.cpf_usuario_atual = ('')
        self.t_login.cpf.setText('')
        self.t_login.senha.setText('')
        self.QtStack.setCurrentIndex(0)

    def abrir_usuario(self):
        self.QtStack.setCurrentIndex(6)

    def abrir_extrato(self):
        self.extrato()
        self.QtStack.setCurrentIndex(3)

    def abrir_cadastrar(self):
        self.t_login.cpf.setText('')
        self.t_login.senha.setText('')
        self.t_cadastro.senha.setText('')
        self.t_cadastro.cpf.setText('')
        self.t_cadastro.nome.setText('')
        self.t_cadastro.endereco.setText('')
        self.QtStack.setCurrentIndex(1)

    def abrir_depositar(self):
        self.t_deposito.valor.setText('')
        self.QtStack.setCurrentIndex(2)

    def abrir_transferencia(self):
        self.t_transferencia.valor.setText('')
        self.t_transferencia.conta.setText('')
        self.QtStack.setCurrentIndex(5)

    def abrir_saque(self):
        self.t_saque.lineEdit.setText('')
        self.QtStack.setCurrentIndex(4)

    def desconectar(self):
        '''
            encerra a conexao com o servidor
        '''
        print('cliente encerrado')
        self.conexao.send(''.encode())
        self.conexao.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    app.exec_()
    show_main.desconectar()
    sys.exit()
