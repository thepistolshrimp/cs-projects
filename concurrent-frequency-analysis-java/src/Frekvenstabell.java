import java.io.*;
import java.util.*;

//Oppgave 1 Frekvenstabell

class Frekvenstabell extends TreeMap<String, Integer> {

    @Override
    public String toString() {
        String s = "";
        
        for (String key : this.keySet()) {
            String str = key + " " + this.get(key) + "\n";
            s += str;
        }
        return s;

    }

    public static Frekvenstabell flett(Frekvenstabell f1, Frekvenstabell f2) {
        Frekvenstabell flettet = new Frekvenstabell();
        
        for (String key : f1.keySet()) {
            flettet.put(key, f1.get(key));
        }

        for (String key : f2.keySet()) {
            if (flettet.containsKey(key)) {
                flettet.put(key, flettet.get(key) + f2.get(key));
            } else {
                flettet.put(key, f2.get(key));
            }
        }

        return flettet;
    }

    public void skrivTilFil(String filnavn) {
        
        try (PrintWriter out = new PrintWriter(filnavn)) {
            out.println(this.toString());
        } catch (FileNotFoundException e) {
            System.out.println("FEIL i skrivTilFil: " + e);
        }

    }
}