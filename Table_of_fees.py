class BrokerageAccount:
    def __init__(self, commission, minimum_commission):
        self.commission = commission
        self.minimum_commission = minimum_commission

    def params(self):
        print("Minimalna opłata: " + str(self.minimum_commission) + "PLN, " + "nie mniej niż: " + str(
            self.commission) + "%." + '\n')


class bonds(BrokerageAccount):
    def show_commission(self):
        print('Tabela opłat - Obligacje.')
        self.params()



class stocks(BrokerageAccount):
    def show_commission(self):
        print('Tabela opłat - Akcje.')
        self.params()



class etf(BrokerageAccount):
    def show_commission(self):
        print('Tabela opłat - ETF.')
        self.params()



bonds = bonds(0.40, 6.00)
stocks =stocks(0.38, 5.00)
etf = etf(0.29, 19.00)

bonds.show_commission()
stocks.show_commission()
etf.show_commission()
