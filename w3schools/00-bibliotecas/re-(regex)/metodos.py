'''
Método          Descrição
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

''' Principais métodos
Método          Descrição 
fidall()        Retorna uma lista contendo todas as correspondências.           
search()        Retorna um objeto Match se houver uma correspondência em qualquer lugar da string.
split()         Retorna uma lista onde a string foi dividida em cada correspondência.
sub()           Substitui uma ou muitas correspondências por uma string.
'''
