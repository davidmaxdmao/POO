# criando mais de um construtor na classe com @classmethod

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    #construtor alternativo
    @classmethod
    def outro_consturtor(cls, nome):
        return cls(nome)

#aqui utiliza o primeiro construtor
p = Pessoa('marcos')
print(p.nome)
print('')
#aqui utiliza o construtor alternativo
p = Pessoa.outro_consturtor('pedro')
print(p.nome)