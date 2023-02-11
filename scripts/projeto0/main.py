import unittest
from projeto0 import *

class TestStringMethods(unittest.TestCase):

    def test_3_9(self):
        # Enter code here
        self.assertEqual(contaSequencia('ACTGCTATCCATT', 'AT'), 2)
        self.assertEqual(contaSequencia('TTTTTCATT', 'TT'), 3)
        self.assertEqual(contaSequencia('ACGTTACGGAACG', 'ACG'), 2)

    def test_3_8(self):
        # Enter code here
        self.assertEqual(ocorrencias('banana', 'a'), [1, 3, 5])
        self.assertEqual(ocorrencias('banana', 'A'), [])
        self.assertEqual(ocorrencias('banana', '!'), [])
        self.assertEqual(ocorrencias('b3n3n3', 'b'), [0])

    def test_3_7(self):
        # Enter code here
        self.assertTrue(palindrono_geral("Amora me tem aroma."))
        self.assertTrue(palindrono_geral("Madam, I'm Adam."))
        self.assertTrue(palindrono_geral("A man, a plan, a canal: Panama"))
        self.assertFalse(palindrono_geral("Amora não aroma"))
        self.assertTrue(palindrono_geral("a!b!b!A"))

    def test_2_11(self):
        # Enter code here
        self.assertEqual(algarismos(1), 1)
        self.assertEqual(algarismos(11), 2)
        self.assertEqual(algarismos(234), 3)
        self.assertEqual(algarismos(10000000), 8)

    def test_1_7(self):
        # Enter code here
        self.assertAlmostEqual(juros(20, 1, 0), 20)
        self.assertAlmostEqual(juros(3, -1, 0.5), 1.8195919791379003)
        self.assertAlmostEqual(juros(123, 30, 5), 1.714262784219647e+67)

    def test_3_6(self):
        # Enter code here
        self.assertEqual(forte('9EwL56'), False)
        self.assertEqual(forte('HXKW1393'), False)
        self.assertEqual(forte('ffu4G7Fghjk'), True)
        self.assertEqual(forte('AAAAAAA'), False)
        self.assertEqual(forte('aBcDeFg1234'), True)

    def test_3_5(self):
        # Enter code here
        self.assertEqual(remove_py_com("def f(x): # f function "), "def f(x): ")
        self.assertEqual(remove_py_com('def \"#\" f(x) # comentário'), "def \"#\" f(x) ")
        self.assertEqual(remove_py_com('def \"#\" f(x) !## comentário'), "def \"#\" f(x) !")
        self.assertEqual(remove_py_com('def f( # x) !## comentário'), "def f( ")

    def test_3_4(self):
        # Enter code here
        self.assertEqual(cesar(3, "mensagem secreta"), "phqvdjhp#vhfuhwd")
        self.assertEqual(cesar(3, "      #####   "), "######&&&&&###")
        self.assertEqual(cesar(0, "ABCDEF"), "ABCDEF")
        self.assertEqual(cesar(-1, "aBcDeF"), "`AbCdE")

    def test_3_3(self):
        # Enter code here
        self.assertEqual(palindrono("reviveR"), True)
        self.assertEqual(palindrono("aaaa"), True)
        self.assertEqual(palindrono("ola olo"), False)
        self.assertEqual(palindrono("amada"), False)
        self.assertEqual(palindrono("oCo"), True)

    def test_3_2(self):
        # Enter code here
        self.assertEqual(filtra_letras('Ola!, -- disse ele...'), "Oladisseele")
        self.assertEqual(filtra_letras('!P-y-t-h-o-n!'), "Python")
        self.assertEqual(filtra_letras('\0/\\0//\0/'), "")

    def test_3_1(self):
        # Enter code here
        self.assertEqual(conta_letras('Ola, mundo!  '), 8)
        self.assertEqual(conta_letras('123 45'), 0)
        self.assertEqual(conta_letras('!!!%$#A%B??'), 2)

    def test_2_10(self):
        # Enter code here
        self.assertEqual(repetidos(['ola', 'ole', 'abba', 'ole']), True)
        self.assertEqual(repetidos([3, 2, -5, 0, 1]), False)
        self.assertEqual(repetidos([3, 'a', -5, 'a', 3]), True)
        self.assertEqual(repetidos([3, 'a', True, 'b', 3.01]), False)

    def test_2_9(self):
        # Enter code here
        self.assertEqual(maximo2([3, -2, 1, 0, -2, 1]), 1)
        self.assertEqual(maximo2([1, 3, 2, 3, 0]), 2)
        self.assertEqual(maximo2([1, 3, 200, 200, 0]), 3)
        self.assertEqual(maximo2([-1, -3, -200, -200, 0]), -1)

    def test_2_8(self):
        # Enter code here
        self.assertEqual(sum_within([4, 7, 44, 23], 17, 46), 67)
        self.assertEqual(sum_within([4, 7, 44, 23], 0, 0), 0)
        self.assertEqual(sum_within([2, 4, 3, 1], 1, 2), 3)
        self.assertEqual(sum_within([90, 23, 44, 3, 1], 45, 2), 0)

    def test_2_7(self):
        # Enter code here
        self.assertAlmostEqual(leibniz(0), 0)
        self.assertAlmostEqual(leibniz(1), 4.0)
        self.assertAlmostEqual(leibniz(2), 2.666666666666667)
        self.assertAlmostEqual(leibniz(3), 3.466666666666667)
        self.assertAlmostEqual(leibniz(4), 2.8952380952380956)
        self.assertAlmostEqual(leibniz(40), 3.116596556793833)

    def test_2_6_2(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        studs = [("#", "nome", -10), \
                 ("#", "nome", 0), \
                 ("#", "nome", 10), \
                 ("#", "nome", 95)]
        classifica(studs)
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()

        self.assertEqual(s, "# nome inválido\n# nome insuficiente\n# nome insuficiente\n# nome excelente\n")

    def test_2_6_1(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        studs = [("UP194187304", "José Fonseca", 97), \
                 ("UP194209183", "Manuel Ferreira", 87), \
                 ("UP194294793", "Maria Ramos", 50), \
                 ("UP194399128", "Antonio Fernandes", 45), \
                 ("UP194739873", "Júlia Pinto", -1), \
                 ("UP194739889", "Manuela Faria", 50)]
        classifica(studs)
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()

        self.assertEqual(s,
                         "UP194187304 José Fonseca excelente\nUP194209183 Manuel Ferreira muito bom\nUP194294793 Maria Ramos suficiente\nUP194399128 Antonio Fernandes insuficiente\nUP194739873 Júlia Pinto inválido\nUP194739889 Manuela Faria suficiente\n")

    def test_2_5(self):
        # Enter code here
        self.assertAlmostEqual(valor([24.8, 49.1]), 120.457)
        self.assertAlmostEqual(valor([0, 12.7, 0]), 20.700999999999997)
        self.assertAlmostEqual(valor([100, 200.1, 300.4]), 978.8149999999998)

    def test_2_2_3(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        ex22_3()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s, "12 0\n10 12\n32 22\n3 54\n66 57\n17 123\n42 140\n99 182\n20 281\n")

    def test_2_2_2(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        ex22_2()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s,
                         "12 144 3.4641016151377544\n10 100 3.1622776601683795\n32 1024 5.656854249492381\n3 9 1.7320508075688772\n66 4356 8.12403840463596\n17 289 4.123105625617661\n42 1764 6.48074069840786\n99 9801 9.9498743710662\n20 400 4.47213595499958\n")

    def test_2_2_1(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        ex22_1()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s, "12\n10\n32\n3\n66\n17\n42\n99\n20\n")

    def test_2_1_4(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        tempC4()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s, "-5 23.0\n0 32.0\n5 41.0\n10 50.0\n15 59.0\n20 68.0\n25 77.0\n")

    def test_2_1_3(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        tempC3()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s, "-5\n0\n5\n10\n15\n20\n25\n")

    def test_2_1_2(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        tempC2()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s, "-5\n0\n5\n10\n15\n20\n25\n")

    def test_2_1_1(self):
        # Enter code here
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        tempC1()
        sys.stdout = sys.__stdout__
        s = capturedOutput.getvalue()
        self.assertEqual(s, "-5\n0\n5\n10\n15\n20\n25\n")

    def test_1_6(self):
        # Enter code here
        self.assertEqual(segundos(0, 0, 600), 600)
        self.assertEqual(segundos(0, 30, 0), 1800)
        self.assertEqual(segundos(15, 0, 3), 54003)
        self.assertEqual(segundos(2, 15, 30), 8130)

    def test_1_5(self):
        # Enter code here
        x1 = 0.0002908882086657216
        x2 = 3.144695461148894
        x3 = 6.2687863408506335
        self.assertAlmostEqual(radianos(0, 0, 60), x1)
        self.assertAlmostEqual(radianos(180, 10, 40), x2)
        self.assertAlmostEqual(radianos(359, 10, 30), x3)

    def test_1_4(self):
        # Enter code here
        self.assertAlmostEqual(dist(1, 1, 4, 4), 4.242640687119285)
        self.assertAlmostEqual(dist(5, -2, -4, -15), 15.811388300841896)
        self.assertAlmostEqual(dist(0, 0, 10, 15), 18.027756377319946)

    def test_1_3(self):
        # Enter code here
        self.assertAlmostEqual(celsius(-30), -34.44444444444444)
        self.assertAlmostEqual(celsius(0), -17.77777777777778)
        self.assertAlmostEqual(celsius(20), -6.666666666666667)
        self.assertAlmostEqual(celsius(100), 37.77777777777778)

    def test_1_2(self):
        self.assertAlmostEqual(area_circ(0), 0.0)
        self.assertAlmostEqual(area_circ(4), 50.26548245743669)
        self.assertAlmostEqual(area_circ(7), 153.93804002589985)

    def test_1_1(self):
        self.assertAlmostEqual(perim_circ(0), 0.0)
        self.assertAlmostEqual(perim_circ(4), 25.132741228718345)

if __name__ == '__main__':
    unittest.main(exit=False)