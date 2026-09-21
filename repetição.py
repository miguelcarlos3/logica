# estruturas de repetição são utilizadas para executar um bloco de código várias vezes, enquanto uma condição for verdadeira.
# FOR é utilizada para percorrer uma sequência de elementos, como uma lista ou uma string, e executar um bloco de código para cada elemento da sequência.
# WHILE é utilizada para executar um bloco de código enquanto uma condição for verdadeira.
# BREAK é utilizada para sair de um loop antes que ele termine.
# CONTINUE é utilizada para pular para a próxima iteração de um loop.
# FOR ELSE é utilizada para executar um bloco de código quando o loop for concluído sem interrupção.
# FUNÇÃO RANGE é utilizada para gerar uma sequência de números, que pode ser utilizada em um loop FOR.
texto = input("Digite um texto: ")
Vogais = "aeiouAEIOU"
for letra in texto:
    if letra.upper() in Vogais:
        print (letra, "é uma vogal.")

print()
