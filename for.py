texto = input ("Informe um textos:")
vogais = "aeiou"
# Exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in vogais:
        print (letra, "é uma vogal.")
else:
    print() # adiciona uma quebra de linha após a execução do loop
    # Exemplo utilizando a função range()
for numero in range (1, 11):
    print (numero)
    