"""
Problema: João começou a se exercitar na academia e foi instruído por seu personal trainer
a descansar exatamente por 45 segundos entre os exercícios, porém ele sempre excede esse tempo.
Crie um programa que mostre o progresso desse intervalo em segundos e que avise sobre quando o tempo de descanso terminar.
"""
import time
intervalo = 0
for intervalo in range(45, 0, -1):
    print(f"Intervalo de => {intervalo}s")
    time.sleep(0.25)
    if intervalo == 15:        
        print("Finalizando, atenção")
        time.sleep(0.5)
    if intervalo == 1:
        print(" 0, Retomar Exrcícios...")
        time.sleep(0.5)