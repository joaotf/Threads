package Barbeiro_Dorminhoco;

public class Main {
    public static void main(String args[]) {
        Barbearia baiano = new Barbearia("Baiano",5,5);
        Thread thread_do_baiano = new Thread(baiano);
        thread_do_baiano.start();
    }
}