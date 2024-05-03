class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):  # self = referêcia pro objeto, é uma referencia explicita
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")

    def correr(self):
        print("Vrum...")

    def trocar_marcha(self, nmr_marcha):
        print("Trocando Marcha...")

        def _trocar_marcha(nmr_marcha):
            if nmr_marcha > self.marcha:
                print("Marcha trocada... ")
            else:
                print("Não foi possível trocar de marcha...")


    def __str__(self): # alterações teram de ser feitas manualmente
        return f"Bicileta: Cor:{self.cor}, Modelo:{self.modelo}, Ano:{self.ano}, Valor:R${self.valor}"
    
    def __str__(self): # não será necesssário realizar alterações, pois será realizado automaticamente
        return f"{self.__class__.__name__}: {''.join([f'{chave}={valor}' for chave, valor in self.__dict__.itens()])}"
        


b1 = Bicicleta("Azul", "Caloi", 2024, 1500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Amarela", "Caloi", 2022, 600)
print(b2)


