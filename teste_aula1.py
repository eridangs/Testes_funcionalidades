import unittest

from aula01 import classificacao

def test_temp_tropical():
    resultado = classificacao(100)
    assert resultado == "tempestade tropical"
    print("Teste test_temp_tropical v. 100: PASSOU")
   
    resultado = classificacao(62)
    assert resultado == "tempestade tropical"
    print("Teste test_temp_tropical v. 62: PASSOU")

    resultado = classificacao(118)
    assert resultado == "tempestade tropical"
    print("Teste test_temp_tropical v. 118: PASSOU")

def test_categoria_1():
    resultado = classificacao(119)
    assert resultado == "furacao de categoria 1"
    print("Teste test_categoria_1 v. 119: PASSOU")

    resultado = classificacao(153)
    assert resultado == "furacao de categoria 1"
    print("Teste test_categoria_1 v. 153: PASSOU")

    resultado = classificacao(140)
    assert resultado == "furacao de categoria 1"
    print("Teste test_categoria_1 v. 140: PASSOU")

def test_categoria_2():
    resultado = classificacao(154)
    assert resultado == "furacao de categoria 2"
    print("Teste test_categoria_2 v. 154: PASSOU")

    resultado = classificacao(177)
    assert resultado == "furacao de categoria 2"
    print("Teste test_categoria_2 v. 177: PASSOU")

    resultado = classificacao(160)
    assert resultado == "furacao de categoria 2"
    print("Teste test_categoria_2 v. 177: PASSOU")

def test_categoria_3():
    resultado = classificacao(178)
    assert resultado == "furacao de categoria 3"
    print("Teste test_categoria_3 v. 178: PASSOU")

    resultado = classificacao(209)
    assert resultado == "furacao de categoria 3"
    print("Teste test_categoria_3 v. 209: PASSOU")

    resultado = classificacao(190)
    assert resultado == "furacao de categoria 3"
    print("Teste test_categoria_3 v. 190: PASSOU")

def test_categoria_4():
    resultado = classificacao(210)
    assert resultado == "furacao de categoria 4"
    print("Teste test_categoria_4 v. 210: PASSOU")

    resultado = classificacao(249)
    assert resultado == "furacao de categoria 4"
    print("Teste test_categoria_4 v. 249: PASSOU")

    resultado = classificacao(230)
    assert resultado == "furacao de categoria 4"
    print("Teste test_categoria_4 v. 230: PASSOU")

def test_categoria_5():
    resultado = classificacao(250)
    assert resultado == "furacao de categoria 5"
    print("Teste test_categoria_5 v. 250: PASSOU")

    resultado = classificacao(280)
    assert resultado == "furacao de categoria 5"
    print("Teste test_categoria_5 v. 280: PASSOU")

def test_menor():
    resultado = classificacao(61)
    assert resultado == ""
    print("Teste ventos menor que 62km: PASSOU")

    resultado = classificacao(0)
    assert resultado == ""
    print("Teste ventos menor que 62km: PASSOU")

def test_char():
    resultado = classificacao("abc")
    assert resultado == ""
    print("Teste caracter: PASSOU")


if __name__ == "__main__":
    print("Executando Testes...")
    test_temp_tropical()
    test_categoria_1()
    test_categoria_2()
    test_categoria_3()
    test_categoria_4()
    test_categoria_5()
    test_menor()
    test_char()
