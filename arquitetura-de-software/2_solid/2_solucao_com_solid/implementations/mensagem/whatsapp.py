import logging
from interfaces.mensagem import iMensagem

logging.basicConfig(level=logging.DEBUG)    # Configuração do log. Define onde o log será escrito.

# Implementação da interface (iMensagem):
class WhatsApp(iMensagem):
    def __init__(self):
        super().__init__()
        logging.debug("Estabelece as conexões com o WhatsApp.")

    def enviar(self, parametros: dict):
        logging.debug(f"Envia mensagem pelo WhatsApp:")
        logging.debug(f"\tNúmero do WhatsApp: {parametros["numero_celular"]}")
        logging.debug(f"\tMensagem: {parametros["mensagem"]}")
        if parametros["caminho_anexo"]: self.anexar(parametros["caminho_anexo"])

    def anexar(self, caminho_anexo: str):
        logging.debug(f"\tAnexo: {caminho_anexo}")