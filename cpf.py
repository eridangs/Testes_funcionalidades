def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    if type(cpf) == int:
        return False
    else:
        cpf = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se tem 11 dígitos ou se todos são iguais
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        # Função para calcular um dígito verificador
        def calcular_digito(cpf_parcial, peso_inicial):
            soma = sum(int(digito) * peso for digito,
            peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))

            resto = (soma * 10) % 11
            return '0' if resto == 10 else str(resto)
        
        # Calcula os dois dígitos verificadores
        digito1 = calcular_digito(cpf[:9], 10)
        digito2 = calcular_digito(cpf[:10], 11)
        
        # Verifica se os dígitos calculados batem com os informados
        return cpf[-2:] == digito1 + digito2
        # Cpf valido na receita federal true or false
