from template import iTemplate
from impressora import iImpressora
import mensagem
import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG)

class Relatorio:
    def __init__(self, template: iTemplate, impressora: iImpressora, mensagem: mensagem.iMensagem):
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

    def enviar(self, destinatario: str, assunto: str, corpo: str, caminho_anexo: Optional[str] = None):
        if isinstance(self.mensagem, mensagem.iEmail):  # Verifica se self.mensagem é uma instância da classe iEmail.
            self.mensagem.enviar(destinatario, assunto, corpo, caminho_anexo)
        elif isinstance(self.mensagem, mensagem.iMensagem):  # Verifica se self.mensagem é uma instância da classe iMensagem.
            if isinstance(self.mensagem, mensagem.SMS):  # Verifica se self.mensagem é uma instância da classe SMS.
                self.mensagem.enviar(destinatario, corpo)
            else:
                self.mensagem.enviar(destinatario, corpo, caminho_anexo)