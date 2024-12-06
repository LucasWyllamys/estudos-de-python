# O método update() insere todos os itens de um conjunto em outro.
# Isso altera o conjunto original e não retorna um novo conjunto.
# Observação: ambos os métodos union() e update() excluirão quaisquer itens duplicados.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)  # Saída: {1, 'b', 2, 3, 'c', 'a'}
