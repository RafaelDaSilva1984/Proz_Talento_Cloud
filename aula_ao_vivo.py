def multplicar(n1, n2):
    return n1 * n2
for valor in range(1,11):
    for i in range(1,11):  
        multi = multplicar(valor,i)
        print(f"Tábuada {valor} X {i} = " , multi)
    
