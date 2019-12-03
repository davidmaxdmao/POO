# Quando obtemos um erro ou exceção o cigo vai para, no entanto
# se tratarmos esse erro/execeção o codigo vai executar uma ação
# ao se deparar com o erro e em seguida vai proseguir no seu funcionamento.
# Podemos fazer isso por meio do try e excepet.

# # Primeiro exemplo
# def algo():
#     raise Exception('exececao')
#     print('depois do raise')
#
# def algo2():
#     try:
#         algo()
#     except:
#         print('Eu peguei uma excecao')
#         print('executado apos a excecao')
#
# algo2()
# print('')
# #desta forma demonstrada acima iremos executar o que estiver
# #dentro do bloco except para qualquer erro que ocorra. Agora vmaos
# #ver como fazer isso para um erro especifico.
#
# #Neste caso iremos lançar uma exceção caso tente dividir um
# #número por zero, o que geraria um erro.
# def divisao(divisor):
#     try:
#         return 10 / divisor
#     except ZeroDivisionError:
#         return 'divisao por zero'
#
# a = divisao(0)
# print(a) # vai printar na tela: divisao por zero
# print('')
#
# #exemplo 3, agora vamos adicionar mais uma exceção, para se
# #o tipo do valor estiver errado.
#
# def divisao2(divisor):
#     try:
#         return 10 / divisor
#     except (ZeroDivisionError, TypeError):
#         return 'Entre com um número, e diferente de 0'
#
# a = divisao2('asdf')
# print(a)
# print('')
#
# #exemplo 4, agora não quero permitir um numero especifico e tratar o erro.
# def divisao3(divisor):
#     try:
#         if divisor == 13:
#             raise ValueError('13 não é legal')
#         return 10 / divisor
#     except (ZeroDivisionError, TypeError):
#         return 'Entre com um número, e diferente de 0'
#
# a = divisao3(13)
# print(a)
# print('')

#exemplo 4 tornando o codigo acima melhor
def divisao4(divisor):
    try:
        if divisor == 13:
            raise ValueError('13 não é legal')
        #return 10 / divisor
    except ZeroDivisionError:
        return 'Divisao por zero'
    except TypeError:
        return 'Entre um valor numerico'
    except ValueError:
        print('Nao utilize o numero 13')
        raise
    #podemos utilizar o else quando queremos fazer algo quando n ocorrer nem uma exceção
    # para que esse else funcione foi comentado o retorno que existe dentro do if
    else:
        print('n ocorreu nem uma exceção')
    #com o finally podemos definir algo que sempre vai ser executado
    #também podemos colocar retornos dentro do finally.
    finally:
        print('sempre vai executar')

b = divisao4(2)
print(b)


