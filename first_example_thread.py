from threading import Thread
import random,time
consonant = 0;
vogal = 0;

anne = [chr(random.randint(65,90)) for _ in range(0,50)]

def Count_Consonant(array,consonant):
    seconds_start = time.time()
    for x in array:
        if((x != "A") and (x != "E") and (x != "I") and (x != "O") and (x != "U")):
            consonant += 1
    return print(f"Total de Consoantes encontradas --> {consonant}\tSegundos --> {(time.time()-seconds_start)}");

def Count_Vogal(array,vogal):
    seconds_start = time.time()
    for y in array:
        if(y == "A" or y == "E" or y == "I" or y == "O" or y == "U"):
            vogal += 1;
    return print(f"Total de Vogais encontradas --> {vogal}\t\tSegundos --> {(time.time()-seconds_start)}");

def BubbleSort(array):
    seconds_start = time.time()
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return print(f"Ordenação da Array --> Concluída\t\tSegundos --> {(time.time()-seconds_start)}\n\n{anne}")

consonant = Thread(target=Count_Consonant,args=[anne,consonant]);
vogal = Thread(target=Count_Vogal,args=[anne,vogal]);
paitaon = Thread(target=BubbleSort,args=[anne]);

consonant.start()
vogal.start()
paitaon.start()




