

import math

from fPosicao import FalsaPosicao
from newtonRaphson import newtonRaphson
from bisseccaoP import Bisseccao 

print("Escolha um método:")
print("1. Método Bissecção")
print("2. Método Falsa Posição")
print("3. Método de Newton")

escolha = int(input("Digite o número correspondente ao método desejado: "))
if escolha == 1 :
   
   Bisseccao.calculo(0,(math.pi/25))
elif escolha == 2:
    FalsaPosicao.falsa_posicao(0,(math.pi/25))
else:
    newtonRaphson.nR(math.pi/25)