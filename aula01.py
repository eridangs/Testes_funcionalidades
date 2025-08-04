def classificacao (velocidade):
    if type(velocidade) == str:
        return ""
    else:
        if (velocidade >= 62 and velocidade <= 118):
            return "tempestade tropical"
        elif (velocidade >= 119 and velocidade <= 153):
            return "furacao de categoria 1"
        elif (velocidade >= 154 and velocidade <= 177):
            return "furacao de categoria 2"
        elif (velocidade >= 178 and velocidade <= 209):
            return "furacao de categoria 3"
        elif (velocidade >= 210 and velocidade <= 249):
            return "furacao de categoria 4"
        elif (velocidade >= 250):
            return "furacao de categoria 5"
        else:
            return ""
        
# Bloco principal para executar os testes