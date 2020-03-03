from threading import Thread
import os
import time
import random

tabuleiro = [0 for _ in range(100)]
jogadores = []

class Jogador:
    def __init__(self,nickname,money,index,status):
        self.nickname = nickname;
        self.index = index;
        self.money = money;
        self.status = status;

def Tabuleiro(Jogador):
    print(Jogador.nickname)

if __name__ == "__main__":
    menu = int(input("Menu\n1)Jogar\n2)Sair\nOpção --> "))
    os.system("clear")
    while(menu != 2):
        submenu = int(input("Menu dos Jogadores\n1) Adicionar jogador\n2) Listar jogadores\n3) Excluir jogador\n4) Start!\n5) Sair\nOpção --> "))
        if(submenu == 1):
            os.system('clear')                      
            nickname = input("Digite o nickname --> ")
            jogadores.append(Jogador(nickname,0,0,"Livre"))
            print("Jogador adicionado com sucesso!")
        if(submenu == 2):
            os.system('clear')
            if(len(jogadores) != 0):
                for x in jogadores:
                    print(f"Nickname: {x.nickname} | Money: {x.money}\n")
            else:
                print("Lista de jogadores vazia!")
        if(submenu == 3):
            os.system('clear')
            excluir_player = input("Digite o nickname do jogador que você deseja excluir --> ")
            for y in jogadores:
                if(excluir_player == y.nickname):
                    jogadores.pop(jogadores.index(y))
                    print("Jogador excluído com sucesso!")
                else:
                    print("Jogador não encontrado!")
        if(submenu == 4):
            for a in jogadores:
                Tabuleiro(a)
        if(submenu == 5):
            os.system('clear')
            print("Saindo...")
            time.sleep(0.3)
            break;
