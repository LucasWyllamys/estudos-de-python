'''
StringVar(): Armazenar valores associados a widgets e sincroniza mudanças entre widgets e o programa, garantindo que qualquer alteração feita no widget (pelo usuário ou pelo código) seja refletida na variável, e vice-versa.

trace("w", callback): Permite monitorar mudanças na variável e executar uma função automaticamente quando isso ocorre.
    - "w" indica que o evento será disparado quando o valor for alterado (escrito = write).
    - callback é a função que será executada.
'''