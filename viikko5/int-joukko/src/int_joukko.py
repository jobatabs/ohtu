KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko: int) -> list:
        return [0] * koko

    def __init__(self, kapasiteetti: int=None, kasvatuskoko: int=None) -> object:
        self.kapasiteetti = KAPASITEETTI if kapasiteetti is None else kapasiteetti
        self.kasvatuskoko = OLETUSKASVATUS if kasvatuskoko is None else kasvatuskoko

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n: int) -> bool:
        if n in self.ljono:
            return True

        return False

    def lisaa(self, n: int) -> bool:
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n: int) -> bool:
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, a: list, b: list) -> None:
        for i, value in enumerate(a):
            b[i] = value

    def mahtavuus(self) -> int:
        return self.alkioiden_lkm

    def to_int_list(self) -> list:
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i, _ in enumerate(taulu):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a: object, b: object) -> object:
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        lisaa_mitalle(x, a_taulu)
        lisaa_mitalle(x, b_taulu)
        return x

    @staticmethod
    def leikkaus(a: object, b: object) -> object:
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for _, a_value in enumerate(a_taulu):
            for _, b_value in enumerate(b_taulu):
                if a_value == b_value:
                    y.lisaa(b_value)

        return y

    @staticmethod
    def erotus(a: object, b: object) -> object:
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        lisaa_mitalle(z, a_taulu)
        poista_mitalle(z, b_taulu)

        return z

    def __str__(self) -> str:
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos


def lisaa_mitalle(intjoukko: object, taulu: list) -> None:
    for _, value in enumerate(taulu):
        intjoukko.lisaa(value)

def poista_mitalle(intjoukko: object, taulu: list) -> None:
    for _, value in enumerate(taulu):
        intjoukko.poista(value)
