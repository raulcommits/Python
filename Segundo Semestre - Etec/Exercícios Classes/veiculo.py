class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        
    def atributos(self):
        pass
        
class Carro(Veiculo):
    def atributos(self, portas):
        self.numportas = portas
        return(f"O carro é da marca {self.marca}, do ano {self.ano} e tem {self.numportas} portas.")
        
class Moto(Veiculo):
    def atributos(self, guidao):
        self.tipoguidao = guidao
        

carro = Veiculo("Fiat", 2011), Carro(2011, 4)
moto = Veiculo("Honda", 2009), Moto(2009, "Flat")

print(carro.atributos())