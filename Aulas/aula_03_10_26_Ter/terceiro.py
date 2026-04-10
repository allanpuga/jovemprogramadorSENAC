frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
numeros = [1, 2, 3, 4, 5]

# Acessando elementos
print ('Primeira fruta:', frutas[0])  # maçã
print ('Última fruta:', frutas[-1])  # abacaxi

# Modificando elementos
frutas[1] = "manga"
print ('Frutas após modificação:', frutas)

# Adicionando elementos
frutas.append("pera")
frutas.insert(2, "kiwi")
print ('Frutas após adição:', frutas)

# Removendo elementos
frutas.remove("laranja")
ultima_fruta = frutas.pop()  # remove a última fruta
print ('Frutas após remoção:', frutas)
print ('Fruta removida:', ultima_fruta)

# Tamanho (quantidade de elementos)
print ('Número de frutas:', len(frutas))

# Fatiamento (slicing)
print ('Frutas do índice 1 ao 3:', frutas[1:4])  # do índice 1 ao 3 (exclusivo)
print ('Frutas do início ao índice 2:', frutas[:3])  # do início ao índice 2 (exclusivo)
print ('Frutas do índice 2 ao final:', frutas[2:])  # do índice 2 ao final

# Verificando se um elemento está na lista
print ('Banana está na lista?', "banana" in frutas)
print ('Manga está na lista?', "manga" in frutas)   

# Outras operações uteis
print ('Lista original de números:', numeros)
print ('Soma dos números:', sum(numeros))
print ('Maior número:', max(numeros))
print ('Menor número:', min(numeros))
numeros.reverse()
print ('Números invertidos:', numeros)
numeros.sort()
print ('Números ordenados:', numeros)
numeros.sort(reverse=True)
print ('Números ordenados decrescente:', numeros)

# Iterar sobre a lista
print ('Frutas na lista:')
for fruta in frutas:
    print ('- ' + fruta)

# Lista compreensão (exemplo simples)
numeros_quadrados = [x**2 for x in numeros]
print ('Quadrados dos números:', numeros_quadrados)

