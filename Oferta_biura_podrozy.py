class Rejs:
    def rejs(self):
        print("W tej atrakcji czeka Cię rejs ekskluzywnym jachtem")

class Nurkowanie:
    def nurkowanie(self):
        print("Nurkowanie w otoczeniu przepięknej rafy koralowej")


class Wodospady:
    def wodospady(self):
        print("Skakanie z wodospadow")


class Quady:
    def quady(self):
        print("Dziki rajd quadem po lesie")

class Noc_w_muzeum:
    def noc(self):
        print("Zwiedzanie sztuki wspolczesnej w nocnej scenerii")

class Kolacja_na_plazy:
     def kolacja(self):
        print("Romantyczna kolacja na plazy we dwoje")

class Zwiedzanie_miasta:
    def zwiedzanie(self,cena,wiek):
        self.cena = cena
        self.wiek =wiek

        if self.wiek < 18:
            self.cena = self.cena * 0.5
            print(f'Odkryj tajemnice starego miasta za jedyne {self.cena}')
            return self.cena

        else:
            print(f'Odkryj tajemnice starego miasta za jedyne {self.cena}')
            return self.cena

class Kolacja_na_starym_miescie:
    def kolacja(self, wiek):
        self.wiek = wiek
        print('Na co masz dzisiaj ochote? ')
        if self.wiek < 18:
            print("Alkohol tylko powyżej 18lat")
        else:
            print("Wstrząśnięte nie mieszane")




class OpcjaWycieczki:
    def __init__(self):
        self.rejs = Rejs()
        self.nurkowanie = Nurkowanie()
        self.wodospady = Wodospady()
        self.quady = Quady()
        self.noc_w_muzeum = Noc_w_muzeum()
        self.kolacja_na_plazy = Kolacja_na_plazy()
        self.kolacja_na_starym_miescie = Kolacja_na_starym_miescie()
        self.zwiedzanie_miasta = Zwiedzanie_miasta()


    def all_inclusive(self, wiek):
        self.rejs.rejs()
        self.nurkowanie.nurkowanie()
        self.wodospady.wodospady()
        self.quady.quady()
        self.noc_w_muzeum.noc()
        self.kolacja_na_plazy.kolacja()
        self.zwiedzanie_miasta.zwiedzanie(10, wiek)
        self.kolacja_na_starym_miescie.kolacja(wiek)

    def budget(self):
        self.rejs.rejs()
        self.nurkowanie.nurkowanie()
        self.wodospady.wodospady()



osoba1 = OpcjaWycieczki()
osoba1.all_inclusive(15)

print("------------------------------------------")

osoba2 = OpcjaWycieczki()
osoba2.all_inclusive(50)