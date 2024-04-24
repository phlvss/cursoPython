nome = "PaUlo hEnRIquE"

print(nome.upper())
print(nome.lower())
print(nome.title())

nome = "       Paulo   "

print(nome.strip())  # remove os espaçamentos tanto da esquerda quando da direita
print(nome.lstrip()) # remove os espaçamentos da esquerda
print(nome.rstrip()) # remove os espaçamentos da direita

nome = "Python"

print("####" + nome + "####")
print(nome.center(14, "#"))
print(".".join(nome))