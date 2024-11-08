'''
Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.

Recursão é um conceito matemático e de programação comum. Isso significa que uma função chama a si mesma. Isso tem o benefício de significar que você pode fazer um loop pelos dados para chegar a um resultado.

O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escorregar para escrever uma função que nunca termina, ou uma que usa quantidades excessivas de memória ou poder do processador. No entanto, quando escrita corretamente, a recursão pode ser uma abordagem muito eficiente e matematicamente elegante para a programação.

Neste exemplo, tri_recursion() é uma função que definimos para chamar a si mesma ("recurse"). Usamos a variável k como os dados, que decrementa ( -1 ) toda vez que recursionamos. A recursão termina quando a condição não é maior que 0 (ou seja, quando é 0).

Para um novo desenvolvedor, pode levar algum tempo para descobrir exatamente como isso funciona. A melhor maneira de descobrir é testando e modificando.
'''
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0

    return result

tri_recursion(6)
''' Saída:
1
3
6
10
15
21
'''