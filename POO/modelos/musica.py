class Musica:
    Musicas = []
    
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.Musicas.append(self)

    def __str__(self): 
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.Musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica('Aquarela', 'Toquinho', '3:00')
musica2 = Musica('Coração', 'Melim', '3:00')
musica3 = Musica('Paciência', 'Lenine', '3:00')

Musica.listar_musicas()   