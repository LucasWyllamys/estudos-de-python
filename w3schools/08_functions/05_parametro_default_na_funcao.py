# O exemplo a seguir mostra como usar um valor de parâmetro padrão.
# Se chamarmos a função sem argumento, ela usará o valor padrão:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")   # Saída: I am from Sweden
my_function("India")    # Saída: I am from India
my_function()           # Saída: I am from Norway
my_function("Brazil")   # Saída: I am from Brazil