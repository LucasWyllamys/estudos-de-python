''' SOLID:
    - SRP: Uma classe, módulo, componente, função, entidade etc., deve ter apenas uma responsabilidade, ou seja, deve ter apenas um motivo para ser modificada.
    - OCP: Classes, objetos, métodos, entidades, funções etc., devem estar abertos para extensão, mas fechados para modificações.
    - LSP: Classes derivadas devem ser capazes de substituir totalmente classes-bases.
    - ISP: As classes não devem ser forçadas a depender de interfaces que não utilizam.
    - DIP: Módulos de alto nível não devem ser dependentes de módulos de baixo nível; ambos devem depender de abstrações. Detalhes devem depender de abstrações, não o inverso.
'''
from repositorio import Repositorio

class Relatorio:
    def __init__(self):
        self.caminho_relatorio = ""

    def gerar(self, dados, caminho_template: str):
        self.__carregar_template(caminho_template)
        self.__renderizar(dados)
        self.__salvar(Repositorio().caminho_repositorio)

    @staticmethod
    def __carregar_template(caminho_template):
        print(f"Carrega o template: {caminho_template}")

    @staticmethod
    def __renderizar(dados):
        print(f"Renderiza os dados: {dados}")

    def __salvar(self, caminho_repositorio):
        self.caminho_relatorio = caminho_repositorio + r"\relatorios\relatorio.pdf"
        print(f"Salva o relatório: {self.caminho_relatorio}, no repositório: {caminho_repositorio}")

    def exibir(self):
        print(f"Exibe o relatório: {self.caminho_relatorio}")