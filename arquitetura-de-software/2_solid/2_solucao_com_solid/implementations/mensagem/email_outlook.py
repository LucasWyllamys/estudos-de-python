import logging
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
print(os.getcwd())
from interfaces.mensagem import iMensagem

logging.basicConfig(level=logging.DEBUG)    # Configuração do log. Define onde o log será escrito.

# Implementação da interface (iMensagem):
class EmailOutlook(iMensagem):
    def __init__(self):
        super().__init__()
        logging.debug("Estabelece as conexões com o servidor de e-mail OUTLOOK.")

    def enviar(self, parametros: dict):
        logging.debug(f"Envia e-mail via Outlook:")
        logging.debug(f"\tDestinatário: {parametros["destinatario"]}")
        logging.debug(f"\tAssunto: {parametros["assunto"]}")
        logging.debug(f"\tCorpo: {parametros["corpo"]}")
        if parametros["caminho_anexo"]: self.anexar(parametros["caminho_anexo"])

    def anexar(self, caminho_anexo: str):
        logging.debug(f"\tAnexo: {caminho_anexo}")