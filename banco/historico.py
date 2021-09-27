import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes=[]

    def imprimir(self):
        print('\nAbertura: {}'.format((self.data_abertura)))
        print('Transações: ')
        for t in self.transacoes:
            print(' - ', t)