conta = True
conta_universitaria = False

saldo = 1490
saque = 3500
cheque_especial = 26388

if conta:
    if saque <= saldo:
        print ("saque realizado")
    elif saque <= (saldo + cheque_especial):
        print ("saque realizado com cheque especial")
    else:
        print ("saque não realizado")
elif conta_universitaria:
    if saque <= saldo:
        print ("saque realizado")
    else:
        print ("saque não realizado")
# IF tenario permite fazer uma condição em uma linha só
# IF aninhado podemos criar estruturas condicionais animhadas, ou seja, uma condição dentro de outra condição.

