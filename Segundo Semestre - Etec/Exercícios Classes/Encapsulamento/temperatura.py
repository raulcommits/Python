class ControleTemperatura:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura < -50 and temperatura > 100:
            print("Temperatura inválida! Deve estar entre -50 e 100 graus Celsius.")
        else:
            self.__temperatura = temperatura

    def converter_para_fahrenheit(self):
        return self.__temperatura * 1.8 + 32
    
graus = ControleTemperatura(30)
print(f"A temperatura em Graus é: {graus.temperatura}°")
print(f"A temperatura em Fahrenheit é: {graus.converter_para_fahrenheit()}°")