import java.io.*;
import java.util.*;

//Oppgave 7 KlarGjorData (MAIN)

public class KlarGjorData {
    
    static int ANTALL_TRÅDER = 8;

    public static void main(String[] args) {

        if (args.length == 0) {
            System.out.println("Mangler <filsti> !!!");
            return;
        }

        String filNavn = args[0];
        File fil = new File(filNavn);
        String mappe = fil.getParent() + "/";

        Monitor smittet = new Monitor();
        Monitor ikkeSmittet = new Monitor();
        ArrayList<Thread> leseTråder = new ArrayList<>();
        
        try (Scanner sc = new Scanner(fil)) {
            while (sc.hasNextLine()) {
                String[] linje = sc.nextLine().split(",");
                String csv = linje[0];
                String status = linje[1];

                String path = mappe + csv;
                
                if (status.equals("True")) {
                    Thread t = new Thread(new Lesetrad(path, smittet));
                    leseTråder.add(t);
                    t.start();
                } else { 
                    Thread t = new Thread(new Lesetrad(path, ikkeSmittet));
                    leseTråder.add(t);
                    t.start();
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Fil ikke funnet: " + e);
        }


        for (Thread t: leseTråder) {
            try {
                t.join();
            } catch (InterruptedException e) {
                System.out.println("Avbrutt lesetråd!" + e); 
            }
        }
                
        
        ArrayList<Thread> fletteTråder = new ArrayList<>();
        System.out.println("Starter fletting...");

        for (int i = 0; i < ANTALL_TRÅDER; i++) {
            Thread[] tråder = {new Thread(new Flettetrad(smittet)), new Thread(new Flettetrad(ikkeSmittet))};

            for (Thread t : tråder) {
                fletteTråder.add(t);
                t.start();
            }
        }
    

        for (Thread t : fletteTråder) {
            try {
                t.join();
            } catch (InterruptedException e){
                System.out.println("Avbrutt flettetråd!" + e);
            }
        }
        

        try {
            Frekvenstabell smittetResultat = smittet.hentResultat();
            Frekvenstabell ikkeSmittetResultat = ikkeSmittet.hentResultat();

            smittetResultat.skrivTilFil("smittet");
            System.out.println("Ferdig med smittet");

            ikkeSmittetResultat.skrivTilFil("ikke_smittet");
            System.out.println("Ferdig med ikke_smittet");

        } catch (InterruptedException e) {
            System.out.println("Feil ved henting av resultat!");
        }
    }
}

