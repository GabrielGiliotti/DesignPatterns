from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


    # Alem das fabricas abstratas, que criam um produto de acordo com o contexto, temos tambem a interface
    # para os produtos. Essa classe seria correspondente a Interface Button 