from testes import *
from projeto1 import *
import unittest

class TestProj1(unittest.TestCase):

    def test_formatSermao_2(self):
      s1 = formataSermao(sermao)
      s2 = format_sermao
      assertTextLinesEqual(self,s1,s2)

    def test_formataSermao_1(self):
      s1 = formataSermao(sermao_ex)
      s2 = format_sermao_ex
      assertTextLinesEqual(self,s1,s2)

    def test_formataPalavra_1(self):
      s1 = formataPalavra('-Normalizá-lo-ei!!')
      s2 = '-Normalizá-lo-ei!!'
      self.assertEqual(s1,s2)

    def test_formataPalavra_2(self):
      s1 = formataPalavra('!!veritas!!')
      s2 = '!!*veritas*!!'
      self.assertEqual(s1,s2)

    def test_formataPalavra_3(self):
      s1 = formataPalavra('English?')
      s2 = '~~English~~?'
      self.assertEqual(s1,s2)

    def test_normalizaPalavra_3(self):
      s1 = normalizaPalavra(':Palavra1a')
      s2 = (':','Palavra1a','palavra1a','')
      self.assertEqual(s1,s2)

    def test_normalizaPalavra_2(self):
      s1 = normalizaPalavra('')
      s2 = ('','','','')
      self.assertEqual(s1,s2)

    def test_normalizaPalavra_1(self):
      s1 = normalizaPalavra('-Normalizá-lo-ei!!')
      s2 = ('-','Normalizá-lo-ei','normalizá-lo-ei','!!')
      self.assertEqual(s1,s2)
    
    def test_maiorParagrafo_4(self):
      ex1 = (['SERMÃO'],[['sermão']],[('I',[]),('II',[['ad'],['ae','af']])])
      self.assertEqual(maiorParagrafo(ex1),'II')
    
    def test_maiorParagrafo_3(self):
      self.assertEqual(maiorParagrafo(sermao),'II')

    def test_maiorParagrafo_2(self):
      ex1 = (['SERMÃO'],[['sermão']],[('I',[['a'],['b','c']]),('II',[['ad'],['ae','af']])])
      self.assertEqual(maiorParagrafo(ex1), 'I')

    def test_maiorParagrafo_1(self):
      self.assertEqual(maiorParagrafo(sermao_ex),'I')

    def test_deusPeixes_3(self):
      self.assertEqual(deusPeixes(sermao), 7)

    def test_deusPeixes_2(self):
      ex1 = (['Deus','e','peixes'],[['Deus','e','peixes'],['Veni,','vidi,','vici.']],[('I',[['Deus','peixes.'],['Deus:','peixes']])])
      self.assertEqual(deusPeixes(ex1),0)

    def test_deusPeixes_1(self):
      self.assertEqual(deusPeixes(sermao_ex),0)

    def test_totais_2(self):
      self.assertEqual(totais(sermao),(6,80,11974))

    def test_totais_1(self):
      self.assertEqual(totais(sermao_ex),(1,2,16))

    def test_organizaCapitulos_1(self):
      l1 = [['I'],['Parágrafo um.','Parágrafo dois.'],['II'],['Parágrafo  três.']]
      l2 = [('I',[['Parágrafo','um.'],['Parágrafo','dois.']]),('II',[['Parágrafo','três.']])]
      self.assertEqual(organizaCapitulos(l1),l2)

    def test_organizaSermao_2(self):
      l1 = organizaSermao(linhas_sermao)
      l2 = sermao
      self.assertEqual(l1,l2)

    def test_organizaSermao_1(self):
      l1 = organizaSermao(linhas_sermao_ex)
      l2 = sermao_ex
      self.assertEqual(l1,l2)

    def test_separaLinhas_2(self):
      l1 = separaLinhas(['a','','',' ',''])
      l2 = [['a'],[' ']]
      self.assertEqual(l1,l2)

    def test_separaLinhas_1(self):
      l1 = separaLinhas(['a','b','','c'])
      l2 = [['a','b'],['c']]
      self.assertEqual(l1,l2)

    def test_separaLinha_3(self):
      l1 = separaLinha('Sou  espaço  ')
      l2 = ['Sou','espaço']
      self.assertEqual(l1,l2)

    def test_separaLinha_2(self):
      l1 = separaLinha('   ')
      l2 = []
      self.assertEqual(l1,l2)

    def test_separaLinha_1(self):
      l1 = separaLinha('Olá mundo')
      l2 = ['Olá','mundo']
      self.assertEqual(l1,l2)

    def test_leTexto_1(self):
      txt1 = leTexto('dados/sermao_ex.txt')
      txt2 = linhas_sermao_ex
      self.assertEqual(txt1,txt2)

    def test_leTexto_2(self):
      txt1 = leTexto('dados/sermao.txt')
      txt2 = linhas_sermao
      self.assertEqual(txt1,txt2)

if __name__ == '__main__':
    unittest.main(exit=False)


