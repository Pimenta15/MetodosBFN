import sympy

x = sympy.Symbol('x')
xk = 3.14 / 25
f = (3.14*((300/sympy.cos(x))**2) * 0.8)/(0.5*3.14*(14**2)*(1 + sympy.sin(x)-(sympy.cos(x)/2)))-1200
fd = sympy.diff(f, x)
e = 0.001
cont = 0

while (abs(f.subs(x, xk)) > e and abs(f.subs(x, xk))) or cont > 3:
    xk = xk - (f.subs(x, xk)/fd.subs(x, xk))
    cont += 1


print(xk)
