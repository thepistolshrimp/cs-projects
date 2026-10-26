import java.util.*;
import java.io.*;
import java.util.concurrent.ThreadLocalRandom;


//Oppgave 2

public class Subsekvensregister {
    private ArrayList<Frekvenstabell> register = new ArrayList <>();
    private static int SUBSEKVENSLENGDE = 3;


    public String hentFrekvenstabell() {
        return register.toString();
    }


    public int antall() {
        return register.size();
    }


    public void settInn(Frekvenstabell f) {
        register.add(f);
    }


    public Frekvenstabell taUt() {
        if (register.isEmpty()) {
            return null;}
        else {
            int removeIndex = ThreadLocalRandom.current().nextInt(0, antall());
            Frekvenstabell out = register.remove(removeIndex);
            return out;
        }
    }

    public static Frekvenstabell les(String filnavn) {
        Frekvenstabell f = new Frekvenstabell();
        
        try (Scanner g = new Scanner(new File(filnavn))) {
            
            while (g.hasNextLine()) {
                String s = g.nextLine();
                
                for(int i = 0; i <= s.length()-SUBSEKVENSLENGDE; i++) {
                    String ss = s.substring(i,i + SUBSEKVENSLENGDE);
                    f.put(ss, 1);
                }
            } 

        } catch (FileNotFoundException e) {
            System.out.println("FEIL i subsekvensregister: " + e);
        }

        return f;
    }

}
