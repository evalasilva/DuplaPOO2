from pessoa import Pessoa
from conta import Conta

class Banco:
    _total_contas = 0
    _numero_conta = 100

    __slots__ = ['_dict_clientes']
    def __init__(self):
        self._dict_clientes = {}

    @staticmethod
    def get_total_contas():
        return Banco._total_contas

    def jaexiste(self, cpf):
        if cpf in self._dict_clientes.keys():
            return True
        else:
            return False

    def cadastrar(self,nome, endereco, cpf, nasc, senha):
        if self.jaexiste(cpf):
            return False
        else:
            cliente = Pessoa(nome, endereco, cpf, nasc)
            conta = Conta(Banco._numero_conta, cliente, senha)
            self._dict_clientes[cpf] = conta
            Banco._numero_conta += 1
            Banco._total_contas += 1
            return True

