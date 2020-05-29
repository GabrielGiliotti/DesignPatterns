from AbstractProductA import AbstractProductA

class ConcreteProductA2(AbstractProductA):
    def relatorio(self) -> str:
        return "Relatorio de Umidade sera enviado."

    # Havendo a interface do produto, existe a implementacao do produto que possivelmente pode ser retornada
    # Se a Fabrica entender que e necessaio trazer o produto. Essa Classe corresponde ao WinCheckBox