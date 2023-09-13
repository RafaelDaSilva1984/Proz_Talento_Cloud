
print("Restaurante Proz ... Escolha sua Loclização: ")

print("""Digite:
        Opção [1] Grupo maior que 5 pessoas, 1º Andar 
        Opção [2] Grupo menor que 5 pessoas, Terreo
        Opção [3] Grupo fumantes ou animais de estimação, Externo 
        Opção [4] Finalizar...
       """)

while True:
    opcao=(int(input("Digite sua opção: ")))
    if opcao == 1:
        print("Sua localização será 1º Andar...")
    elif opcao == 2:
        print ("Sua locação será o Térreo...")
    elif opcao == 3:
        print("Sua localização será área Externa...")
    elif opcao == 4:
        print("Finalizando acesso...")
        break
    else:
        print("Opção Incorreta...")
        
