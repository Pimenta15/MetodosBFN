import math

class Bisseccao:
    precisao = 10 ** -3
    cont = 0

    def calculo(a, b):
        format_str = "{:,.3f}"
        xi = (a + b) / 2
        fa = Bisseccao.funcao(a)
        fb = Bisseccao.funcao(b)
        fx = Bisseccao.funcao(xi)
        
        print("ID:",Bisseccao.cont)
        print("A:", format_str.format(a))
        print("B:", format_str.format(b))
        print("Xi:", format_str.format(xi))
        print("fa:", format_str.format(fa))
        print("fb:", format_str.format(fb))
        print("fx:", format_str.format(fx))
        Bisseccao.cont += 1
        if (fx > 0 and fa < 0) or (fx < 0 and fa > 0):
            erro = abs(xi - a)
            print("erro:", format_str.format(erro), "\n")
            if erro > Bisseccao.precisao:
                Bisseccao.calculo(a, xi)
        
        if (fx > 0 and fb < 0) or (fx < 0 and fb > 0):
            erro = abs(xi - b)
            print("erro:", format_str.format(erro), "\n")
            if erro > Bisseccao.precisao:
                Bisseccao.calculo(xi, b)

    def funcao(x):
        resultado = ((math.pi * (300 / math.cos(x)) ** 2 * 0.8) /
                     (0.5 * math.pi * 14 ** 2 * (1 + math.sin(x) - 0.5 * math.cos(x)))) - 1200
        return resultado