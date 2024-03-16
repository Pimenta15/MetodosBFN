import sympy 
import math

class newtonRaphson:
    @staticmethod
    def exibir(xk, f, cont):
        format_str = "{:,.3f}"
        print("ID:", cont)
        print("Xi:", format_str.format(xk))
        print("fx:", format_str.format(f))

    @staticmethod
    def nR(xk):
        x = sympy.Symbol('x')
        f = (math.pi * ((300 / sympy.cos(x))**2) * 0.8) / (0.5 * math.pi * (14**2) * (1 + sympy.sin(x) - (sympy.cos(x) / 2))) - 1200
        fd = sympy.diff(f, x)
        e = 0.001
        cont = 0

        while abs(f.subs(x, xk)) > e:
            xk = xk - (f.subs(x, xk) / fd.subs(x, xk))
            newtonRaphson.exibir(xk, f.subs(x, xk), cont)
            cont += 1

