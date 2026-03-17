# Criar classe Musica
class Musica:
	def __init__(self, nome, artista, estilo):
		self.nome = nome
		self.artista = artista
		self.estilo = estilo
	
	def tocar(self):
		return f"tocando '{self.nome}' por self.artista..."

# Instanciando objetos da classe Musica
# instanciando o objeto m1
m1 = Musica(
	'Sexo, Violencia y Llantas',
	'Rosalía',
	['Pop', 'Rock', 'Alternativo']
)

# instanciando o objeto m2
m2 = Musica(
    'Flutua',
    'Johnny Hooker',
    ['Pop', 'Rock', 'MPB']
)

# instanciando o objeto m3
m3 = Musica(
    'Veludo Marrom',
    'Liniker',
    ['Pop', 'Soul', 'R&B', 'MPB']
)

# verificar a classe do objeto m1
type(m1)

# endereço do objeto m1 na memória do computador
id(m1)
id(m2)
id(m3)

