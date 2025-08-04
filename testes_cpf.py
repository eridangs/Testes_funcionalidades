import unittest


from cpf import validar_cpf

def cpf_visivelmente_falso():
    cpf = "123.456.789-000"
    resultado = validar_cpf(cpf)
    assert resultado == False
    print(f"CPF {cpf} visivelmente falso")

    cpf = "111.111.111-11"
    resultado = validar_cpf(cpf)
    assert resultado == False
    print(f"CPF {cpf} visivelmente falso")

def cpf_completo_invalido():
    cpf = "123.456.789-01"
    resultado = validar_cpf(cpf)
    assert resultado == False
    print(f"CPF {cpf} completo inválido")

def cpf_valido():
    cpf = "087.937.681-33"
    resultado = validar_cpf(cpf)
    assert resultado == True
    print(f"CPF {cpf} completo válido")

def cpf_sem_formato():
    cpf = "12345678909"
    resultado = validar_cpf(cpf)
    assert resultado == True
    print(f"CPF {cpf} sem formatação de pontos e traço")
    
def cpf_caracteres_errados():
    cpf = "123.456.789.09"
    resultado = validar_cpf(cpf)
    assert resultado == True
    print(f"CPF {cpf} sem formatação correta de pontos e traço")

    cpf = "123-456-789-09"
    resultado = validar_cpf(cpf)
    assert resultado == True
    print(f"CPF {cpf} sem formatação correta de pontos e traço")

def cpf_numero_inteiro():
    cpf = 12345678909
    resultado = validar_cpf(cpf)
    assert resultado == False
    print(f"CPF {cpf} dado como número")

def caracteres_invalidos_letras():
    cpf = "123.456.789-0a"
    resultado = validar_cpf(cpf)
    assert resultado == False
    print(f"CPF {cpf} com caracteres inválidos")

    cpf = "gyu.put.qbp-ba"
    resultado = validar_cpf(cpf)
    assert resultado == False
    print(f"CPF {cpf} com caracteres inválidos")


if __name__ == "__main__":
    print("Executando Testes...")
    cpf_visivelmente_falso()
    cpf_completo_invalido()
    cpf_valido()
    cpf_sem_formato()
    cpf_caracteres_errados()
    cpf_numero_inteiro()
    caracteres_invalidos_letras()