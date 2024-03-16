import math 

class bisseccao :

    @staticmethod
    def função(a):
     x = int(a)
     resultado = ((math.pi*((300/math.cos(x))**2) *0.8)/ (0.5* math.pi*(14**2)*(1 + math.sin(x)-0.5*math.cos(x))) )-1200
     return resultado

    @staticmethod
    def calculo(a ,b):
        format_str = "{:,.3f}"
        x = (a+b ) / 2
        erro = abs((a-b) )/2

        while erro >0.01 :
            fa = bisseccao.função(a);
            fb = bisseccao.função(b );
            fx = bisseccao.função(x);
             
            if fa*fb > 0 :
               erro = abs(x-a)
            else :
               erro = abs(x-b)   

            if a>0 and fx>0 or a<0 and fx<0:
               a = x;
            else:
               b = x;

            print(format_str.format(x))
            x= (a+b)/2