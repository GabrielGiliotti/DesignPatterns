from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    """
    Interface para as acao relatorio
    """
    
    @abstractmethod
    def relatorio(self) -> str:
        pass


    # Alem das fabricas abstratas, que criam um produto de acordo com o contexto, temos tambem a interface
    # para os produtos. Essa classe seria correspondente a Interface Button 