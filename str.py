# classe string python é famosa por se rica em métodos e possui uma grande variedade de funcionalidades que facilitam a manipulação de texto. Abaixo estão alguns dos métodos mais comuns e úteis da classe string em Python:
# 1. upper(): Converte todos os caracteres da string para maiúsculas.
# 2. lower(): Converte todos os caracteres da string para minúsculas.
# 3. strip(): Remove espaços em branco no início e no final da string.
# 4. replace(old, new): Substitui todas as ocorrências de uma substring por outra.
# 5. split(sep): Divide a string em uma lista de substrings com base em um separador especificado.
# 6. join(iterable): Junta uma lista de strings em uma única string, usando um separador especificado.
# 7. find(sub): Retorna o índice da primeira ocorrência de uma substring na string, ou -1 se não for encontrada.
# 8. isdigit(): Verifica se todos os caracteres da string são dígitos.
# 9. isalpha(): Verifica se todos os caracteres da string são letras.
# 10. format(): Permite formatar strings de maneira flexível, substituindo marcadores por valores específicos.
# 11. title(): Converte a primeira letra de cada palavra da string para maiúscula e as demais para minúscula.
nome = "GuIlHerMe "
print(nome.upper())
print (nome.lower())
print (nome.strip())
print (nome.title())






texto = "Olá mundo, seja uma pessoa legal"
print (texto)
print(texto.upper())
print (texto.lower())
print (texto.strip())
print (texto.rstrip())
print (texto.lstrip())


menu = "Python"
print ("####" + menu + "####")
print (menu.center(20))
print (menu.center(20, "#"))
print ("-".join (menu))
print ("p-y-r-o-t-h-o-n")

for letra in menu:
    print(letra, end="")
print ()

###Interpolação: Em python temos 3 formas de intepolar variaveis em  strings
# a primeira o sinal de %, a segunda é utilizando o método a format e a ultima é utilizando f string
nome = "Guilherme" 
idade = 26
profissão = "Programador"
linguagem = "Python"
print ("Olá, meu nome é %s, tenho %d anos e sou %s. Minha linguagem favorita é %s." % (nome, idade, profissão, linguagem))

nome = "Pedro"
age = 87
profissão = "Engenheiro"
linguagem = "PHP"
print ("Olá, meu nome é {0}, tenho {1} anos e sou {2}. Minha linguagem favorita é {3}.".format(nome, age, profissão, linguagem))


pi  = 3.987
print (f"O valor de pi é {pi:.1f}")

nome = "Mulanbo de ferraz"
print (nome[12])
print (nome[2])
print (nome[6])
print (nome[8])
print (nome[12])


#Strings são imutáveis em Python, o que significa que uma vez criada, uma string não pode ser alterada. No entanto, você pode criar novas strings a partir de operações em strings existentes. Por exemplo, você pode concatenar strings usando o operador + ou repetir strings usando o operador *.
#Strings de multiplas linhas podem ser criadas usando aspas triplas (''' ou """). Isso é útil para criar strings longas ou para incluir quebras de linha dentro da string.
#Exemplo de string de multiplas linhas:
texto_multilinha = """
Esta é uma string de múltiplas linhas.
Pode conter várias linhas de texto.
"""
print(texto_multilinha)

nome = "Matheus"
mensagem = f"""Olá meu nome é {nome}.
Eu estou aprendendo Python e estou achando muito interessante trabalhar com strings."""
print(mensagem)

print (""" 
=========== MENU ============
   1 depositar
    2 sacar
    3 extrato
    0 sair
""")