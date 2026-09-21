Conta_normal = 30000
saque = int (input ("Digite o valor que deseja sacar: "))
Cheque_especial = 5000
if saque <= Conta_normal:
    print ("Saque realizado com sucesso")
    Conta_normal = Conta_normal - saque
    print ("Saldo atual", Conta_normal)
elif saque <= Cheque_especial:
    print ("Saque realizado com sucesso")
    Cheque_especial = Cheque_especial - saque
    print ("Saldo atual", Cheque_especial)
else:
    print ("Saque não realizado")