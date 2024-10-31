# Você pode acessar itens de tupla consultando o número do índice, dentro de colchetes:
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1])  # Saída: banana (obs.: O primeiro item tem índice 0)

# Indexação negativa significa começar do fim.
# -1 refere-se ao último item, -2 refere-se ao penúltimo item etc.
thisTuple = ("maçã", "banana", "laranja")
print(thisTuple[-1])  # Saída: laranja

# Intervalo de índices:
# Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo.
# Ao especificar um intervalo, o valor de retorno será uma nova tupla com os itens especificados.
# Observação: a pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).
# Lembre-se de que o primeiro item tem índice 0.
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mago")
print(thisTuple[2:5])  # Saída: ('cherry', 'orange', 'kiwi')

# Ao deixar de fora o valor inicial, o intervalo começará no primeiro item:
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mago")
print(thisTuple[:4])  # Saída: ('apple', 'banana', 'cherry', 'orange')

# Ao deixar de fora o valor final, o intervalo continuará até o final da tupla:
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mago")
print(thisTuple[2:])  # Saída: ('cherry', 'orange', 'kiwi', 'melon', 'mago')

# Especifique índices negativos se quiser iniciar a pesquisa a partir do final da tupla:
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mago")
print(thisTuple[-4:-1])  # Saída: ('orange', 'kiwi', 'melon')
