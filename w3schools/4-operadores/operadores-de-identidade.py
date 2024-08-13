''' Operadores de identidade são usados para comparar os objetos, não se eles são iguais, mas se eles são realmente o mesmo objeto, com o mesmo local de memória:
Operator	    Description	                                                        Example
is 	            Retorna True se ambas as variáveis forem o mesmo objeto	            x is y	
is not	        Retorna True se ambas as variáveis não forem o mesmo objeto	        x is not y
'''
# Exemplo:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # Retorna True porque z é o mesmo objeto que x
print(x is y)   # Retorna False porque x não é o mesmo objeto que y, mesmo que tenham o mesmo conteúdo
print(x == y)   # Para demonstrar a diferença entre "is" e "==": esta comparação retorna True porque x é igual a y