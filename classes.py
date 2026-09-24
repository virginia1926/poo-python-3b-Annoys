#xemplo edição primeira aula 
class Conteudo:

    def __init__(self, titulo: str, ano: int):
        self.titulo = titulo
        self.ano = ano

    def exibir_detalhes(self):
        """Método que será sobrescrito nas classes filhas (Polimorfismo)."""
        return f"Título: {self.titulo} | Ano: {self.ano}"



class Filme(Conteudo):

    def __init__(self, titulo: str, ano: int, duracao_minutos: int):
        super().__init__(titulo, ano)
        self.duracao_minutos = duracao_minutos

    def exibir_detalhes(self):
        return (
            f"[FILME] {self.titulo} ({self.ano}) - Duração: {self.duracao_minutos} min"
        )



class Serie(Conteudo):

    def __init__(self, titulo: str, ano: int, temporadas: int):
        super().__init__(titulo, ano)
        self.temporadas = temporadas

    def exibir_detalhes(self):
        return f"[SÉRIE] {self.titulo} ({self.ano}) - {self.temporadas} Temporada(s)"


class Podcast(Conteudo):

    def __init__(self, titulo: str, ano: int, apresentador: str):
        super().__init__(titulo, ano)
        self.apresentador = apresentador

    def exibir_detalhes(self):
        return f"[PODCAST] {self.titulo} ({self.ano}) - Apresentado por: {self.apresentador}"




catalogo: list[Conteudo] = [
    Filme("Madagascar", 2005, 86),
    Serie("Diários de um Vampiro", 2009, 8),
    Podcast("Podpah", 2020, "Igão e Mítico"),
]


print("--- Catálogo da Plataforma ---")
for item in catalogo:
    print(item.exibir_detalhes())
