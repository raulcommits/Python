class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        
        
class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.numportas = portas
    
    def MostrarCarro(self):
        print(f"O carro é da marca {self.marca}, do ano {self.ano} e tem {self.numportas} portas.")
        
class Moto(Veiculo):
    def __init__(self, marca, ano, guidao):
        super().__init__(marca, ano)
        self.tipoguidao = guidao
        
    def MostrarMoto(self):
        print(f"A moto é da marca {self.marca}, do ano {self.ano} e tem o tipo {self.tipoguidao} de guidão.")
        
umCarro = Carro("Honda", 2001, 4)
umaMoto = Moto("Yamaha", 2004, "Flat")

umCarro.MostrarCarro()
umaMoto.MostrarMoto()