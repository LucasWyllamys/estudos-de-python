# Como acessar um item: Os itens da lista são indexados e você pode acessá-los consultando o número do índice:
myList = ['maçã', 'banana', 'morango']
print(myList[1])    # Saída: banana (Obs.: O primeiro item tem índice 0.)

# Indexação Negativa: Indexação negativa significa começar do fim.
# -1 refere-se ao último item, -2 refere-se ao penúltimo item etc.
myList = ['maçã', 'banana', 'morango']
print(myList[-1])   # Saída: morango

# Intervalo de índices: Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo.
# Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.
myList = ['maçã', 'banana', 'morango', 'laranja', 'melão', 'manga', 'limão', 'uva']
print(myList[2:5])  # Saída: ['morango', 'laranja', 'melão'] (Obs.: a pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).)
# Lembre-se de que o primeiro item tem índice 0.

# Ao deixar de fora o valor inicial, o intervalo começará no primeiro item:
myList = ['maçã', 'banana', 'morango', 'laranja', 'melão', 'manga', 'limão', 'uva']
print(myList[:4])   # Saída: ['maçã', 'banana', 'morango', 'laranja'] (Obs.: O 4 'manga' não é incluso!)

# Ao deixar de fora o valor final, o intervalo irá para o final da lista:
myList = ['maçã', 'banana', 'morango', 'laranja', 'melão', 'manga', 'limão', 'uva']
print(myList[2:])   # Saída: ['morango', 'laranja', 'melão', 'manga', 'limão', 'uva'] (Obs.: O 2 'morango' é incluso)

# Faixa de índices negativos: Especifique índices negativos se quiser iniciar a pesquisa a partir do final da lista:
myList = ['maçã', 'banana', 'morango', 'laranja', 'melão', 'manga', 'limão', 'uva']
print(myList[-4:-1])    # Saída: ['melão', 'manga', 'limão'] (Obs.: Este exemplo retorna os itens de 'melão'(-4) para, mas NÃO incluindo 'uva'(-1))