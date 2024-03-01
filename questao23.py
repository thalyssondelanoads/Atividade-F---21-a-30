def data_recente():
    if ano1 > ano2:
        print(f' A Data mais Recente é {dia1}/{mes1}/{ano1} ')
    
    elif ano2 > ano1:
        print(f' A Data mais Recente é {dia2}/{mes2}/{ano2} ')
        
    elif ano1 == ano2 and mes1 > mes2:
        print(f' A Data mais Recente é {dia1}/{mes1}/{ano1} ')
        
    elif ano1 == ano2 and mes2 > mes1:
        print(f' A Data mais Recente é {dia2}/{mes2}/{ano2} ')
        
    elif ano1 == ano2 and mes1 == mes2 and dia1 > dia2:
        print(f' A Data mais Recente é {dia1}/{mes1}/{ano1} ')
        
    else:
        print(f' A Data mais Recente é {dia2}/{mes2}/{ano2} ')
        
#-------------------------------- 
    
print('Verificar Condição')
print('------------')

dia1 = int(input('Digite o Dia da 1° Data: '))
mes1 = int(input('Digite o Mês da 1° Data: '))
ano1 = int(input('Digite o Ano da 1° Data: '))
print('------------')

dia2 = int(input('Digite o Dia da 2° Data: '))
mes2 = int(input('Digite o Mês da 2° Data: '))
ano2 = int(input('Digite o Ano da 2° Data: '))
print('------------')

data_recente()
