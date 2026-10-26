public class Celle {
    boolean levende;
    Celle[] naboer;
    int antNaboer;
    int antLevendeNaboer;

    Celle() {
    levende = false;              //deloppgave a)
    naboer = new Celle[8];        
    antNaboer = 0;                
    antLevendeNaboer = 0;         
    }

    void settDød() {             //deloppgave b)
        levende = false;
    }

    void settLevende() {
        levende = true;
    }

    boolean erLevende() {      //deloppgave c)
        return levende;
    }

    char hentStatusTegn() {    //deloppgave d)
        if(levende) {
            return 'O'; 
        }
        else {
            return '.';
        }
    }

    void leggTilNabo(Celle nabo) {    //delopggave e)
        naboer[antNaboer] = nabo;
        antNaboer ++;
    }

    void tellLevendeNaboer() {
        antLevendeNaboer = 0;   //må nullstille telleren her
        for(int i = 0; i < antNaboer; i++){
            if(naboer[i].erLevende()) {
                antLevendeNaboer ++;
            }
        }}
    
    void oppdaterStatus() {
        if(levende) {
            if(antLevendeNaboer < 2 || antLevendeNaboer > 3) {
                settDød();}}
            else {
                if(antLevendeNaboer == 3) {
                    settLevende();}
                }
            } 

}

