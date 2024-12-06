# O método intersection() retornará um novo conjunto, que contém apenas os itens que estão presentes em ambos os conjuntos:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)  # Saída: {'apple'}

# Você pode usar o operador & em vez do método intersection() e obterá o mesmo resultado:
# O operador & só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método intersection().
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)  # Saída: {'apple'}

# O método intersection_update() também manterá SOMENTE as duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)  # Saída: {'apple'}

# Os valores True e 1 são considerados o mesmo valor. O mesmo vale para False e 0:
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)  # Saída: {False, 1, 'apple'}
