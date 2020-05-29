from __future__ import annotations
from Observer import Observer
from Subject import Subject
from ConcreteFactory1 import ConcreteFactory1
from ConcreteFactory2 import ConcreteFactory2
from ConcreteFactory3 import ConcreteFactory3
from ConcreteFactory4 import ConcreteFactory4

class ConcreteObserverA(Observer):

    temperatura_recebida: int = None
    umidade_recebida: int = None

    def update_temperatura(self, subject: Subject) -> None:
        self.temperatura_recebida = subject._state_temperatura
        print("Observador: Status de Temperatura recebido para analise.")
        print("Observador: Dado utilizado para tomada de medidas.")


    def update_umidade(self, subject: Subject) -> None:
        self.umidade_recebida = subject._state_umidade
        print("Observador: Status de Umidade recebido para analise.")
        print("Observador: Dado utilizado para tomada de medidas.")


    def tomada_de_medidas(self) -> None:
        if self.temperatura_recebida < 10 or self.temperatura_recebida > 38:
            print("Temperatura Critica !")
            if self.umidade_recebida <= 20:
                print("Umidade Critica !")
                # Iniciar Acoes preventivas de alta criticidade para umidade e temperatura
                medida1(ConcreteFactory1())	
            else:
                print("Umidade aceitavel.")
                # Iniciar Acoes preventivas de alta criticidade para temperatura
                # e emitir relatorio sobre umidade relativa do ar.
                medida2(ConcreteFactory2())
        else:
            print("Temperatura Aceitavel.")	
            if self.umidade_recebida <= 20:
                print("Umidade Critica !")
                # Iniciar Acoes preventivas de alta criticidade para umidade
                # e emitir relatorio sobre temperatura.	
                medida3(ConcreteFactory3())
            else:
                print("Umidade aceitavel.")
                # Emitir relatorio sobre temperatura umidade relativa do ar
                medida4(ConcreteFactory4())


def medida1 (factory: AbstractFactory) -> None:
    _wft = factory.acao_temperatura() #b1 
    _wfu = factory.acao_umidade()     #b2
    # workflow temperatura e workflow umidade
    print(_wft.workflow())
    print(_wfu.workflow())


def medida2 (factory: AbstractFactory) -> None:
    _wft = factory.acao_temperatura() #b1
    _rtu = factory.acao_umidade()     #a2
    # workflow temperatura e relatorio de umidade
    print(_wft.workflow())
    print(_rtu.relatorio())

def medida3 (factory: AbstractFactory) -> None:
    _wfu = factory.acao_umidade()     #b2
    _rtt = factory.acao_temperatura() #a1
    # workflow umidade e relatorio temperatura
    print(_wfu.workflow())
    print(_rtt.relatorio())

def medida4 (factory: AbstractFactory) -> None:
    _rtu = factory.acao_umidade()     #a1
    _rtt = factory.acao_temperatura() #a2
    # relatorios de temperatura e umidade
    print(_rtu.relatorio())
    print(_rtt.relatorio())