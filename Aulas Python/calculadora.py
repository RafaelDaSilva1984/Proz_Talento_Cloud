"""Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação 
e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""
print("Função Calculadora ")
contador = 0
def calculadora(valor1, valor2):
    soma = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2 
    
    if opcao == 1:
        return soma, " Escolheu Soma de valores"
    elif opcao == 2:
        return subtracao, " Escoheu Subtração de valores"
    elif opcao == 3:
        return multiplicacao, " Escolheu Multiplicação de valores"
    elif opcao == 4:
        return divisao, " Escolheu Divisão de valores"
    else:
        return " Sua Escolha foi Opção Inválida ou 0 Sair.."
    

valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
opcao = int(input('Opcao: '))
while opcao not in (0,1,2,3,4):    
    print('Opção inválida')
    opcao = int(input('Digite novamente Opcao [0 Sair, 1 Soma + , 2 Subtração - , 3 Multiplicação * , 4 Divisão / ]:  '))
    contador += 1
    if opcao == 0:         
         break
     
valor_calculado = calculadora(valor1, valor2)
print(valor_calculado)
