from abc import ABC, abstractmethod
from Subject import Subject

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update_temperatura(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass

    @abstractmethod
    def update_umidade(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""