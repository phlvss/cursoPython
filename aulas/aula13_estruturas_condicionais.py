MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:                                # IF 
    print("Maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:                               # IF ELSE 
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:                                #IF, ELSE IF e ElSE
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode realizar as aulas teéoricas, mas não pode realizar as aulas práticas.")
else:
    ("Ainda não pode tirar a CNH.")


