Saldo = int (input ("Enter com valor"))
Saque = int (input ("valor que quer retirar"))
Limite_saque_diario = 800 
if  Saque > Limite_saque_diario:
    print ("saque não realizado ")
else:
    Saldo_final = Saldo - Saque 
    print ("saque realizado")
    print ("Saldo final", Saldo_final)



    