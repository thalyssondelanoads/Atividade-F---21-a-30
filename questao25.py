def validar_senha():
    if senha == 1234:
        print(' Acesso Liberado! ')
    
    else:
        print(' Acesso Negado! ')

#---------------------------

print('Permissão de Acesso ')
print('---------')

senha = int(input('Digite a Senha: '))
print('---------')

validar_senha()
