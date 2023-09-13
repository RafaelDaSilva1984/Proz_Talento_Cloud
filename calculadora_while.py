""" 
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. 
Quando o usuário escolher a opção “Sair”, o sistema irá parar.
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

while opcao != 0:
    escolha = input("Deseja continuar: S para 'Sim' e N para 'Não': ").upper()
    if   escolha == "N":
        print("Finalizando....")
        break
    valor1 = float(input("Valor 1: "))
    valor2 = float(input("Valor 2: "))
    opcao = int(input('Opcao: '))
    contador += 1
    if opcao == 0:         
        break
   
    valor_calculado = calculadora(valor1, valor2)
    print(valor_calculado)

