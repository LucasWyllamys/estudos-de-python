# Uma variável só está disponível de dentro da região em que foi criada. Isso é chamado de escopo.

# Uma variável criada dentro de uma função pertence ao escopo local dessa função e só pode ser usada dentro dela.
def myFunc():
    x = 300     # Variável de escopo local
    print(x)
    def myInnerFunc():  # Função dentro da função
        print(x)    # A variável x não está disponível fora da função, mas está disponível para qualquer função dentro da função.
    myInnerFunc()   # Saída: 300

myFunc()    # Saída: 300