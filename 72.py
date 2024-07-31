class Biblioteca:
    def __init__(self, livro1, **kwargs):
        self.livro1 = livro1
    
prat1 = Biblioteca('1984')
prat1.livro2 = 'Diário de um banana 1'
prat1.livro3 = 'Diário de um banana 2'
prat1.livro4 = 'Diário de um banana 3'
prat1.livro5 = 'Diário de um banana 4'


print(prat1.livro1)