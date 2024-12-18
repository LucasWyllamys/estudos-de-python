''' O Python tem um pacote integrado chamado re, que pode ser usado para trabalhar com expressões regulares. 
Método (re)     Descrição
compile()       Compila um padrão de expressão regular em um objeto de expressão regular, que pode ser usado para realizar correspondências.
match()         Verifica se o padrão corresponde ao início da string. Retorna um objeto match ou None.
fullmatch()     Verifica se o padrão corresponde à string inteira. Retorna um objeto match ou None.
search()        Procura pelo padrão em qualquer parte da string. Retorna o primeiro objeto match encontrado ou None.
findall()       Encontra todas as ocorrências do padrão na string e retorna uma lista de correspondências.
finditer()      Encontra todas as ocorrências do padrão e retorna um iterador com objetos match.
sub()           Substitui as ocorrências do padrão na string por uma nova string (repl). O parâmetro count limita o número de substituições.
subn()          Semelhante a re.sub, mas retorna uma tupla contendo a string modificada e o número de substituições feitas.
split()         Divide a string com base no padrão e retorna uma lista das partes. O parâmetro maxsplit limita o número de divisões.
escape()        Escapa todos os caracteres não alfanuméricos na string, tornando-a segura para uso em uma expressão regular.
purge()         Limpa o cache de expressões regulares compiladas.
error           Exceção levantada para erros relacionados a expressões regulares.
'''

# Principais métodos:-----------------------------------------------------------------------------------
import re

# Exemplo com o método fidall():
string = "The rain in Spain"
lista = re.findall("ai", string)
print(lista)    # Saída: ['ai', 'ai']
# A lista contém as correspondências na ordem em que foram encontradas.
# Se nenhuma correspondência for encontrada, uma lista vazia será retornada:

# Exemplo com o método search():


# Exemplo com o método split():
    
# Exemplo com o método sub():
