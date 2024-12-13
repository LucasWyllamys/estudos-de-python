# Você pode ter instruções if dentro de instruções if, o que é chamado de instruções if aninhadas:
x = 41

if x > 10:
    print("maior que dez")
    if x > 20:
        print("e maior que vinte")
    else:
        print("e menor que vinte")
''' Saída:
maior que dez
e maior que vinte
'''
