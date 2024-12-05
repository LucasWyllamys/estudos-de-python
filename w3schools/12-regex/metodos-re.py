'''
Método              Descrição
re.compile()        Compila um padrão de expressão regular em um objeto de expressão regular, que pode ser usado para realizar correspondências.
re.match()          Verifica se o padrão corresponde ao início da string. Retorna um objeto match ou None.
re.fullmatch()      Verifica se o padrão corresponde à string inteira. Retorna um objeto match ou None.
re.search()         Procura pelo padrão em qualquer parte da string. Retorna o primeiro objeto match encontrado ou None.
re.findall()        Encontra todas as ocorrências do padrão na string e retorna uma lista de correspondências.
re.finditer()       Encontra todas as ocorrências do padrão e retorna um iterador com objetos match.
re.sub()            Substitui as ocorrências do padrão na string por uma nova string (repl). O parâmetro count limita o número de substituições.
re.subn()           Semelhante a re.sub, mas retorna uma tupla contendo a string modificada e o número de substituições feitas.
re.split()          Divide a string com base no padrão e retorna uma lista das partes. O parâmetro maxsplit limita o número de divisões.
re.escape()         Escapa todos os caracteres não alfanuméricos na string, tornando-a segura para uso em uma expressão regular.
re.purge()          Limpa o cache de expressões regulares compiladas.
re.error            Exceção levantada para erros relacionados a expressões regulares.
'''

# O Python tem uma biblioteca integrada chamada re, que pode ser usada para trabalhar com expressões regulares.
import re

string = "Lucas Wyllamys Carmo da Silva - Lucas Wyllamys"

padrao = re.compile("Lucas Wyllamys")

result = re.fullmatch(padrao, string)  
print(result)   # Saída: None

result = re.search(padrao, string)
print(result)   # Saída: <re.Match object; span=(0, 14), match='Lucas Wyllamys'>. O atributo span indica onde que a string começa e termina (o valor de término não entra na conta!).

result = re.findall(padrao, string)
print(result)   # Saída: ['Lucas Wyllamys', 'Lucas Wyllamys']

