from AbstractFactory import AbstractFactory
from ConcreteProductA1 import ConcreteProductA1
from ConcreteProductB1 import ConcreteProductB1

class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

    # Correspondente a uma das classes concretas que herdam da Interface GUIFactory, ou AbstractFactory no caso
    # Poderia ser a WinFactory do Exemplo 