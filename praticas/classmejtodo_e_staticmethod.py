#classmethod e staticmethod

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)

    @classmethod
    # Obs.: O cls faz referencia a propria classe.
    def de_string(cls, data_string): #recebe uma data neste formato: 01-05-2015

        # pega a data fornecida do parametro usa o map para aplicar uma função a
        #string tira os traços e bota cada elemento em dia mes e ano.
        dia, mes, ano = map(int, data_string.split('-'))
        # aqui é como se estivéssemos estanciando a própria classe com o cls
        data = cls(dia, mes, ano)
        return data

    # Um metodo statico, não tem referencia nem com a classe nem com o objeto é
    # simplesmente uma função dentro da classe, não pode ser herdada, nem sobreescrita.
    @staticmethod
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <=2020

# um metodo de classe(@classmethod) pode ser chamado tanto por um bojeto quanto pela
# propria classe. Pode ser herdado e sobreescrito.
data = Data(10, 10, 10)
Data.de_string('103-5-2')
# Um metodo statico pode ser chamado tanto pela propria classe
# quanto por um objeto, como vemos logo a baixo.
vdd = Data.is_date_valid('10-10-2016')
print(vdd)
vddd = data.is_date_valid('40-10-2016')
print(vddd)






