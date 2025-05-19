class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
        
pessoa = Pessoa("Raul", 19)
pessoa.falar()