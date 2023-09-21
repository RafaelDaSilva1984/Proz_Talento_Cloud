"""
Aula Def com array
"""

def achar_nome(elemento, listas):

    if elemento in listas:        
        i = listas.index(elemento)
        print("Encontrou", i)

    else:
        print("Não Encontrou, segue lista dos inscritos: ")
        for i in listas:
            print(i)



listas = ["ANA","MARIA","JORGE"]

while True:
    elemento = input("Digite nome a pesquisar: ").upper()
    if elemento == "X":
        print("Finalizando")
        break
    achar_nome(elemento, listas)