from banco import Banco
def sucesso(ok):
    if (ok):
        print('\nOperação realizada com sucesso!')
    else:
        print('\nNão foi possível realizar a operação!')
# ADICIONANDO INFORMAÇÕES

b = Banco()
print(b.get_total_contas())

b.cadastrar('Eva', 'rua qlq', '123','23/02/1985')

print('Conta', b._dict_clientes['123'].numero)

sucesso(b._dict_clientes['123'].sacar(100))


sucesso(b._dict_clientes['123'].sacar(96))