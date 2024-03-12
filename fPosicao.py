import math
class FalsaPosicao:
    precisao = 10**-3
    cont = 0

    @staticmethod
    def falsa_posicao(a, b):
        precisao = 10**-3
    cont = 0

    @staticmethod
    def main():
        FalsaPosicao.falsa_posicao(0, math.pi/25)

    @staticmethod
    def falsa_posicao(a, b):
        format_str = "{:,.3f}"
        print("ID:", FalsaPosicao.cont)
        FalsaPosicao.cont += 1

        fa = FalsaPosicao.funcao(a)
        fb = FalsaPosicao.funcao(b)

        xi = b - ((b - a) * fb) / (fb - fa)
        fx = FalsaPosicao.funcao(xi)

        print("A:", format_str.format(a))
        print("B:", format_str.format(b))
        print("Xi:", format_str.format(xi))
        print("fa:", format_str.format(fa))
        print("fb:", format_str.format(fb))
        print("fx:", format_str.format(fx))

        erro = abs(xi - b) if abs(xi - b) < abs(xi - a) else abs(xi - a)
        print("Erro:", format_str.format(erro))

        if erro <= FalsaPosicao.precisao:
            print("A solução foi encontrada")
            return

        FalsaPosicao.falsa_posicao(xi, b)


    @staticmethod
    def funcao(x):
        resultado = ((math.pi*((300/math.cos(x))**2) *0.8)/ (0.5* math.pi*(14**2)*(1 + math.sin(x)-0.5*math.cos(x))) )-1200
        return resultado



