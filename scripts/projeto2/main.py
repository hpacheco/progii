# -*- coding: utf-8 -*-

#from projeto2 import *
from t2 import *

import unittest

class TestProj2(unittest.TestCase):

# T1

    def test_t1_maisPartilhados(self):
        r = maisPartilhados()
        mais = (4, {('1981', 'physics'), ('1958', 'medicine'), ('2001', 'chemistry'), ('1973', 'physics'), ('2002', 'physics'), ('2011', 'medicine'), ('2015', 'medicine'), ('1997', 'chemistry'), ('1977', 'medicine'), ('2021', 'physics'), ('1947', 'medicine'), ('2002', 'chemistry'), ('2000', 'physics')})
        self.assertEqual(r, mais)

    def test_t1_multiLaureados(self):
        r = multiLaureados()
        self.assertEqual(r, {'Linus Pauling': {'chemistry', 'peace'}, 'Marie Curie': {'chemistry', 'physics'}})

    def test_t1_anosSemPremio(self):
        r = anosSemPremio()
        self.assertEqual(r, (1914, 1919))

    def test_t1_rankingDecadas(self):
      r = rankingDecadas()
      rank = {'190x': ('Germany', 11), '191x': ('Germany', 9), '192x': ('Germany', 8), '193x': ('Germany', 16), '194x': ('USA', 15), '195x': ('USA', 33), '197x': ('USA', 45), '196x': ('USA', 30), '198x': ('USA', 47), '199x': ('USA', 58), '200x': ('USA', 79), '202x': ('USA', 29), '201x': ('USA', 75)}
      self.assertEqual(r,rank)

# T2

    def test_t2_toGrayscale(self):
      rgb: np.ndarray = asarray(Image.open('dados/test.png'))
      gray: np.ndarray = asarray(Image.open('dados/test_gray.png'))
      np.testing.assert_array_almost_equal(toGrayscale(rgb),gray,decimal=0)

    def test_t2_toBW(self):
      gray: np.ndarray = asarray(Image.open('dados/test_gray.png'))
      bw: np.ndarray = asarray(Image.open('dados/test_bw.png'))
      np.testing.assert_array_almost_equal(toBW(gray,(0,20)),bw,decimal=0)

    def test_t2_autoThreshold(self):
      r = autoThreshold('dados/test_bw.png',5)
      self.assertEqual(r,(0,5))

    def test_t2_toContour(self):
      bw: np.ndarray = asarray(Image.open('dados/test_bw.png'))
      contour: np.ndarray = asarray(Image.open('dados/test_contour.png'))
      np.testing.assert_array_almost_equal(toContour(bw),contour,decimal=0)

