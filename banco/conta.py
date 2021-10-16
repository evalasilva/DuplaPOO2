from historico import Historico

class Conta:


    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_l_max', '_senha']
    def __init__(self, numero, titular, senha, saldo=0, limite=200):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._l_max = limite
        self._limite = limite
        self._senha = senha
        self._historico = Historico()


    @property
    def numero(self):
        return self._numero

    @ numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, cliente):
        self._titular = cliente

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def senha(self):
        return self._senha

    def depositar(self, valor):
        if valor > 0:
            self._historico.transacoes.append('Depósito de R${} '.format(valor))
            if self._limite == self._l_max:
                self._saldo += valor
            else:
                self.pagarLimite(valor)
            return True
        else:
            return False

    def sacar(self, valor):
        if self._saldo >= 0:
            # JUROS DO LIMITE R$ 2 E SABER QNT VAI TIRAR DO LIMITE
            if (self._saldo < valor):
                if (self._saldo + self._limite + 2.0) >= valor:
                    return self.usarLimite(valor)
            elif(self._saldo >= valor):
                self._saldo -= valor
                self._historico.transacoes.append('Saque de R${}'.format(valor))
                return True
        self._historico.transacoes.append('Tentativa de saque de R${} - SALDO INSUFICIENTE!'.format(valor))
        return False

    def extrato(self):
        uma_string = ''
        uma_string += ('\nConta: {} - Saldo: R${}'.format(self._numero, self._saldo))+'\n'
        uma_string += self._historico.imprimir() + '\n'
        self._historico.transacoes.append('Emissão de extrato-saldo de R${}\n'.format(self._saldo))
        return uma_string

    def transferir(self, destino, valor):

        if(self.sacar(valor) == True):
            destino.depositar(valor)
            self._historico.transacoes.append('Transferência de R${} para conta {}'.format(valor, destino._numero))
            return True
        else:
            return False

    def usarLimite(self, valor):
        divTotal = 2.0 + valor
        tiraLimite = divTotal - self._saldo
        if (self._limite - tiraLimite) < 0.0:
            return False
        else:
            self._saldo = 0.0
            self._limite -= tiraLimite
            self._historico.transacoes.append('Saque de R${} '.format(valor))
            self._historico.transacoes.append('\tALERTA!!!\nUso de limite de R${}'.format(tiraLimite))
            return True

    def pagarLimite(self, valor):

        divida = self._l_max - self._limite
        if valor >= divida:
            self._limite = self._l_max
            self._saldo += valor - divida
            self._historico.transacoes.append('Pagamento de R${} do limite'.format(divida))

        else:
            self._limite += valor
            self._historico.transacoes.append('Pagamento de R${} do limite'.format(valor))
