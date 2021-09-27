from historico import Historico

class Conta:
    _total_contas = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']
    def __init__(self, numero, titular, saldo, limite=0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

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

    def depositar(self, valor):
        if (self._saldo + valor ) > self._limite:
            return False
        else:
            self._saldo += valor
            return True

    def sacar(self, valor):
        if (self._saldo < valor):
           return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append('saque de R${}'.format(valor))
            return True

    def extrato(self):
        print('\nConta: {} - Saldo: R${}'.format(self._numero, self._saldo))
        self._historico.transacoes.append('Emissão de extrato-saldo de R${}\n'.format(self._saldo))


    def transferir(self, destino, valor):
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            self._historico.transacoes.append('Transferência de R${} para conta {}'.format(valor, destino._numero))
            return True