# T3

    def test_t3_eleitoresPorto(self):
      r = eleitoresPorto()
      self.assertEqual(r,2019)

    def test_t3_taxaAbstencao(self):
      r = taxaAbstencao()
      xs = [(1975, 8.469655914752872), (1976, 16.674254034178237), (1979, 12.924164637145363), (1980, 15.197467656080955), (1983, 22.197057420229104), (1985, 25.739654437542637), (1987, 28.451911394660932), (1991, 32.60289091155008), (1995, 33.79203573536146), (1999, 38.9540432370464), (2002, 38.35696381836895), (2005, 35.63617762873651), (2009, 40.25883294679326), (2011, 41.93145502041587), (2015, 44.13864814372821), (2019, 51.42704330923308), (2022, 48.58296003165151)]
      self.assertEqual([x for x,y in r],[x for x,y in xs])
      for i in range(len(r)):
          self.assertTrue(abs(r[i][1] - xs[i][1]) <= 1)

    def test_t3_perdaGrandesMunicipios(self):
      r = perdaGrandesMunicipios()
      xs = {'Arcos de Valdevez': 1976, 'Ponte de Lima': 2019, 'Viana do Castelo': 2015, 'Barcelos': 2019, 'Braga': 1999, 'Esposende': 1999, 'Vila Verde': 2011, 'Fafe': 2015, 'Guimarães': 1999, 'Vila Nova de Famalicão': 1999, 'Arouca': 2015, 'Espinho': 1999, 'Gondomar': 1999, 'Maia': 1983, 'Matosinhos': 1999, 'Oliveira de Azeméis': 1983, 'Paredes': 1999, 'Porto': 1999, 'Póvoa de Varzim': 1999, 'Santa Maria da Feira': 1999, 'Santo Tirso': 1999, 'Vale de Cambra': 2015, 'Valongo': 1999, 'Vila do Conde': 1999, 'Vila Nova de Gaia': 1999, 'Chaves': 2015, 'Amarante': 1976, 'Felgueiras': 1999, 'Lousada': 1999, 'Marco de Canaveses': 1999, 'Paços de Ferreira': 2015, 'Penafiel': 1999, 'Lamego': 1976, 'Vila Real': 1999, 'Bragança': 1983, 'Mirandela': 1999, 'Águeda': 1983, 'Albergaria-a-Velha': 1983, 'Anadia': 2019, 'Aveiro': 1999, 'Estarreja': 1999, 'Ílhavo': 1999, 'Ovar': 1999, 'Cantanhede': 1976, 'Coimbra': 1999, 'Figueira da Foz': 1976, 'Montemor-o-Velho': 1976, 'Leiria': 1976, 'Marinha Grande': 1999, 'Pombal': 1976, 'Porto de Mós': 2019, 'Tondela': 2011, 'Viseu': 1983, 'Castelo Branco': 1999, 'Covilhã': 1999, 'Fundão': 1999, 'Guarda': 1999, 'Seia': 1999, 'Alcobaça': 2019, 'Alenquer': 1976, 'Caldas da Rainha': 1976, 'Lourinhã': 1976, 'Peniche': 1987, 'Torres Vedras': 1999, 'Abrantes': 1999, 'Ourém': 2019, 'Tomar': 2019, 'Torres Novas': 1999, 'Cartaxo': 1999, 'Santarém': 1999, 'Cascais': 1999, 'Lisboa': 1999, 'Loures': 1999, 'Mafra': 1976, 'Oeiras': 1979, 'Sintra': 1999, 'Vila Franca de Xira': 1987, 'Almada': 1999, 'Barreiro': 1999, 'Moita': 1999, 'Montijo': 1999, 'Palmela': 1976, 'Seixal': 2019, 'Sesimbra': 2019, 'Setúbal': 1999, 'Odemira': 1976, 'Santiago do Cacém': 1999, 'Beja': 1999, 'Portalegre': 1999, 'Évora': 2019, 'Faro': 1999, 'Lagos': 2019, 'Loulé': 2019, 'Olhão': 1999, 'Portimão': 2019, 'Silves': 1999, 'Tavira': 1976, 'Ponta Delgada': 1976, 'Angra do Heroísmo': 1999, 'Câmara de Lobos': 2015, 'Funchal': 1999, 'Santa Cruz': 2015}
      self.assertEqual(r,xs)

    def test_t3_demografiaMunicipios(self):
      r = demografiaMunicipios()
      xs = {'Alentejo Central': ('Estremoz', 'Évora'), 'Alentejo Litoral': ('Odemira', 'Sines'), 'Algarve': ('Monchique', 'Loulé'), 'Alto Alentejo': ('Nisa', 'Campo Maior'), 'Alto Minho': ('Paredes de Coura', 'Viana do Castelo'), 'Alto Tâmega e Barroso': ('Montalegre', 'Chaves'), 'Ave': ('Vieira do Minho', 'Guimarães'), 'Baixo Alentejo': ('Mértola', 'Beja'), 'Beira Baixa': ('Idanha-a-Nova', 'Castelo Branco'), 'Beiras e Serra da Estrela': ('Sabugal', 'Guarda'), 'Cávado': ('Terras de Bouro', 'Braga'), 'Douro': ('Torre de Moncorvo', 'Vila Real'), 'Grande Lisboa': ('Lisboa', 'Sintra'), 'Ilha Graciosa': ('Santa Cruz da Graciosa', 'Santa Cruz da Graciosa'), 'Ilha Terceira': ('Vila da Praia da Vitória', 'Angra do Heroísmo'), 'Ilha da Madeira': ('Porto Moniz', 'Funchal'), 'Ilha das Flores': ('Lajes das Flores', 'Santa Cruz das Flores'), 'Ilha de Porto Santo': ('Porto Santo', 'Porto Santo'), 'Ilha de Santa Maria': ('Vila do Porto', 'Vila do Porto'), 'Ilha de São Jorge': ('Calheta [R.A.A.]', 'Velas'), 'Ilha de São Miguel': ('Nordeste', 'Ponta Delgada'), 'Ilha do Corvo': ('Corvo', 'Corvo'), 'Ilha do Faial': ('Horta', 'Horta'), 'Ilha do Pico': ('Lajes do Pico', 'Madalena'), 'Lezíria do Tejo': ('Coruche', 'Benavente'), 'Médio Tejo': ('Mação', 'Ourém'), 'Oeste': ('Bombarral', 'Torres Vedras'), 'Península de Setúbal': ('Alcochete', 'Seixal'), 'Região de Aveiro': ('Sever do Vouga', 'Aveiro'), 'Região de Coimbra': ('Pampilhosa da Serra', 'Coimbra'), 'Região de Leiria': ('Alvaiázere', 'Leiria'), 'Terras de Trás-os-Montes': ('Vinhais', 'Bragança'), 'Tâmega e Sousa': ('Cinfães', 'Penafiel'), 'Viseu Dão Lafões': ('Vouzela', 'Viseu'), 'Área Metropolitana do Porto': ('Porto', 'Vila Nova de Gaia')}
      self.assertEqual(r,xs)

# T4

    def test_t4_maisNomeado(self):
      r = maisNomeado()
      self.assertEqual(r,('Ramón Menéndez Pidal', 149))

    def test_t4_nomeacoesCruzadas(self):
      r = nomeacoesCruzadas()
      self.assertEqual(r,(286,{'Medicine', 'Physics', 'Chemistry', 'Peace'}))

    def test_t4_caminhoEinsteinFeynman(self):
      r = caminhoEinsteinFeynman()
      res = [['Arthur Compton', 'Carl Anderson'], ['Werner Karl Heisenberg', 'Hans Albrecht Bethe']]
      self.assertIn(r,res)

if __name__ == '__main__':
    unittest.main(exit=False)


