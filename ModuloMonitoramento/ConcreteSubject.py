from __future__ import annotations
from random import randrange
from Subject import Subject

class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state_temperatura: int = None
    _state_umidade: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Gerenciador de Evento: Um observador foi registrado.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Gerenciador de Evento: Um observador foi removido.")
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify_temperatura(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        print("Gerenciador de Evento: Atualizando Observador sobre condicoes climaticas...")
        for observer in self._observers:
            observer.update_temperatura(self)


    def notify_umidade(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        print("Gerenciador de Evento: Atualizando Observador sobre condicoes climaticas...")
        for observer in self._observers:
            observer.update_umidade(self)


    def evento_de_temperatura(self) -> None:
        
        print("\nGerenciador de Evento: Recebendo dados dos Sensores de Temperatura.")
        self._state_temperatura = randrange(-10, 50)

        print(f"Gerenciador de Evento: Temperatura Media calculada: {self._state_temperatura} ºC")
        self.notify_temperatura()

    def evento_de_umidade(self) -> None:
        
        print("\nGerenciador de Evento: Recebendo dados dos Sensores de Umidade.")
        self._state_umidade = randrange(0, 100)

        print(f"Gerenciador de Evento: Umidade relativa calculada: {self._state_umidade} %")
        self.notify_umidade()