
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} - {self._like} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'{self._nome} - {self.temporadas} - {self._like} likes'


class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    @property
    def listagem(self):
        return self._programa

    def __len__(self):
        return len(self._programa)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
yesterday = Filme('yesterday', 2020, 100)
himym = Serie('How i met your mother', 2005, 9)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
yesterday.dar_like()
yesterday.dar_like()
yesterday.dar_like()

atlanta.dar_like()
atlanta.dar_like()
himym.dar_like()
himym.dar_like()

filmes_series = [vingadores, atlanta, yesterday, himym]
playlist_fds = Playlist('Fim de semana', filmes_series)

#verifica o tamanho da playlist
print(f'tamanho da playlist: {len(playlist_fds)}')

#passa os dados da playlist
for programa in playlist_fds:
    print(programa)

#verificar se a serie ta na playlist
print(himym in playlist_fds)
