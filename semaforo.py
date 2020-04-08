from threading import Thread
import time

class Semaforo:
    def __init__(self,nome,status):
        self.nome = nome;
        self.status = status;
    
    def setStatus(self,status):
        self.status = status;
    
    def getStatus(self):
        return self.status;

    def setNome(self,nome):
        self.nome = nome;
    
    def getNome(self):
        return self.nome;


    def cycleOfLife(self,nome,status):
        for x in range(100):
            if(self.status == "VERDE"):
                print("-------------------------------------")
                print(f"{self.nome} | " , "Status [ ",self.status," ]")
                time.sleep(3)
                print("-------------------------------------")
                self.status = "AMARELO";
                print(f"{self.nome} | " , "Status [ ",self.status," ]")
                time.sleep(2);
                print("-------------------------------------")
                self.status = "VERMELHO";
                print(f"{self.nome} | " , "Status [ ",self.status," ]")
                time.sleep(5);
            
            if(self.status == "VERMELHO"):
                print("-------------------------------------")
                print(f"{self.nome} | " , "Status [ ",self.status," ]")
                time.sleep(5)
                print("-------------------------------------")
                self.status = "AMARELO";
                print(f"{self.nome} | " , "Status [ ",self.status," ]")
                time.sleep(2);
                print("-------------------------------------")
                self.status = "VERDE";
                print(f"{self.nome} | " , "Status [ ",self.status," ]")
                time.sleep(3);
            

semaforo1 = Semaforo("Semáforo 1","VERDE");
semaforo2 = Semaforo("Semáforo 2","VERMELHO")

semaforo_one = Thread(target=semaforo1.cycleOfLife,args=[semaforo1.getNome(),semaforo1.getStatus()])
semaforo_two = Thread(target=semaforo2.cycleOfLife,args=[semaforo2.getNome(),semaforo2.getStatus()])

semaforo_one.start();
semaforo_two.start();


