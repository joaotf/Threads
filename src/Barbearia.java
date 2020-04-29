package Barbeiro_Dorminhoco;

import java.util.Random;

public class Barbearia implements Runnable {
    private final int cadeiras_Espera;
    boolean cadeira_Ocupada = false;
    int[] clientes;
    boolean baiano = false;
    private final String nome;
    private final int clientes_novos;
    int numero_clientes;

    Barbearia(final String nome, final int cadeiras_Espera, final int clientes){
        clientes_novos = clientes;
        this.nome = nome;
        this.cadeiras_Espera = cadeiras_Espera;
        System.out.println("O "+nome+" abriu a barbearia!\n");
        System.out.println("----------------------------------------------------------------");
 
    }

    public void Clientes(){
        final Random random = new Random();
        numero_clientes = random.nextInt(clientes_novos);
        clientes = new int[numero_clientes];

        for (int i = 0; numero_clientes < clientes.length; i++) {
            clientes[i] = i;
        }
    }

    public void BaianoPegouNoSono() throws InterruptedException {
        System.out.println("Nenhum cliente na barbearia! O baiano pode dormir em paz!\n");
        System.out.println("O baiano (dormindo) está esperando os clientes!\n");
        Thread.sleep(7000);
        System.out.println("Baiano disponível!\n");
 
        Clientes();
    }

    public void BaianoAcordou() throws InterruptedException {
        if(numero_clientes != 0){
          if(numero_clientes > 1 && cadeira_Ocupada == false){
            System.out.println("Entrou(aram) "+ numero_clientes + " cliente(s) na barbearia!\n");
          }else{
            System.out.println("Existe(m) "+ numero_clientes + " cliente(s) esperando!\n");
          }
   
        System.out.println("Um cliente ocupou a cadeira do Barbeiro e está sendo atendido!\n");
        numero_clientes--;
        cadeira_Ocupada = true;
        Thread.sleep(4000);

        if(numero_clientes > cadeiras_Espera){
          final int clients = numero_clientes - cadeiras_Espera;
          numero_clientes -= clients;
          
          for (int i = 0; i < clientes.length; i++) {
              clientes[i] = 0;
          }
          for (int j = 0; j < numero_clientes; j++) {
              clientes[j] = j + 1;
          }
          System.out.println(clients + " cliente(s) foram(oi) embora\n");

          System.out.println("Existe(m) "+ numero_clientes + " cliente(s) esperando!\n");
        }

        System.out.println("O cliente que ocupava a cadeira do Barbeiro já foi atendido!\n");
    }else if (numero_clientes == 1){
        System.out.println("A cadeira do Barbeiro está disponível!\n");
        System.out.println("A cadeira do Barbeiro está ocupada, sem clientes esperando!\n");
        Thread.sleep(4000);
        numero_clientes--;
        System.out.println("O cliente que ocupava a cadeira do Barbeiro já foi atendido!\n");
    }else {
      System.out.println("A cadeira do Barbeiro está disponível!\n");
      cadeira_Ocupada = false;
    }
}

@Override
	public void run() {
		while(true){
      if (numero_clientes <= 0){
        try {
          BaianoPegouNoSono();
        } catch (final InterruptedException e) {
          System.err.println(e);
        }
      }else{
        try {
          BaianoAcordou();
        } catch (final InterruptedException e) {
            System.err.println(e);
        }
      }
    }
  }
}