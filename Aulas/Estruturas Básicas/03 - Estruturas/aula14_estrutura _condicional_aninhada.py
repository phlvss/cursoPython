conta_normal = False
conta_universitaria = False
conta_especial = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saldo <= (saldo + cheque_especial):
        print("Saque realizado utilizando o cheque especial!")
    else:
        print("Saldo insuficaente!")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu o seu tipo de conta, entre em contato com o seu gerente!")