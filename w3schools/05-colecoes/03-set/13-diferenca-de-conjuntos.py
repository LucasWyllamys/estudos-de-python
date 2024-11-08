# O método difference() retornará um novo conjunto que conterá apenas os itens do primeiro conjunto que não estão presentes no outro conjunto:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)  # Saída: {'cherry', 'banana'}

# Você pode usar o operador - em vez do método difference() e obterá o mesmo resultado.
# O operador - só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método difference().
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)  # Saída: {'cherry', 'banana'}

# O método difference_update() também manterá os itens do primeiro conjunto que não estão no outro conjunto, mas alterará o conjunto original em vez de retornar um novo conjunto:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)  # Saída: {'banana', 'cherry'}

# O método symmetric_difference() manterá apenas os elementos que NÃO estão presentes em ambos os conjuntos:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)  # Saída: {'microsoft', 'banana', 'cherry', 'google'}

# Você pode usar o operador ^ em vez do método symmetric_difference() e obterá o mesmo resultado.
# o operador ^ só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método symmetric_difference().
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)  # Saída: {'google', 'cherry', 'microsoft', 'banana'}

# O método symmetric_difference_update() também manterá tudo, exceto as duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)   # Saída: {'microsoft', 'google', 'cherry', 'banana'}
