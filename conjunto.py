 # Conjuntos são uma estrutura de dados chamada set.
 # Um set é uma coleção que não possui objetos repetidos, usamos sets para representar 
 # conjuntos matemáticos 
 # Conjutos em python não suportam indexação e nem fatiamento, caso queria acessar tem que transforma em uma lista

numero =set ([1,2,3,4,5,6,7,8,9,1])
print (numero)

fruta = set ("Abacaxi")
print (fruta)

compras = set (("Banana","Arroz","Pepino"))
print (compras)

sequencia = {1,2,3,4,5,6,7,8}
sequencia = list(sequencia)
sequencia [2]
print (sequencia[2])

cars = {"Tesla","celta","GWM"}
for indice, cars in enumerate (cars):
    print (f"{indice}: {cars}")

conjunto_A = {2,6,9}

conjunto_B = {6,8,9}

conjunto_A.union(conjunto_B)

conjunto_A.intersection(conjunto_B)

conjunto_A.difference(conjunto_B)

conjunto_B.issubset(conjunto_A)

print (conjunto_A.union(conjunto_B))
print (conjunto_A.intersection(conjunto_B))
print (conjunto_B.issubset(conjunto_A))
