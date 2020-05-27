from ConcreteSubject import ConcreteSubject
from ConcreteObserverA import ConcreteObserverA
from ConcreteObserverB import ConcreteObserverB

def main():
    
    print("Local onde vamos inserir os valores dos sensores.")

if __name__ == "__main__":
    
    main()
    # The client code.

    subject = ConcreteSubject() # Correspondente ao EventManager: Gerencia inscrições, notificações

    observer_a = ConcreteObserverA() # Correspondente a um tipo de Listener: O Objeto que sera inscrito para receber notificações
    subject.attach(observer_a)		 # Ou outras ações

    observer_b = ConcreteObserverB() # Correspondente a um tipo de Listener: O Objeto que sera inscrito para receber notificações
    subject.attach(observer_b)       # Ou outras ações

    subject.some_business_logic()  # Vamos supor que a logica de negocio é o evento de recepcao de sinal dos sensores
    subject.some_business_logic()  # Entao o sensores recebem um sinal (valores que posso passar por parametro), analisam se é um 
    							   # sinal Com Criticidade Baixa ou Alta, e a partir disso, notifica os Listerners (De acordo com 
    subject.detach(observer_a)     # a necessidade).

    subject.some_business_logic()  # Mapeando os entidade para construir a estrutura depois
    							   # Classe Observer <--> interface EventListener
    							   # ConcreteObeserverA <--> Listener qualquer (Baixa Criticidade)
    							   # ConcreteObeserverB <--> Listener qualquer (Alta Criticidade)
    							   # ConcreteSubject <--> EventManager 
    							   # Subject <--> interface para definir as acoes que o EventManager pode realizar, como por exemplo
    							   # Attach Observer, Detach Observer, Notify Observer, etc (Posso definir mais ações)

    							   # No exemplo do site, Editor é uma extensão da logica de negocio, isto eh, poderia herdar EventManager
    							   # E, além de conter todas as ações do Manager, poderia oferecer mais ações. No caso do site, foi 
    							   # realizada uma composição onde, dentro do Editor existe um objeto EventManager
    							   # No meu caso seriam os sensores, mas provavelmente farei tudo dentro do Manager.