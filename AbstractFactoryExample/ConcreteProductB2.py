from __future__ import annotations
from AbstractProductB import AbstractProductB

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"

    # Havendo a interface do produto, existe a implementacao do produto que possivelmente pode ser retornada
    # Se a Fabrica entender que e necessaio trazer o produto. Essa Classe corresponde ao MacCheckBox.
    # Nesse exemplo, o produto B2 interage com um produto A1 ou A2, diferente do exemplo dos botoes, que são isolados.