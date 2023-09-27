"""
Num torneio de e-sports é necessário que todos os integrantes da mesma equipe tenham etiquetas que os identifiquem. 
Por exemplo, se o nome da equipe é “Os Lutadores”,o primeiro membro deve ter uma etiqueta “Os Lutadores – 1", 
o segundo membro “Os Lutadores – 2", e assim pela frente:

"""

print("Identificação de Lutadores E-sports da Turma - 6")
print(f"\n")
equipe=(input("Qual nome a ser registrado para sua Equipe: "))
lutadores=(int(input("Quantos lutadores em sua Equipe: ")))
print("Nome Registro da sua Equipe: ", equipe)
for lutadores in range(1,lutadores+1):    
    print("Os",equipe, "- Lutador ",lutadores)
print("Boa sorte nos Jogos....")