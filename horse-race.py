from threading import Thread
import random as r
import queue;

resultado = []
random = [r.randint(1,4) for _ in range(200)]
tabuleiro = [0 for _ in range(100)]

class Horse:
    def __init__(self,nome,index,status):
        self.nome = nome;
        self.index = index;
        self.status = status;

    def setNome(self,nome):
        self.nome = nome;
    def setIndex(self,index):
        self.index = index;
    def setStatus(self,status):
        self.status = status;

    def getNome(self):
        return self.nome;
    def getIndex(self):
        return self.index;
    def getStatus(self):
        return self.status;

    def Race(self,Horse,Queue):
        playing=True;
        while(playing):
            print(f"Horse: [{Horse.getNome()}]\nIndex: [{Horse.getIndex()}]\nStatus: [{Horse.getStatus()}]")
            movimento = r.choice(random)
            if(Horse.getIndex()+movimento <= len(tabuleiro)-1):
                tabuleiro[Horse.getIndex()] = 0;
                if(Horse.getIndex() >= len(tabuleiro)-1):
                    Horse.setIndex(len(tabuleiro)-1);
                    tabuleiro[Horse.getIndex()] = Horse.getNome();
                    Horse.setStatus("Stopped")
                    print(f"Horse: [{Horse.getNome()}]\nIndex: [{Horse.getIndex()}]\nStatus: [{Horse.getStatus()}]")
                    Queue.put(f"Horse Race: {Horse.getNome()}")
                    playing = False;
                else:
                    Horse.setIndex(Horse.getIndex()+movimento)
                    Horse.setStatus("Running")
                    tabuleiro[Horse.getIndex()] = Horse.getNome()
            else:
                tabuleiro[len(tabuleiro)-1] = Horse.getNome();
                Horse.setStatus("Stopped")
                Queue.put(f"Horse Race: {Horse.getNome()}")
                break;

            print(tabuleiro)

if __name__ == "__main__":
    horse_1 = Horse("João",0,"Running")
    horse_2 = Horse("Paulo",0,"Running")
    horse_3 = Horse("Judas",0,"Running")
    horse_4 = Horse("Salomão",0,"Running")

    first = queue.Queue()
    running_horse_1 = Thread(target=horse_1.Race,args=[horse_1,first])
    running_horse_2 = Thread(target=horse_2.Race,args=[horse_2,first])
    running_horse_3 = Thread(target=horse_3.Race,args=[horse_3,first])
    running_horse_4 = Thread(target=horse_4.Race,args=[horse_4,first])

    running_horse_1.start()
    running_horse_2.start()
    running_horse_3.start()
    running_horse_4.start()

    running_horse_1.join()
    running_horse_2.join()
    running_horse_3.join()
    running_horse_4.join()

    print("\n\n\nClassificação Geral\n")
    for x in range(4):
        print(f"{x+1}° Lugar",first.get(),"\n")
