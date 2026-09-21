
def exibir_mensagem():
    print ("olá mundo")

def exibir_mensagem_2(nome):
    print (f"Seja bem vindo {nome}")

def exibir(nome = "matheus"):
    print (f"oi tudo bem {nome}")

exibir_mensagem_2(nome = "fera")
exibir(nome = "Kauan")

def carro(marca,modelo,placa):
    print (f"inserido com sucesso {marca}/{modelo}/{placa}")
carro("fiat","taus", "bua-3452")
carro = input ("coloque o {marca}/{modelo}/{placa}")

def calculadora (a,b):
    resultado = a + b
    print (resultado)


a = int (input ("digite o valor"))
b = int (input ("digete o valor "))

salario = 3547

def salario_bonus (bonus):
    global salario
    salario += bonus
    return salario

print (salario_bonus)