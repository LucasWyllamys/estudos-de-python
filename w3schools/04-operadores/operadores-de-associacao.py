''' Operadores de associação são usados para testar se uma sequência é apresentada em um objeto:
Operator	    Description	                                                                               Example
in 	            Retorna True se uma sequência com o valor especificado estiver presente no objeto	       x in y	
not in	        Retorna True se uma sequência com o valor especificado não estiver presente no objeto      x not in y
'''
# Exemplo:
frutas = ['maçã', 'banana']

print('banana' in frutas)               # Saída: True (retorna True porque uma sequência com o valor "banana" está na lista)
print('morango' not in frutas)          # Saída: True (retorna True porque uma sequência com o valor "morango" não está na lista)

if 'maça' in frutas:
    print('Sim, maçã é uma fruta!')     # Saída: True

    