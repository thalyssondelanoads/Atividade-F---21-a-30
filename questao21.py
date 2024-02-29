def arredondar():
    from math import ceil, floor
    
    meio = num + 0.5
    sucessor = num // 1 + 1
    
    if meio >= sucessor:
        pra_maior = ceil(num)
        print(F' O Número foi aproximado para {pra_maior} ')
        
    else:
        pra_menor = floor(num)
        print(F' O Número foi aproximado para {pra_menor} ')

#----------------------------

print('Arredondar Números')
print('-------------')

num = float(input('Digite o Número que Deseja Arredondar: '))
print('-------------')

arredondar()
