import logging
from interfaces.mensagem import iMensagem

logging.basicConfig(level=logging.DEBUG)    # Configuração do log. Define onde o log será escrito.

# Implementação da interface (iMensagem):
class SMS(iMensagem):
    def __init__(self):
        super().__init__()
        logging.debug("Estabelece as conexões com o SMS.")

    def enviar(self, parametros: dict):
        logging.debug(f"Envia mensagem pelo SMS:")
        logging.debug(f"\tNúmero do Telefone: {parametros["numero_celular"]}")
        logging.debug(f"\tMensagem: {parametros["mensagem"]}")