"""
A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, 
eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons, 
e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. 
Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. 


"""
lista_produtos = ['Máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
lista_produtos.pop()
lista_produtos[1],lista_produtos[4]='Rímel','Cremes Hidrantes'
qtd_produtos = len(lista_produtos)
lista_produtos.append('Escova de Cabelo')
lista_produtos.append('Protetor Solar')
for i in range(len(lista_produtos)):
    print('Produto : ',i + 1, lista_produtos[i],"á venda.")