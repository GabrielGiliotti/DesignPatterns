from __future__ import annotations
from AbstractProductB import AbstractProductB

class ConcreteProductB2(AbstractProductB):
    def workflow(self) -> str:
        return "O Workflow de medidas preventivas para Umidade sera iniciado em instantes."

    # Havendo a interface do produto, existe a implementacao do produto que possivelmente pode ser retornada
    # Se a Fabrica entender que e necessaio trazer o produto. Essa Classe corresponde ao MacCheckBox.
    # Nesse exemplo, o produto B2 interage com um produto A1 ou A2, diferente do exemplo dos botoes, que são isolados.