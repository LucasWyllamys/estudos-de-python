# Como verificar se uma string está dentro de outra
txt = 'Isso é uma string'
print('uma' in txt)     # Saída: True
print('carro' in txt)   # Saída: False
# Usando if
if 'é' in txt:
  print('A string "é" está presente!')

# Como verificar se uma string não está dentro de outra
txt = 'Isso é uma string'
print('uma' not in txt)       # Saída: False
print('carro' not in txt)     # Saída: True
# Usando if
if 'carro' not in txt:
  print('A string "é" não está presente!')