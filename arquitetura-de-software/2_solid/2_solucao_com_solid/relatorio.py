''' SOLID:
    - SRP: Uma classe, módulo, componente, função, entidade etc., deve ter apenas uma responsabilidade, ou seja, deve ter apenas um motivo para ser modificada.
    - OCP: Classes, objetos, métodos, entidades, funções etc., devem estar abertos para extensão, mas fechados para modificações.
    - LSP: Classes derivadas devem ser capazes de substituir totalmente classes-bases.
    - ISP: As classes não devem ser forçadas a depender de interfaces que não utilizam.
    - DIP: Módulos de alto nível não devem ser dependentes de módulos de baixo nível; ambos devem depender de abstrações. Detalhes devem depender de abstrações, não o inverso.
'''

class Relatorio:
    def __init__(self):
        pass

    def generate(self):
        print("Gerando relatório...")

    def display(self):
        print("Exibindo relatório...")