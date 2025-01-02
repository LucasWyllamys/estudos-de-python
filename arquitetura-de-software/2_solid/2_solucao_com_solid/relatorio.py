from template import iTemplate
from impressora import iImpressora
from interfaces.mensagem import iMensagem
import logging

logging.basicConfig(level=logging.DEBUG)    # Configuração do log. Define onde o log será escrito.

class Relatorio:
    def __init__(self, template: iTemplate, impressora: iImpressora, mensagem: iMensagem):
        self.template = template
        self.impressora = impressora
        self.mensagem = mensagem
        self.caminho_relatorio = None

    def gerar(self, caminho_template: str, dados: dict, caminho_repositorio: str):
        self.caminho_relatorio = self.template.renderizar(caminho_template, dados, caminho_repositorio)

    def exibir(self):
        logging.debug(f"Exibe o relatório: {self.caminho_relatorio}")

    def imprimir(self):
        self.impressora.imprimir(self.caminho_relatorio)

    def enviar(self, parametros: dict): 
        self.mensagem.enviar(parametros)      