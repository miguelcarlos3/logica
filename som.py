while True:
    numero = int(input("informe um numero"))
    if numero == 10:
     break

    print (numero)
# While é utilizada para executar um bloco de código enquanto uma condição for verdadeira.
# Break é utilizada para sair de um loop antes que ele termine.
# Continue é utilizada para pular para a próxima iteração de um loop.
for numero in range(100):
   if numero == 10:
      continue 
   print (numero)