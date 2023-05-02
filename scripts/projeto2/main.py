import unittest
import math
from projeto2 import *

class TestStringMethods(unittest.TestCase):

    # T1

    def test_totalEspecies(self):
        self.assertEqual(totalEspecies(), 5203)

    def test_parenteMaisProximo(self):
        self.assertEqual(parenteMaisProximo('Homo sapiens','Macaca fuscata'), 'Catarrhini')

    # T2

    # T3

    def test_casosCaes(self):
        self.assertEqual(casosCaes(),238)

    def test_eventosFelideos(self):
        eventos = [('cat', 184), ('tiger', 45), ('lion', 41), ('snow leopard', 9), ('puma', 4), ('Canada lynx', 1), ('Eurasian lynx', 1), ('fishing cat', 1), ('leopard', 1)]
        self.assertEqual(eventosFelideos(),eventos)

    def test_maisHumanos(self):
        classes = {'farm': 'Greece', 'pet': 'United States', 'reserve': 'Mongolia', 'wildlife': 'United States', 'zoo': 'Singapore'}
        self.assertEqual(maisHumanos(),classes)

    def test_mediaQuintas(self):
        medias = {'Canada': 62, 'Denmark': 14, 'France': 4, 'Greece': 11, 'Italy': 253, 'Lithuania': 22, 'Netherlands': 6, 'Poland': 63, 'Spain': 23, 'Sweden': 14, 'United States': 37}
        self.assertEqual({k:math.floor(v) for k,v in mediaQuintas().items()},medias)

    # T5

    def test_hubPorto(self):
        self.assertEqual(hubPorto(),('Trindade', {'Linha Azul', 'Linha Amarela', 'Linha Verde', 'Linha Laranja', 'Linha Vermelha', 'Linha Violeta'}))

    def test_temCaminhoDireto(self):
        self.assertEqual(temCaminhoDireto('Trindade', 'Trindade'), True)
        self.assertEqual(temCaminhoDireto('Campanha','Sete Bicas'),True)
        self.assertEqual(temCaminhoDireto('Casa da Musica','Hospital de Sao Joao'), False)

    def test_caminhoMaisRapido(self):
        self.assertAlmostEqual(caminhoMaisRapido('Campanha','Sete Bicas'), 876.2643147041399)
        self.assertAlmostEqual(caminhoMaisRapido('Casa da Musica','Santo Ovidio'),1022.2265891442585)


if __name__ == '__main__':
    unittest.main(exit=False)