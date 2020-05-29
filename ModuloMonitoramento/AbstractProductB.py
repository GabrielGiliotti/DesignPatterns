from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractProductB(ABC):
    """
    Interface para as acoes relacionadas a umidade
    """

    @abstractmethod
    def workflow(self) -> str:
        pass

    # Alem das fabricas abstratas, que criam um produto de acordo com o contexto, temos tambem a interface
    # para os produtos. Essa classe seria correspondente a Interface Checkbox

