import socket
import sys
from banco import Banco


class Servidor():

    def __init__(self):
        self.banco = Banco()
        self.serv = None
        self.conexao = None
        self.inicializar()
        self.menu()

    def inicializar(self):
        host = 'localhost'
        port = 8055
        addr = (host, port)
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv_socket.bind(addr)
        serv_socket.listen(10)
        print('aguardando conexao...')
        con, client = serv_socket.accept()
        print(f'Conectado a {client}')
        self.conexao = con
        self.serv = serv_socket
        print('conectado! \taguardando mensagem...\n')

    def menu(self):

        while True:
            mensServidor = self.conexao.recv(1024).decode()
            print('mensagem recebida: ' + mensServidor)
            msg_banco = list(mensServidor.split('//'))
            if msg_banco[0] == 'cadastrar':
                self.cadastrar(msg_banco)
            elif msg_banco[0] == 'sacar':
                self.sacar(msg_banco)
            elif msg_banco[0] == 'login':
                self.login(msg_banco)
            elif msg_banco[0] == 'depositar':
                self.depositar(msg_banco)
            elif msg_banco[0] == 'extrato':
                self.extrato(msg_banco)
            elif msg_banco[0] == 'transferir':
                self.transferir(msg_banco)
            else:
                print('cliente encerrado')
                self.conexao = None
                print('aguardando conexao...')
                con, client = self.serv.accept()
                print(f'Conectado a {client}')
                self.conexao = con

    def cadastrar(self, msg_banco):
        resposta = self.banco.cadastrar(
            msg_banco[1], msg_banco[2], msg_banco[3], msg_banco[4], msg_banco[5])
        self.msgCliente(resposta)

    def login(self, msg_banco):
        resposta = self.banco.login(msg_banco[1], msg_banco[2])
        self.msgCliente(resposta)

    def depositar(self, msg_banco):
        resposta = self.banco.depositar(msg_banco[1])
        print('Saindo do servidor:', resposta)
        self.msgCliente(resposta)

    def sacar(self, msg_banco):
        resposta = self.banco.sacar(msg_banco[1])
        print('Saindo do servidor:', resposta)
        self.msgCliente(resposta)

    def transferir(self, msg_banco):
        resposta = self.banco.transferir(msg_banco[1], msg_banco[2])
        print('Saindo do servidor:', resposta)
        self.msgCliente(resposta)

    def extrato(self, msg_banco):
        resposta = self.banco.historico()
        print('Saindo do servidor:', resposta)
        self.msgCliente(resposta)

    def msgCliente(self, dados):
        tira = '[]'
        for i in tira:
            dados = str(dados).replace(i, '')
        self.conexao.send(str(dados).encode())
        print("Enviado!")


if __name__ == '__main__':
    servidor = Servidor()
    sys.exit(servidor.serv.close())
