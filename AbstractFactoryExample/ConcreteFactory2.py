from AbstractFactory import AbstractFactory
from ConcreteProductA2 import ConcreteProductA2
from ConcreteProductB2 import ConcreteProductB2

class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()

    # Correspondente a uma das classes concretas que herdam da Interface GUIFactory, ou AbstractFactory no caso
    # Poderia ser a MacFactory do Exemplo 