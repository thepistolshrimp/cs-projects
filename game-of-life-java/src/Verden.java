public class Verden {
    Rutenett rutenett;
    int genNr;

    Verden(int antRad, int antKolonne){                 // a)

        rutenett = new Rutenett(antRad, antKolonne);
        genNr = 0;

        rutenett.fyllMedTilfeldigeCeller();
        rutenett.kobleAlleCeller();
    }

    void tegn() {                                       // b)
        
        rutenett.tegnRutenett();
        System.out.println("Generasjon nr" + genNr);
        System.out.println("Det er " + rutenett.antallLevende() + " levende celler");
    }   
    //ser riktig ut :)

    void oppdatering() {                                // c)

        for (int rad=0; rad < rutenett.antRader; rad ++) {
            for (int kol=0; kol < rutenett.antKolonner; kol ++) {
                rutenett.hentCelle(rad, kol).tellLevendeNaboer();
            }
        }
        
        for (int rad=0; rad < rutenett.antRader; rad ++) {
            for (int kol=0; kol < rutenett.antKolonner; kol ++) {
                rutenett.hentCelle(rad, kol).oppdaterStatus();
            }
        }
        genNr ++;
    } 
}


