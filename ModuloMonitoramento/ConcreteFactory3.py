from AbstractFactory import AbstractFactory
from ConcreteProductA1 import ConcreteProductA1
from ConcreteProductB2 import ConcreteProductB2

class ConcreteFactory3(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def acao_temperatura(self) -> ConcreteProductA1:
        return ConcreteProductA1()


    def acao_umidade(self) -> ConcreteProductB2:
        return ConcreteProductB2()

    # Correspondente a uma das classes concretas que herdam da Interface GUIFactory, ou AbstractFactory no caso
    # Poderia ser a WinFactory do Exemplo 