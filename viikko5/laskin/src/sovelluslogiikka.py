class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._previous = arvo

    def miinus(self, operandi):
        self._previous = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._previous = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._previous = self._arvo
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._previous = self._arvo
        self._arvo = arvo
    
    def kumoa(self):
        self._arvo = self._previous

    def arvo(self):
        return self._arvo

class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.logiikka = sovelluslogiikka
        self.lue_syote = lue_syote
    
    def suorita(self):
        syote = self.lue_syote()
        self.logiikka.plus(syote)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.logiikka = sovelluslogiikka
        self.lue_syote = lue_syote
    
    def suorita(self):
        syote = self.lue_syote()
        self.logiikka.miinus(syote)

class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.logiikka = sovelluslogiikka
        self.lue_syote = lue_syote
    
    def suorita(self):
        self.logiikka.aseta_arvo(0)

class Kumoa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.logiikka = sovelluslogiikka
        self.lue_syote = lue_syote
    
    def suorita(self):
        self.logiikka.kumoa()

