#Declaração e Tipos

numero = 5
print("Número = ", numero)
print(type(numero))

bebida_favorita = ("Guarana Antarctica")
print("Qual Bebida é a Favorita: ",bebida_favorita)
print(type(bebida_favorita))

preco_bebida = 5.5
print("Qual Preço da Bebida: ", preco_bebida)
print(type(preco_bebida))

bebida_alcoolica = False
print("A Bebida é alcoolica: ", bebida_alcoolica)
print(type(bebida_alcoolica))

#Operadores Aritméticos

almoco_favorita = "X-Filé Churrasco"
almoco_preco = 21.99
orcamento = 24.50

resultado = orcamento - almoco_preco
print('Restanto de orçamento R$ {:.2f}'.format (resultado ))

resultado_dois = almoco_preco * 2
print ("Valor gastos",resultado_dois)

resultado_tres = almoco_preco / 10
print('Dividindo o valor em duas partes de R$:', resultado_tres)

#Operadores Relacionais e Condicionais

valor_total_almoco = 122
qtd_pessoas = 5
divisao_almoco = valor_total_almoco / qtd_pessoas
print(divisao_almoco," e ", orcamento)

if divisao_almoco <= orcamento:
    print ('Bom almoço, sobra de R$', orcamento - divisao_almoco)
else:
    print ('Valor fora oraçemto, Muito caro, desculpe!')