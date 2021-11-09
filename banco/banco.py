from random import randint
import mysql.connector as mysql
import hashlib
import datetime


class Banco:
    _numero = 101

    def __init__(self):
        self.conexao = mysql.connect(
            host='localhost', db='Poo22', user='root', passwd='WFSL1021')
        self.cursor = self.conexao.cursor()
        self.id = 0

    def existe_cpf(self, cpf):
        query = "SELECT cpf FROM conta WHERE cpf ='{}'".format(cpf)
        self.cursor.execute(query)
        resultado = self.cursor.fetchall()
        if len(resultado) != 0:  # Verifica se o retorno contém alguma linha
            return True
        else:
            return False

    def cadastrar(self, nome, endereco, cpf, nasc, senha):
        if self.existe_cpf(cpf):
            return False
        else:
            Banco._numero = randint(11, 20000)
            data = datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')
            historico = ('\nAbertura: {}'.format((data))) + \
                '\n' + 'Transações: ' + '\n'
            query = "INSERT INTO conta (numero, nome, endereco, cpf, senha, historico) VALUES (%s,%s, %s, %s, MD5(%s), %s)"
            self.cursor.execute(
                query, (Banco._numero, nome, endereco, cpf, senha, historico))
            self.conexao.commit()

        return True

    def login(self, cpf, senha):
        try:
            self.cursor.execute(
                "SELECT id_conta, saldo, limite FROM conta WHERE cpf = %s AND senha = MD5(%s)", (cpf, senha))
            conta = list(self.cursor.fetchone())
            if(conta != None):
                print(conta)
                if conta[0] > 0:
                    resposta = [True, conta[1], conta[2]]
                    self.id = conta[0]
        except:
            resposta = [False]
        return resposta

    def sacar(self, valor, flag=0):
        self.cursor.execute(
            "SELECT saldo,limite FROM conta WHERE id_conta = {}".format((self.id)))
        resultado = self.cursor.fetchall()

        valor = float(valor)
        saldo = float(resultado[0][0])
        limite = float(resultado[0][1])

        resposta = [False]

        if saldo >= 0:
            if (saldo < valor):
                if (saldo + resultado[0][1] + 2.0) >= valor:
                    resposta = self.usarLimite(valor, saldo, limite)
            elif(saldo >= valor):
                saldo -= valor
                self.atualizar_valores(saldo, limite)
                self.atualizar_historico('\nSaque de R${} '.format(valor))
                resposta = [True, saldo, limite]
        return resposta

    def depositar(self, valor, flag=0):
        valor = float(valor)
        if valor > 0.0:
            self.cursor.execute(
                "SELECT saldo,limite FROM conta WHERE id_conta = {}".format((self.id)))
            resultado = self.cursor.fetchall()
            saldo = float(resultado[0][0])
            limite = float(resultado[0][1])

            if limite == 200.00:
                saldo += valor
                self.atualizar_valores(saldo, limite)
                resposta = [True, saldo, limite]
            else:
                resposta = self.pagarLimite(valor, saldo, limite)

            if(flag == 0):
                self.atualizar_historico('\nDepósito de R${} '.format(valor))
            return resposta
        else:
            return [False]

    def usarLimite(self, valor, saldo, limite):
        divTotal = 2.0 + valor
        tiraLimite = divTotal - saldo
        if (limite - tiraLimite) < 0.0:
            return [False]
        else:
            saldo = 0.0
            limite -= tiraLimite
            self.atualizar_valores(saldo, limite)
            return [True, saldo, limite]

    def atualizar_valores(self, saldo, limite):
        self.cursor.execute('UPDATE conta SET saldo=%s, limite=%s WHERE id_conta=%s', (float(
            saldo), float(limite), self.id))
        self.conexao.commit()

    def atualizar_historico(self, msg):
        try:
            self.cursor.execute(
                "SELECT historico FROM conta WHERE id_conta = {}".format((self.id)))
            resultado = self.cursor.fetchall()

            resultado = resultado[0][0] + msg

            self.cursor.execute(
                "UPDATE conta SET historico = %s WHERE id_conta = %s", (resultado, self.id))

            self.conexao.commit()
        except:
            print('Erro')

    def historico(self):
        try:
            self.cursor.execute(
                'SELECT historico FROM conta WHERE id_conta={}'.format(self.id))
            resultado = self.cursor.fetchall()
            return resultado[0][0]
        except:
            print('Erro')

    def pagarLimite(self, valor, saldo, limite):
        divida = 200 - limite
        if valor >= divida:
            limite = 200
            saldo += valor - divida
        else:
            limite += valor
        self.atualizar_valores(saldo, limite)
        return [True, saldo, limite]

    def transferir(self, destino, valor):
        valor = float(valor)
        self.cursor.execute(
            "SELECT id_conta,numero FROM conta WHERE cpf = {}".format((destino)))
        Destino = self.cursor.fetchall()
        if(self.sacar(float(valor), 1)[0] == True):
            atual = self.id

            self.cursor.execute(
                "SELECT numero FROM conta WHERE id_conta = {}".format((self.id)))
            origem = self.cursor.fetchall()

            self.atualizar_historico(
                '\n\nTransferência realizado de R${} para conta {} '.format(valor, Destino[0][1]))

            self.id = int(Destino[0][0])
            self.atualizar_historico(
                '\nTransferência recebida de R${} da conta {} '.format(valor, origem[0][0]))
            self.depositar(valor, 1)

            self.id = atual
            self.cursor.execute(
                "SELECT saldo,limite FROM conta WHERE id_conta = {}".format((self.id)))
            resultado = self.cursor.fetchall()
            saldo = float(resultado[0][0])
            limite = float(resultado[0][1])

            # self._historico.transacoes.append(
            #     'Transferência de R${} para conta {}'.format(valor, destino._numero))
            return [True, saldo, limite]
        else:
            return [False]
