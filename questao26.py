def hipotenusa_cateto():
    if lado1 > lado2 and lado1 > lado3:
        print(f' Hipotenusa: {lado1} / Catetos: {lado2} e {lado3} ')
    
    elif lado2 > lado1 and lado2 > lado3:
        print(f' Hipotenusa: {lado2} / Catetos: {lado1} e {lado3} ')
    
    else:
        print(f' Hipotenusa: {lado3} / Catetos: {lado1} e {lado2} ')

#---------------------------

print('Identificar Hipotenusa e Catetos de um Triângulo')
print('---------')

lado1 = int(input('Digite o 1º Lado: '))
lado2 = int(input('Digite o 2º Lado: '))
lado3 = int(input('Digite o 3º Lado: '))

print('---------')

hipotenusa_cateto()
