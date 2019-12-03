class SomentePares(list):
    #aqui estamos sobreescrevendo o metodo append da classe list
    def append(self, inteiro):
        #isinstance testa se determina objeto é do tipo de determinada lasse
        #como vimos q em python tudo é um objeto, logo abaixo estamos verificando
        # se o objeto inteiro é uma instacia do tipo int que é uma classe.
        if not isinstance(inteiro, int):
            # a palavra raise lança uma exceção
            raise TypeError('Somente inteiros')
        if inteiro % 2:
            raise ValueError('Somente pares')
        #caso n caia em nem um dos ifs, chamamos o metodo append da classe
        #pai list.
        super().append(inteiro)

sp = SomentePares()
sp.append(2)# aqui n gera nem um erro, mas caso forneçamos
            # no parametro um número impar ou de ponto flutuante
            # irá gerar um erro.