def sacar (saldo, saque, limite): # Inicio da função sacar
    if saldo >= saque and saque <= limite:
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possível realizar o saque.") # Fim da função sacar

    saldo = int (input("Digite o saldo atual: "))       
      