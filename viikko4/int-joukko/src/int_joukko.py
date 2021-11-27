KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        
        if not isinstance(kapasiteetti, int):
            raise TypeError("Kapasiteetin täytyy olla kokonaisluku")  # heitin vaan jotain :D

        if kapasiteetti < 0:
            raise ValueError("Kapasiteetti ei voi olla negatiivinen")  # heitin kans jotain :D

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.joukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.joukko

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return

        self.lisaa_luku(luku)
        self.muuta_alkioiden_lukumaaraa(1)

        if self.alkioiden_lkm % len(self.joukko) == 0:
            self.kasvata_taulua()

    def poista(self, poistettava_luku):
        if poistettava_luku in self.joukko:
            self.joukko = [luku for luku in self.joukko if luku != poistettava_luku]
            self.muuta_alkioiden_lukumaaraa(-1)

    def lisaa_luku(self, luku):
        self.joukko[self.alkioiden_lkm] = luku

    def muuta_alkioiden_lukumaaraa(self, muutos):
        self.alkioiden_lkm += muutos

    def kasvata_taulua(self):
        taulukko_old = self.joukko
        self.joukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.joukko)

    def kopioi_taulukko(self, taulu, kopio):
        for i in range(0, len(taulu)):
            kopio[i] = taulu[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.joukko[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        for luku in joukko2.to_int_list():
            joukko1.lisaa(luku)

        return joukko1

    @staticmethod
    def leikkaus(joukko1, joukko2):
        leikkausjoukko = IntJoukko()
        joukko1_lista = joukko1.to_int_list()
        joukko2_lista = joukko2.to_int_list()

        leikkaus = [luku for luku in joukko1_lista if luku in joukko2_lista]

        for luku in leikkaus:
            leikkausjoukko.lisaa(luku)

        return leikkausjoukko

    @staticmethod
    def erotus(joukko1, joukko2):
        for luku in joukko2.to_int_list():
            joukko1.poista(luku)

        return joukko1

    def __str__(self):
        return f"{'{'}{str(self.joukko[:self.alkioiden_lkm]).strip('[]')}{'}'}"