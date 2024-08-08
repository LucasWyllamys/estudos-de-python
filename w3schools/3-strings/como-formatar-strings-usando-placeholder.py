# Use o f-strings ou o método format() para combinar strings e números.
idade = 36
txt = f'Meu nome é Lucas, eu tenho {idade} anos'
print(txt)  # Saída: Meu nome é Lucas, eu tenho 36 anos

# Um espaço reservado pode incluir um modificador para formatar o valor.
# Um modificador é incluído adicionando dois pontos (:) seguidos de um tipo de formatação legal, como .2f, o que significa número de ponto fixo com 2 decimais.
preco = 59
txt = f'O preco é {preco:.2f} reais'    # .2f significa número de ponto fixo com 2 decimais.   
print(txt)  # O preco é 59.00 reais

# Um espaço reservado pode conter código Python, como operações matemáticas.
txt = f'O preco é {20 * 59} reais'
print(txt)  # Saída: O preco é 1180 reais
