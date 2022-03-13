from projeto2 import *
import unittest


class TestProj2(unittest.TestCase):

    def test_paisMaisNuclear(self):
        self.assertEqual(paisMaisNuclear(dados),"United States")

    def test_reatorMaisRecente(self):
        self.assertEqual(reatorMaisRecente(dados),"PWR")

    def test_paisTresMaioresCentrais(self):
        self.assertEqual(paisTresMaioresCentrais(dados),"China")

    def test_centraisParis(self):
        self.assertEqual(centraisParis(dados),109)

    def test_trintaPorCento(self):
        self.assertEqual(trintaPorCento(dados3),426)

    def test_anoMaisNuclear(self):
        self.assertEqual(anoMaisNuclear(dados3),2002)

    def test_nuclearDecadas(self):
        self.assertEqual(nuclearDecadas(dados3),[18, 44, 53, 64, 64, 67])

    def test_naoMaisNuclear(self):
        l1 = list(naoMaisNuclear(dados3,paises3))
        l2 = ['Italy','Japan','Lithuania']
        self.assertEqual(set(l1),set(l2))

    def test_maisRenovaveis2020(self):
        x,y = maisRenovaveis2020(dados4)
        self.assertEqual(x,'Costa Rica')
        self.assertAlmostEqual(y,99.841)

    def test_energiaPortugal2020(self):
        l1 = list(map(lambda x: (x[0],round(x[1])),energiaPortugal2020(dados4)))
        l2 = [('gas', 34), ('wind', 24), ('hydro', 24), ('other_renewables', 8), ('coal', 5), ('solar', 3), ('oil', 3), ('nuclear', 0)]
        self.assertEqual(l1,l2)

    def test_maisDependentesCarvao(self):
        l1 = maisDependentesCarvao(dados4)
        l2 = {1985: 'Poland', 1986: 'Poland', 1987: 'Poland', 1988: 'Poland', 1989: 'Poland', 1990: 'Poland', 1991: 'Poland', 1992: 'Poland', 1993: 'Poland', 1994: 'Poland', 1995: 'Poland', 1996: 'Poland', 1997: 'Poland', 1998: 'Poland', 1999: 'Poland', 2000: 'Botswana', 2001: 'Botswana', 2002: 'Botswana', 2003: 'Botswana', 2004: 'Botswana', 2005: 'Botswana', 2006: 'Botswana', 2007: 'Botswana', 2008: 'Botswana', 2009: 'Botswana', 2010: 'Botswana', 2011: 'Botswana', 2012: 'Botswana', 2013: 'Botswana', 2014: 'Botswana', 2015: 'Botswana', 2016: 'Botswana', 2017: 'Botswana', 2018: 'Botswana', 2019: 'Botswana', 2020: 'Mongolia', 2021: 'Poland'}
        self.assertEqual(l1,l2)

    def test_gasEU(self):
        l2 = {1990: 11, 1991: 11, 1992: 10, 1993: 10, 1994: 10, 1995: 11, 1996: 13, 1997: 13, 1998: 14, 1999: 16, 2000: 17, 2001: 18, 2002: 20, 2003: 21, 2004: 22, 2005: 22, 2006: 23, 2007: 24, 2008: 24, 2009: 23, 2010: 26, 2011: 25, 2012: 23, 2013: 20, 2014: 18, 2015: 19, 2016: 18, 2017: 22, 2018: 22, 2019: 24, 2020: 24, 2021: 22}
        l1 = { x : round(y) for x,y in gasEU(dados4).items() }
        self.assertEqual(l1,l2)

    def test_anoMaisRenovavelEU(self):
        l2 = {'Germany': 2020, 'Austria': 2020, 'Belgium': 2020, 'Bulgaria': 2018, 'Cyprus': 2020, 'Croatia': 2014, 'Denmark': 2005, 'Slovakia': 2020, 'Slovenia': 2014, 'Spain': 2020, 'Estonia': 2020, 'Finland': 2020, 'France': 2020, 'Greece': 2013, 'Hungary': 2013, 'Ireland': 2020, 'Italy': 2020, 'Latvia': 2017, 'Lithuania': 2018, 'Luxembourg': 2020, 'Malta': 2016, 'Netherlands': 2013, 'Poland': 2001, 'Portugal': 2020, 'Romania': 2014, 'Sweden': 2020, 'Iceland': 2011, 'Norway': 2002, 'United Kingdom': 2020, 'Switzerland': 2017}
        self.assertEqual(anoMaisRenovavelEU(dados4,dados5),l2)

if __name__ == '__main__':
    unittest.main(exit=False)


