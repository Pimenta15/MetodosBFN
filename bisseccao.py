import math 

class bisseccao :

    @staticmethod
    def funcao(x):
        resultado = ((math.pi * (300 / math.cos(x)) ** 2 * 0.8) /
                     (0.5 * math.pi * 14 ** 2 * (1 + math.sin(x) - 0.5 * math.cos(x)))) - 1200
        return resultado

    @staticmethod
    def calculo(a ,b):
        format_str = "{:,.3f}"
        x = (a+b ) / 2
        erro = abs((a-b) )/2

        while erro >0.001 :
            fa = bisseccao.funcao(a);
            fb = bisseccao.funcao(b );
            fx = bisseccao.funcao(x);
            
            print("A:", format_str.format(a))
            print("B:", format_str.format(b))
            print("Xi:", format_str.format(x))
            print("fa:", format_str.format(fa))
            print("fb:", format_str.format(fb))
            print("fx:", format_str.format(fx))

             
            if fa*fb > 0 :
               erro = abs(x-a)
            else :
               erro = abs(x-b)   

            if a>0 and fx>0 or a<0 and fx<0:
               a = x;
            else:
               b = x;

            print("Erro : " , format_str.format(x))
            print("\n")
            x= (a+b)/2