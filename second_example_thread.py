from threading import Thread
import random
import queue
import time
import os

jogadores = []
tempo = []
dinheiro = []
resultado = list()
numeros_random = [random.randint(1,6) for _ in range(500)]
tabuleiro = [list() for s in range(100)]

class Jogador:
    def __init__(self,nickname):
        self.nickname = nickname
        self.money = 0
        self.index = 0
        self.status = "Livre"
    
    def Play(self):
        dado1 = random.choice(numeros_random)
        dado2 = random.choice(numeros_random)
        print(f"\nJogador: { self.nickname }\n    Dado 1: {dado1}\n    Dado 2: {dado2}\n    Status: {self.status}\n    Posição: {self.index}\n    Dinheiro: {self.money}\n")
        return dado1,dado2

    def Repeated(self,dados):
        if self.status == "Livre" and dados[0] == dados[1]:
            self.status = "Preso"
            play_again = self.Play()
            self.Repeated(play_again)
        elif self.status == "Preso" and dados[0] != dados[1]:
            play_again = self.Play()
            self.Repeated(play_again)
        elif self.status == "Preso" and dados[0] == dados[1]:
            self.status = "Livre"
        elif self.status == "Livre" and dados[0] != dados[1]:
            if self.index+(dados[0]+dados[1]) >= len(tabuleiro):
                self.index = len(tabuleiro)
            else:
                self.index = self.index +(dados[0] + dados[1])
                if self.index % 2 == 0:
                    self.money = (self.money + 79.99)
                else:
                    self.money = (self.money + 53.21)

def Board(Jogador,First):
    timer = time.time()
    while(1):
        Jogador.Repeated(Jogador.Play())
        for i in tabuleiro:                                      
                for j in i:
                    if Jogador.nickname == j:
                        i.remove(Jogador.nickname)
        if(Jogador.index < len(tabuleiro)):       
            tabuleiro[Jogador.index].append(Jogador.nickname)
        else:
            tabuleiro[len(tabuleiro)-1].append(Jogador.nickname)
        print(tabuleiro)
        
        if Jogador.index >= len(tabuleiro):
            print(f"\nThread finalizada --> {Jogador.nickname}!\n")
            tempo = time.time() - timer;
            First.put([Jogador.nickname,Jogador.money,tempo])
            break
        
if __name__ == "__main__":
    menu = int(input("Menu\n1)Jogar\n2)Sair\nOpção --> "))
    os.system("cls")
    while(menu != 2):
        submenu = int(input("Menu dos Jogadores\n1) Adicionar jogador\n2) Listar jogadores\n3) Excluir jogador\n4) Start!\n5) Sair\nOpção --> "))
        if(submenu == 1):
            os.system('cls')
            nickname = input("Digite o nickname --> ")
            jogadores.append(Jogador(nickname))
            os.system('cls')
            print("Jogador adicionado com sucesso!")
        if(submenu == 2):
            os.system('cls')
            if(len(jogadores) != 0):
                for x in jogadores:
                    print(f"Nickname: {x.nickname} | Money: {x.money}\n")
            else:
                print("Lista de jogadores vazia!")
        if(submenu == 3):
            os.system('cls')
            excluir_player = input("Digite o nickname do jogador que você deseja excluir --> ")
            for y in jogadores:
                if(excluir_player == y.nickname):
                    jogadores.pop(jogadores.index(y))
                    print("Jogador excluído com sucesso!")
                else:
                    print("Jogador não encontrado!")
        if(submenu == 4):
            for q in jogadores:
                tabuleiro[0].append(q.nickname)
            first = queue.Queue()
            thread_1 = Thread(target=Board,args=[jogadores[0],first])
            thread_2 = Thread(target=Board,args=[jogadores[1],first])
            thread_3 = Thread(target=Board,args=[jogadores[2],first])
            thread_4 = Thread(target=Board,args=[jogadores[3],first])
    
            thread_1.start()
            thread_2.start()
            thread_3.start()
            thread_4.start()
            
            thread_1.join()
            thread_2.join()
            thread_3.join()
            thread_4.join()


            for p in range(len(jogadores)):
                resultado.append(first.get())
                
            for u in resultado:
                dinheiro.append(u[1])
                tempo.append(u[2])
                print(f"| Jogador: {u[0]} | Tempo: {u[2]} | Montante: R${u[1]} |");

            maximo = max(dinheiro)
            minimo = min(tempo)
            index = dinheiro.index(maximo)
            index_tempo = tempo.index(minimo)
            print(f"\nJogador mais rápido --> {resultado[index_tempo][0]}")
            print(f"\nMontante mais valioso --> {maximo} pertencente à {resultado[index][0]}")
            break;
        if(submenu == 5):
            os.system('clear')
            print("Saindo...")
            time.sleep(0.5)
            break;
