def area():
    area = x * y
    
    if area < 0:
        print(' A Área NÃO pode ser Negativa')
        
    else:
        print(f' A Área do Retângulo é {area} ')

#---------------------------

print('Área do Retângulo no Plano')
print('----------------')

x = int(input('Digite o Valor de X no Plano:  '))
y = int(input('Digite o Valor de Y no Plano:  '))
print('----------------')

area()
