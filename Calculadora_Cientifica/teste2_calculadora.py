import pytest
from calculadora import Calculadora_cientifica

x = Calculadora_cientifica()

def test_validar():
    assert x._validar(4,1) == True
    assert x._validar(4) == True
    assert x._validar(-10,1) == True
    assert x._validar(10,2.5) == True
    with pytest.raises(TypeError):
        x._validar(1,"1")
        x._validar("1","1")
        x._validar("1",1)

def test_soma():
    assert x.soma(4,1) == 5
    assert x.soma(4,0) != 5
    assert x.soma(10,-1) == 9
    with pytest.raises(TypeError):
        x.soma(1,"1")
        x.soma("1","1")
        x.soma("1",1)

def test_subtracao():
    assert x.subtracao(15,10) == 5
    assert x.subtracao(15,8) != 5
    assert x.subtracao(10,-10) == 20
    assert x.subtracao(-15,10) == -25
    with pytest.raises(TypeError):
        x.subtracao(1,"1")
        x.subtracao("1","1")
        x.subtracao("1",1)

def test_multiplicacao():
    assert x.multiplicacao(10,5) == 50
    assert x.multiplicacao(5,5) == 25
    assert x.multiplicacao(10,10) != 20
    assert type(x.multiplicacao(15,10)) == int
    with pytest.raises(TypeError):
        x.multiplicacao(1,"1")
        x.multiplicacao("1","1")
        x.multiplicacao("1",1)

def test_divisao():
    assert x.divisao(10,5) == 2
    assert x.divisao(5,5) == 1
    assert x.divisao(10,10) != 2
    assert type(x.divisao(15,10)) == float
    with pytest.raises(TypeError):
        x.divisao(1,"1")
        x.divisao("1","1")
        x.divisao("1",1)
    with pytest.raises(ZeroDivisionError):
        x.divisao(42,0)
        x.divisao(10,0)
        x.divisao(0,0)

def test_potenciacao():
    assert x.potenciacao(10,2) == 100
    assert x.potenciacao(0,3) == 0
    assert x.potenciacao(3,0) == 1
    assert type(x.potenciacao(15,10)) == float
    with pytest.raises(TypeError):
        x.potenciacao("x","y")
        x.potenciacao(4,"y")
        x.potenciacao("x",4)

def test_raiz():
    assert x.raiz_quadrada(100)== 10
    assert x.raiz_quadrada(25)==5
    assert x.raiz_quadrada(81)==9
    assert x.raiz_quadrada(100)!=11
    with pytest.raises(ValueError):
        x.raiz_quadrada(-25)
        x.raiz_quadrada(-10)
    with pytest.raises(TypeError):
        x.raiz_quadrada("x")
        x.raiz_quadrada("y")
        x.raiz_quadrada("x")

def test_logaritimo():
        assert x.logaritimo_natural(10)==2.302585092994046
        assert x.logaritimo_natural(8)==2.0794415416798357
        assert x.logaritimo_natural(8)!=2.07944154168
        with pytest.raises(ValueError):
            x.logaritimo_natural(-10)
            x.logaritimo_natural(0)
        with pytest.raises(TypeError):
            x.logaritimo_natural("x")
            x.logaritimo_natural("y")
            x.logaritimo_natural("x")

def test_seno():
        assert x.seno(20)==0.3420201433256687
        assert x.seno(10)==0.17364817766693033
        assert x.seno(60)==0.8660254037844386
        assert x.seno(70)!=0.8660254037844386
        with pytest.raises(TypeError):
            x.seno("x")
            x.seno("y")
            x.seno("x")

def test_coseno():
        assert x.coseno(20)==0.9396926207859084
        assert x.coseno(10)==0.984807753012208
        assert x.coseno(60)==0.5000000000000001
        assert x.coseno(70)!=0.5000000000000001
        with pytest.raises(TypeError):
            x.coseno("x")
            x.coseno("y")
            x.coseno("x")

def test_tangente():
        assert x.tangente(20)==0.36397023426620234
        assert x.tangente(10)==0.17632698070846498
        assert x.tangente(60)==1.7320508075688767
        assert x.tangente(70)!=1.7320508075688767
        with pytest.raises(TypeError):
            x.tangente("x")
            x.tangente("y")
            x.tangente("x")
        with pytest.raises(ValueError):
            x.tangente(90)