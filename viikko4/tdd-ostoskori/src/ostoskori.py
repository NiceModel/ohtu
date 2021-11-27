from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self._ostokset)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum(ostos.hinta() for ostos in self._ostokset)
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostoksien_nimet = [ostos.tuotteen_nimi() for ostos in self._ostokset]

        if lisattava.nimi() not in ostoksien_nimet:
            self._ostokset.append(Ostos(lisattava))
        else:
            tuotteen_indeksi = ostoksien_nimet.index(lisattava.nimi())
            self._ostokset[tuotteen_indeksi].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        ostoksien_nimet = [ostos.tuotteen_nimi() for ostos in self._ostokset]
        
        if poistettava.nimi() in ostoksien_nimet:
            tuotteen_indeksi = ostoksien_nimet.index(poistettava.nimi())
            ostos = self._ostokset[tuotteen_indeksi]

            if ostos.lukumaara() == 1:
                del self._ostokset[tuotteen_indeksi]
            else:
                ostos.muuta_lukumaaraa(-1)

        # poistaa tuotteen


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
