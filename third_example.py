from threading import Thread
import tkinter
import random
import time
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

sort1 = [random.randint(0,400) for _ in range(200)]

class Increment_Count:
    def __init__(self, parent):
        self.count = 0;
        self.time = 60;
        self.labeltext = tk.Button(parent,text="Tempo:60",width=7, height=1)
        self.labeltext.place(x=5,y=5)
        self.label = tk.Button(parent, text="Contador:0",command=self.refresh_label)
        self.label.pack()

    def count_timer(self):
        while(self.time > 0):
            time.sleep(1)
            self.time -= 1;
            self.labeltext.configure(text="Tempo:%i" % self.time)
        root.quit()

    def refresh_label(self):
        self.label.configure(text="Contador:%i" % self.count)
        self.label.place(x=random.choice(sort1),y=random.choice(sort1))
        self.count += 1;
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Trabalho Doido do Casseb")
    root.geometry("500x500")
    timer = Increment_Count(root)
    a = Thread(target=timer.count_timer)
    b = Thread(target=timer.refresh_label)
    a.start()
    b.start()

    root.mainloop() 