import unittest
from calculadora import Calculadora_cientifica

class Teste_Calculadora_cientifica(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora_cientifica()

    def test_validar(self):
        self.assertTrue(self.calc._validar(1,8))
        self.assertTrue(self.calc._validar(0))
        self.assertTrue(self.calc._validar(4))
        self.assertTrue(self.calc._validar(6,10))
        with self.assertRaises(TypeError):
            self.calc._validar("x","y")
            self.calc._validar(4,"y")
            self.calc._validar("x",4)

    def test_soma(self):
        self.assertEqual(self.calc.soma(20,13), 33)
        self.assertEqual(self.calc.soma(100,400), 500)
        self.assertNotEqual(self.calc.soma(100,400), 50)
        with self.assertRaises(TypeError):
            self.calc.soma("x","y")
            self.calc.soma(4,"y")
            self.calc.soma("x",4)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(10,5), 5)
        self.assertEqual(self.calc.subtracao(20,10), 10)
        with self.assertRaises(TypeError):
            self.calc.subtracao("x","y")
            self.calc.subtracao(4,"y")
            self.calc.subtracao("x",4)

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(10,5), 50)
        self.assertEqual(self.calc.multiplicacao(5,5), 25)
        self.assertNotEqual(self.calc.multiplicacao(5,5), 20)
        self.assertNotEqual(self.calc.multiplicacao(10,0), 25)
        with self.assertRaises(TypeError):
            self.calc.multiplicacao("x","y")
            self.calc.multiplicacao(4,"y")
            self.calc.multiplicacao("x",4)

    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10,2), 5)
        self.assertNotEqual(self.calc.divisao(10,2), 6)
        self.assertEqual(self.calc.divisao(20,5), 4)
        with self.assertRaises(TypeError):
            self.calc.divisao("x","y")
            self.calc.divisao(4,"y")
            self.calc.divisao("x",4)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divisao(10,0)
            self.calc.divisao(50,0)

    def test_potenciacao(self):
        self.assertEqual(self.calc.potenciacao(0,3),0)
        self.assertEqual(self.calc.potenciacao(3,0),1)
        with self.assertRaises(TypeError):
            self.calc.potenciacao("x","y")
            self.calc.potenciacao(4,"y")
            self.calc.potenciacao("x",4)


    def test_raiz(self):
        self.assertEqual(self.calc.raiz_quadrada(100),10)
        self.assertEqual(self.calc.raiz_quadrada(25),5)
        self.assertEqual(self.calc.raiz_quadrada(81),9)
        self.assertNotEqual(self.calc.raiz_quadrada(100),11)
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-25)
            self.calc.raiz_quadrada(-10)
        with self.assertRaises(TypeError):
            self.calc.raiz_quadrada("x")
            self.calc.raiz_quadrada("y")
            self.calc.raiz_quadrada("x")

    def test_logaritimo(self):
        self.assertEqual(self.calc.logaritimo_natural(10),2.302585092994046)
        self.assertEqual(self.calc.logaritimo_natural(8),2.0794415416798357)
        self.assertNotEqual(self.calc.logaritimo_natural(8),2.07944154168)
        with self.assertRaises(ValueError):
            self.calc.logaritimo_natural(-10)
            self.calc.logaritimo_natural(0)
        with self.assertRaises(TypeError):
            self.calc.logaritimo_natural("x")
            self.calc.logaritimo_natural("y")
            self.calc.logaritimo_natural("x")

    def test_seno(self):
        self.assertEqual(self.calc.seno(20),0.3420201433256687)
        self.assertEqual(self.calc.seno(10),0.17364817766693033)
        self.assertEqual(self.calc.seno(60),0.8660254037844386)
        self.assertNotEqual(self.calc.seno(70),0.8660254037844386)
        with self.assertRaises(TypeError):
            self.calc.seno("x")
            self.calc.seno("y")
            self.calc.seno("x")

    
    def test_coseno(self):
        self.assertEqual(self.calc.coseno(20),0.9396926207859084)
        self.assertEqual(self.calc.coseno(10),0.984807753012208)
        self.assertEqual(self.calc.coseno(60),0.5000000000000001)
        self.assertNotEqual(self.calc.coseno(70),0.5000000000000001)
        with self.assertRaises(TypeError):
            self.calc.coseno("x")
            self.calc.coseno("y")
            self.calc.coseno("x")
        
    
    def test_tangente(self):
        self.assertEqual(self.calc.tangente(20),0.36397023426620234)
        self.assertEqual(self.calc.tangente(10),0.17632698070846498)
        self.assertEqual(self.calc.tangente(60),1.7320508075688767)
        self.assertNotEqual(self.calc.tangente(70),1.7320508075688767)
        with self.assertRaises(TypeError):
            self.calc.tangente("x")
            self.calc.tangente("y")
            self.calc.tangente("x")
        with self.assertRaises(ValueError):
            self.calc.tangente(90)
        

if __name__ == "__main__":
    unittest.main()