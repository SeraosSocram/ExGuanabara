from math import sqrt
ctt_oposto = float(input("Comprimento do cateto oposto: "))
ctt_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = sqrt(pow((ctt_oposto), 2) + pow((ctt_adjacente), 2))
print(f"A hipotenusa vai medir {(hipotenusa):.2f}")

# solução usando import math
# hipotenusa = math.hypot(ctt_oposto, ctt_adjacente)
