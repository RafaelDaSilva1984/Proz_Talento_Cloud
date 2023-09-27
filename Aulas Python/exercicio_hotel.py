"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares.
Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...) 
"""
import time
print("Hotel e seus ANDARES WHILE")
andares = 22
while andares > 1:
    andares -= 1
    if andares == 13:
        continue
    print("Andar",andares)
    time.sleep(0.25)
    
    
import time
print(f"\n")
print("Hotel e seus ANDARES FOR CONTINUE")
andares = 0
for andares in range(21,0,-1):
    if andares == 13:
        continue
    print("Andar",andares)    
    time.sleep(0.25)
    
    
import time
print(f"\n")
print("Hotel e seus ANDARES FOR")
andares = 0
for andares in range(21,13,-1):
    print("Andar",andares)
    time.sleep(0.25)
for andares in range(12,0, -1):
    print("Andar",andares)
    time.sleep(0.25)
