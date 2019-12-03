#Criando uma instancia sem chamar init

class Pessoa:
    #aqui utilizamos o init normalmente
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#aqui iniciamos a classe com o new, depois precisamos fornecer
#os valores com esse dicionário, diferente de quando fazemos com o init
#que ja fornecemos os valores no parametro na hora que ciramos o objeto.
p = Pessoa.__new__(Pessoa)
dados = {'nome':'marcos', 'idade':28}
for key, value in dados.items():
    setattr(p, key, value)
print(p.nome, p.idade)