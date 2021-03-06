from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC): 
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def acao_temperatura(self) -> AbstractProductA:
        pass

    @abstractmethod
    def acao_umidade(self) -> AbstractProductB:
        pass

    # Classe correspondente à Interface GUIInterface, onde a aplicação deve estar associada para instanciar um objeto
    # Independente do tipo que será retornado