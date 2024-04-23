nome = "Paulo"
idade = 19
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Paulo", "idade": "19", "profissao": "Programador", "linguagem": "Python"}

print("Olá, me chamo %s, possuo %d anos. Atualmente sou %s, estando mais focado no %s" % (nome, idade, profissao,linguagem))

print("Olá, me chamo {}, possuo {} anos. Atualmente sou {}, estando mais focado no {}".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {2}, possuo {0} anos. Atualmente sou {3}, estando mais focado no {1}".format(idade, linguagem, nome, profissao))

print("Olá, me chamo {nome}, possuo {idade} anos. Atualmente sou {profissao}, estando mais focado no {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print(f"Olá, me chamo {nome}, possuo {idade} anos. Atualmente sou {profissao}, estando mais focado no {linguagem}")

print("Olá, me chamo {nome}, possuo {idade} anos. Atualmente sou {profissao}, estando mais focado no {linguagem}".format(**dados))