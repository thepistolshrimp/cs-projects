//Oppgave 4 Lesetrader

public class Lesetrad implements Runnable {
    
    Monitor monitor;
    String filnavn;

    public Lesetrad(String f, Monitor m) {  
        filnavn = f;
        monitor = m;
    }

    @Override
    public void run() {
        Frekvenstabell ff = Subsekvensregister.les(filnavn);
        monitor.settInn(ff);
    }
}
