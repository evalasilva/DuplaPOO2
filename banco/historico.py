import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes=[]

    def imprimir(self):
        print('\nAbertura: {}'.format((self.data_abertura)))
        print('Transações: ')

        uma_string = ''
        for t in self.transacoes:
            uma_string += t + '\n'

        return uma_string