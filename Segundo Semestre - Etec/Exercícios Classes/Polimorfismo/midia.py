class Midia:
    def exibir_info(self):
        return ("")
        
class Livro(Midia):
    def exibir_info(self):
        livro = "Um Milhão de Finais Felizes"
        autor = "Vitor Martins"
        paginas = "344"
        return ("Livro: " + livro, "Autor: " + autor, "Páginas: " + paginas) # Vitor Martins, 344 páginas
    
class Filme(Midia):
    def exibir_info(self):
        filme = "De Volta para o Futuro"
        diretor = "Robert Zemeckis"
        duracao = "116 minutos"
        return ("Filme: " + filme, "Diretor: " + diretor, "Duração: " + duracao) # Robert Zemeckis, 116 minutos
    
class Musica(Midia):
    def exibir_info(self):
        musica = "Everybody Wants to Rule The World"
        artista = "Tears for Fears"
        duracao = "291 segundos"
        return ("Música: " + musica, "Artista: " + artista, "Duração: " + duracao) # Tears for Fears, 291 segundos
    
def mostrar_midia(midia):
    print(midia.exibir_info())

midias = [Livro(), Filme(), Musica()]

for midia in midias:
    mostrar_midia(midia)