# A estrutura condicional if, else e elif é utilizada para tomar decisões com base em condições. 
# O bloco de código dentro do if será executado se a condição for verdadeira, enquanto o bloco dentro do else será executado se a condição for falsa.
#  O elif permite verificar múltiplas condições.
# IF verifica se a condição for verdadeira 
# ELIF verifica se a condição for falsa e se a segunda condição for verdadeira
# ELSE verifica se a condição for falsa e executa o bloco de código dentro dele
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode tirar Cnh.")
elif idade >= 16:
    print("Pode tirar Cnh com autorização dos pais.")
else:
    print("Não pode tirar Cnh.")




