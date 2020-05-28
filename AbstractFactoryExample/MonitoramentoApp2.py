from __future__ import annotations
from ConcreteFactory1 import ConcreteFactory1
from ConcreteFactory2 import ConcreteFactory2

def client_code_main(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code_main(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code_main(ConcreteFactory2())

# Classe correspondente a aplicacao ou metodo main, isto eh, pode ser tudo inserido na main para
# Fazer com que o AbstractFactory funcione, mas mantive o padrao do site.

# Mapeamento:

# MapeamentoApp2    <-->  Application
# AbstractFactory   <-->  GUIFactory  (Interface)
# ConcreteFactory1  <-->  WinFactory  (Implementa interface GUIFactory)
# ConcreteFactory2  <-->  MacFactory  (Implementa interface GUIFactory)
# AbstractProductA  <-->  Button      (Interface)
# AbstractProductB  <-->  Checkbox    (Interface)
# ConcreteProductA1 <-->  WinButton   (Implementa interface Button)
# ConcreteProductA2 <-->  MacButton   (Implementa interface Button)
# ConcreteProductB1 <-->  WinCheckbox (Implementa interface Checkbox)
# ConcreteProductB2 <-->  MacCheckbox (Implementa interface Checkbox)