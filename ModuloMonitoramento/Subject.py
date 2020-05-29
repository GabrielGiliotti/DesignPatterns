from __future__ import annotations
from abc import ABC, abstractmethod

class Subject:

    """The Subject interface declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify_temperatura(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

    @abstractmethod
    def notify_umidade(self) -> None:
        """
        Notify all observers about an event.
        """
        pass