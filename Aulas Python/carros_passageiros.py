"""Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
E: Veículos com quatro rodas ou mais e com mais de 6000 kg."""

print("Categoria de Habilitação")
print("Informe dados do Carro")
a = ("Veículos com duas ou três rodas, CATEGORIA = A")
b = ("Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg, CATEGORIA = B")
c = ("Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg, CATEGORIA = C")
d = ("Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas, CATEGORIA = D")
e = ("Veículos com quatro rodas ou mais e com mais de 6000 kg, CATEGORIA = E")

rodas=int(input("Quantos rodas possui veículo: "))
peso=float(input("Qual peso do veículo: "))
passageiros=int(input("Quantos passageiros: "))
if rodas <= 3:
    print("{}".format(a))
elif (rodas == 4)  and (peso <= 3500 and (passageiros <= 8)):
    print("{}".format(b))
elif rodas >= 4 and peso >= 3500  and peso <= 6000 and passageiros <= 8 :
    print("{}".format(c))
elif rodas >= 4 and passageiros > 8:
    print("{}".format(d))
elif rodas >= 4 and peso > 6000:
    print("{}".format(e))
else:
    print('Dados Inválidos')