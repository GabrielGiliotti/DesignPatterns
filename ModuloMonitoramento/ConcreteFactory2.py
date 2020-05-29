from AbstractFactory import AbstractFactory
from ConcreteProductA2 import ConcreteProductA2
from ConcreteProductB1 import ConcreteProductB1

class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def acao_temperatura(self) -> ConcreteProductB1:
        return ConcreteProductB1()



    def acao_umidade(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    # Correspondente a uma das classes concretas que herdam da Interface GUIFactory, ou AbstractFactory no caso
    # Poderia ser a MacFactory do Exemplo 