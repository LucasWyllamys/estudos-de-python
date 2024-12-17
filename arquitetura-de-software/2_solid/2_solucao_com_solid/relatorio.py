class Relatorio:
    def __init__(self):
        self.caminho_relatorio = ""

    def gerar(self, dados, caminho_template: str, caminho_repositorio: str):
        self.__carregar_template(caminho_template)
        self.__renderizar(dados)
        self.__salvar(caminho_repositorio)

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