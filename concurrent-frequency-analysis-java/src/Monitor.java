import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;
import java.util.ArrayList;


//Oppgave 3 og 5 Monitor

public class Monitor {

    private final Subsekvensregister register;
    private final Lock lock;
    private final Condition nokElementer;

    public Monitor() {
        this.register = new Subsekvensregister();
        this.lock = new ReentrantLock();
        this.nokElementer = lock.newCondition();
    }

    
    public ArrayList<Frekvenstabell> taUtTo() throws InterruptedException {
        lock.lock();
        try {
            while (register.antall() < 2) {
                if (register.antall() == 1) {
                    return null;                 //viktig!!!
                }
                nokElementer.await();          //vent på beskjed, tråd sover
            }

            ArrayList<Frekvenstabell> liste = new ArrayList<>();

            liste.add(register.taUt());
            liste.add(register.taUt());

            return liste;

        } finally {
            lock.unlock();
        }
    }


    public void settInn(Frekvenstabell f) {
        lock.lock();
        try {
            register.settInn(f);
            nokElementer.signalAll();    //vekke tråder
        } finally {
            lock.unlock();
        }
    }
        

    public Frekvenstabell hentResultat() throws InterruptedException {
        lock.lock();
        try {
            while (register.antall() != 1) {
                nokElementer.await();
            }

            return register.taUt();
        } finally {
            lock.unlock();
        }
    }

    public int antall() {
        lock.lock();
        try {
            return register.antall();
        } finally {
            lock.unlock();
        }
        
    }
}

//Fikk litt hjelp fra Felix Cevro med forklare konseptet i denne deloppgaven.