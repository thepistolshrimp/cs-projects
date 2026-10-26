import java.util.*;

//Oppgave 6 FLettetråd

public class Flettetrad implements Runnable {
    Monitor monitor;

    public Flettetrad(Monitor m) {
        monitor = m;
    }

    @Override
    public void run() {
        try {
            while (true) {
                ArrayList <Frekvenstabell> skalFlettes = monitor.taUtTo();  
                if (skalFlettes == null) {
                    break;
                }  
                
                Frekvenstabell flettet = Frekvenstabell.flett(skalFlettes.get(0), skalFlettes.get(1));

                monitor.settInn(flettet);
            }

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}







                


