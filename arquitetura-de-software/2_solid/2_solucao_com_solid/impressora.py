from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.DEBUG)

# Interface (classe abstrata) (contrato público claro): 
class iImpressora(ABC):
    @abstractmethod         
    def imprimir(self, caminho_relatorio):
        pass

# Implementação da interface:
class ImpressoraA(iImpressora):
    def __init__(self):
        logging.debug("Estabelece as conexões com a impressora A.")

    def imprimir(self, caminho_relatorio):
        logging.debug(f"Imprime o relatório: {caminho_relatorio}")

# Implementação da interface:
class ImpressoraB(iImpressora):
    def __init__(self):
        logging.debug("Estabelece as conexões com a impressora B.")

    def imprimir(self, caminho_relatorio):
        logging.debug(f"Imprime o relatório: {caminho_relatorio}")