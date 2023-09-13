""" 
Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:

caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;

caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.
"""
contador = 0


def calculadora(valor1, valor2):
    soma = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2 

    if opcao == 1:
        res = soma, "Valor Par"
        if soma % 2 != 0:
            res = "Valor Impar"              
    elif opcao == 2:
        res = subtracao, "Valor  Par"
        if subtracao % 2 != 0:
            res = "Valor Impar" 
    elif opcao == 3:
        res = multiplicacao, "Valor Par"
        if multiplicacao % 2 != 0:
            res = "Valor Impar"
    elif opcao == 4:
        res = divisao, "Valor Par"
        if divisao % 2 != 0:
            res = "Valor Impar"
    else:
        res = "Par"                    
    return res    


valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
opcao = int(input('Opcao: '))
res = calculadora(valor1, valor2)


while opcao not in (0,1,2,3,4):    
    print('Opção inválida')
    opcao = int(input('Digite novamente Opcao [0 Sair, 1 Soma + , 2 Subtração - , 3 Multiplicação * , 4 Divisão / ]:  '))
    contador += 1
    if opcao == 0:         
         break    


while res == "Valor Impar":  
    print("Valor Incorreto Resultado IMPAR")
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    opcao = int(input('Opcao: '))
    res = calculadora(valor1, valor2)
    contador +=1
if res == "Valor Impar":
    print("Ocorreu erro valor Impar")
else:  
    print(res)
        
        