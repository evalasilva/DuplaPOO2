import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes=[]

    def imprimir(self):
        uma_string = ''
        uma_string += ('\nAbertura: {}'.format((self.data_abertura))) + '\n'
        uma_string += 'Transações: ' + '\n'

        for t in self.transacoes:
            uma_string += t + '\n'
        return uma_string