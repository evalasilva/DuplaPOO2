from cliente import Cliente
from conta import Conta

def sucesso(ok):
    if (ok):
        print('\nOperação realizada com sucessos!')
    else:
        print('\nNão foi possível realizar a operação!')
# ADICIONANDO INFORMAÇÕES

# CLIENTES

pobre = Cliente('Maurício', 'Santos', '22222222222')
pobre.imprimir()
cPobre = Conta('222-2', pobre, 100.0)

print('Saldo: R$',cPobre._saldo)
print('Limite: R$',cPobre._limite)
sucesso(cPobre.sacar(200.0))
print('Saldo: R$',cPobre._saldo)
print('Limite: R$',cPobre._limite)
sucesso(cPobre.sacar(100.0))
print('Saldo: R$',cPobre._saldo)
print('Limite: R$',cPobre._limite)
sucesso(cPobre.depositar((400.0)))
print('Saldo: R$',cPobre._saldo)
print('Limite: R$',cPobre._limite)




#CONTAS
# cRico = Conta('111-1', rico, 2000.0, 3000.0)
# print('\nTotal de Contas: ', Conta.get_total_contas())
# cPobre = Conta('222-2', pobre, 200.0)
# print('\nTotal de Contas: ', Conta.get_total_contas())
#
# #TRANSIÇÕES
#
# sucesso(cRico.depositar(1000.0))
# print('Saldo: R$',cRico._saldo)
# sucesso(cRico.sacar(1500.0))
# sucesso(cRico.transferir(cPobre, 500.0))
#
#
# cRico.extrato()
# cRico._historico.imprimir()
#
# sucesso(cPobre.depositar(1000.0))
# print('\nSaldo: R$',cPobre._saldo)
# sucesso(cPobre.sacar(1500.0))
# sucesso(cPobre.transferir(cRico, 2000.0))
#
#
# cPobre.extrato()
# cPobre._historico.imprimir()
#
