# Uma variável só está disponível de dentro da região em que foi criada. Isso é chamado de escopo.

# Uma variável criada no corpo principal do código Python é uma variável global e pertence ao escopo global.
# Variáveis ​​globais estão disponíveis em qualquer escopo, global e local.
x = 300     # Variável de escopo global

def myFunc():
    print(x)    # escopo local

myFunc()    # Saída: 300

print(x)    # Saída: 300 (escopo global)

# Se você operar com o mesmo nome de variável dentro e fora de uma função, o Python as tratará como duas variáveis ​​separadas, uma disponível no escopo global (fora da função) e outra disponível no escopo local (dentro da função):
x = 300     # Variável de escopo global

def myFunc():
    x = 200     # Variável de escopo local
    print(x)

myFunc()    # Saída: 200

print(x)    # Saída: 300

# Se você precisar criar uma variável global, mas estiver preso no escopo local, você pode usar a palavra-chave global:
x = 200

def myFunc():
    global y    # A palavra-chave global torna a variável global.
    y = 300
    global x    # Use a palavra-chave global se quiser fazer uma alteração em uma variável global dentro de uma função.
    x = 400

myFunc()

print(y)    # Saída: 300
