''' Um conjunto é um conjunto de caracteres dentro de um par de colchetes [] com um significado especial:
Conjunto        Descrição
[arn]	        Retorna uma correspondência onde um dos caracteres especificados (a, r ou n) está presente.
[a-n]	        Retorna uma correspondência para qualquer caractere minúsculo, em ordem alfabética entre a e n.
[^arn]	        Retorna uma correspondência para qualquer caractere EXCETO a, r e n.
[0123]	        Retorna uma correspondência onde qualquer um dos dígitos especificados (0, 1, 2 ou 3) estão presentes.
[0-9]	        Retorna uma correspondência para qualquer dígito entre 0 e 9.
[0-5][0-9]	    Retorna uma correspondência para quaisquer números de dois dígitos de 00 e 59.
[a-zA-Z]	    Retorna uma correspondência para qualquer caractere alfabeticamente entre a e z, minúsculo OU maiúsculo.
[+]	            Em conjuntos, +, *, ., |, (), $,{} não tem nenhum significado especial, então [+] significa: retornar uma correspondência para qualquer caractere + na string.
'''