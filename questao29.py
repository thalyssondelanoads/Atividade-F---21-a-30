def quadrado_perfeito():
    dezena1 = num // 100
    dezena2 = num % 100
    
    raiz = num ** 0.5
    soma = dezena2 + dezena1
    
    if num < 1000 or num > 9999:
        print('O Número Deve ter 4 Dígitos')
    
    elif raiz == soma:
        print(f'O Número {num} é um Quadrado Perfeito')
        
    else:
        print(f'O Número {num} NÃO é um Quadrado Perfeito')
    
#-------------------------------- 
    
print('Quadrado Perfeito')
print('------------')

num = int(input('Digite o Número de 4 Dígitos que Deseja Conferir: '))
print('------------')

quadrado_perfeito()
