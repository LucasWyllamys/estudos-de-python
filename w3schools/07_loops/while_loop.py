# Com o loop while podemos executar um conjunto de instruções desde que uma condição seja verdadeira:
# Nota: lembre-se de incrementar i, caso contrário o loop continuará para sempre.
i = 1
while i < 6:
    print(i)
    i += 1
''' Saída: 
1
2
3
4
5
'''

# Com a instrução break podemos parar o loop mesmo se a condição while for verdadeira:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
''' Saída:
1
2
3
'''

# Com a instrução continue podemos parar a iteração atual e continuar com a próxima:
# Continue para a próxima iteração se i for 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
''' Saída:
1
2
4
5
6
'''

# Com a instrução else podemos executar um bloco de código uma vez quando a condição não for mais verdadeira:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i não é mais menor que 6")
''' Saída:
1
2
3
4
5
i não é mais menor que 6
'''
