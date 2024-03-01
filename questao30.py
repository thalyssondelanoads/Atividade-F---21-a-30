def quadrado_perfeito():
    dezena1 = num // 100
    dezena2 = num % 100
    soma_dezena = dezena1 + dezena2
    potencia = soma_dezena ** 2
    
    if potencia == num:
        print(f' O Número {num} Atende a Condição ')
    
    else:
        print(f' O Número {num} NÃO Atende a Condição ')
        
#-------------------------------- 
    
print('Verificar Condição')
print('------------')

num = int(input('Digite o Número de 4 DÍgitos que Deseja Verificar: '))
print('------------')

quadrado_perfeito()
