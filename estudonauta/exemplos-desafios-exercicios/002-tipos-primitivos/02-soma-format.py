n1 = int(input('Primeiro número: '))  # A função float é usada para converter string em número flutuante
n2 = int(input('Segundo número: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'é', s)
print('A soma entre {0} e {1} é {2}'.format(n1, n2, s))  #Usando a função .format() na função print()
