from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.DEBUG)    # Configuração do log. Define onde o log será escrito.

# Interface (classe abstrata) (contrato público claro): 
class iImpressora(ABC):
    @abstractmethod         
    def imprimir(self, caminho_relatorio: str):
        pass

# Implementação da interface:
class ImpressoraA(iImpressora):
    def __init__(self):
        super().__init__()
        logging.debug("Configurações iniciais para conexão com a impressora A.")

    def imprimir(self, caminho_relatorio: str):
        logging.debug(f"Imprime o relatório: {caminho_relatorio}")

# Implementação da interface:
class ImpressoraB(iImpressora):
    def __init__(self):
        super().__init__()
        logging.debug("Configurações iniciais para conexão com a impressora B.")

    def imprimir(self, caminho_relatorio: str):
        logging.debug(f"Imprime o relatório: {caminho_relatorio}")