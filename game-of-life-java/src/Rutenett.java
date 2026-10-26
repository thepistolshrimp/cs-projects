public class Rutenett {           // a)
    int antRader;
    int antKolonner;
    Celle [][] rutene;

    Rutenett(int antRader, int antKolonner){     
        this.antRader = antRader;
        this.antKolonner = antKolonner;
        rutene = new Celle[antRader][antKolonner];

    }

    void lagCelle(int rad, int kol) {               // c)
        Celle celle = new Celle();
        rutene[rad][kol] = celle;

        if(Math.random() <= 0.3333) {
            celle.settLevende();}
    }

    void fyllMedTilfeldigeCeller() {                // d)
        for(int rad=0; rad < antRader; rad++){
            for(int kol=0; kol < antKolonner; kol++){
                lagCelle(rad, kol);}
        }
    }

    Celle hentCelle(int rad, int kol) {             // e)
        if(rad < 0 || kol < 0 || rad >= antRader || kol >= antKolonner){
            return null;}

        else {
            return rutene[rad][kol];
        }
    } // så rad-eller kol indeks kan ikke være mindre enn 0 og ikke større enn totalen rad/kol
      // da er den utenfor sin range

    void tegnRutenett() {                           // f)
        for(int rad=0; rad < antRader; rad ++){
            for(int kol= 0; kol < antKolonner; kol ++){
                System.out.print(rutene[rad][kol].hentStatusTegn() + " ");}

            System.out.println();
        }
        
    }

    void settNaboer(int rad, int kol){              // g)
        Celle celle = rutene[rad][kol];

        for(int deltaRad = -1; deltaRad <= 1; deltaRad ++){
            for(int deltaKol = -1; deltaKol <=1; deltaKol ++){
                if(deltaRad == 0 && deltaKol == 0){
                    continue;
                }

                Celle nabo = hentCelle(rad + deltaRad, kol + deltaKol);

                if(nabo != null) {
                    celle.leggTilNabo(nabo);
                } //fikk hjelp av Felix Cevro i denne deloppgaven
            }
        }
    }  

    void kobleAlleCeller() {                        // h)
        for(int rad=0; rad < antRader; rad++){
            for(int kol=0; kol <antKolonner; kol++){
                settNaboer(rad, kol);
            }
        }
    }

    int antallLevende() {                           // i)
        int tell = 0;
        for (int rad=0; rad < antRader; rad ++) {
            for (int kol=0; kol < antKolonner; kol ++) {
                if(rutene[rad][kol].erLevende()) {
                    tell ++;
                }
            }
        }
        return tell;
    }

}
