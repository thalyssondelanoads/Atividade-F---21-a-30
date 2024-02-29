def bhaskara():
    delta = b**2 - (4 * a * c)

    if a == 0:
        print(' ERRO: O Coeficiente A não pode ser 0')

    elif delta < 0:
        print(' ERRO: Não existe raiz de Números Negativos dentro dos Números Reais!')
        
    else:
        x1 = (-b + (delta**0.5)) / (2 * a)
        x2 = (-b - (delta**0.5)) / (2 * a)
        print(f' X1 = {x1:.3} ')
        print(f' X2 = {x2:.3} ')

#--------------------------------

print('Equação de 2º Grau')
print('--------------')

a = int(input('Digite o Valor do Coeficiente A: '))
b = int(input('Digite o Valor do Coeficiente B: '))
c = int(input('Digite o Valor do Coeficiente C: '))
print('--------------')

bhaskara()
