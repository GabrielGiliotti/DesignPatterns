from __future__ import annotations
from ConcreteSubject import ConcreteSubject
from ConcreteFactory1 import ConcreteFactory1
from ConcreteFactory2 import ConcreteFactory2
from ConcreteObserverA import ConcreteObserverA

def main():

	# Instancia observador e fornece dados de temperatura e umidade
	subject = ConcreteSubject()
	observer_a = ConcreteObserverA()
	subject.attach(observer_a)
	subject.evento_de_temperatura()
	subject.evento_de_umidade()
	observer_a.tomada_de_medidas()


if __name__ == "__main__":
    main()