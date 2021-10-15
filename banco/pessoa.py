class Pessoa:

    __slots__ = ['_nome', '_endereco', '_cpf', '_nasc']
    def __init__(self, nome,endereco, cpf, nasc):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nasc = nasc

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nasc(self):
        return self._nasc

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco


    def imprimir(self):
        print('Nome: {} - CPF: {} - Nasc: {}\n Endereço: {}'.format(self._nome, self._cpf, self._nasc, self._endereco))

