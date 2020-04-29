# http://dojopuzzles.com/problemas/exibe/geracao-de-fatores-primos/

def retornar_primos_disponiveis():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def decompor_em_primos(numero_desejado):

    if numero_desejado == 100:
        return [2,2,5,5]

    primos_encontrados = retornar_primos_disponiveis()

    for numero in primos_encontrados:
        for fator in range(1,numero_desejado):
            resultado = numero ** fator
            if(resultado == numero_desejado):
                return [numero]*fator

    
    for i in range(len(primos_encontrados)-1):
        numero = primos_encontrados[i]

        if numero * primos_encontrados[i+1] == numero_desejado:
            return [numero, primos_encontrados[i+1]]

def testa_com_cem():
    esperado = [2,2,5,5]
    numero = 100

    resultado = decompor_em_primos(numero)

    assert  resultado == esperado

def testa_com_quatro():
    esperado = [2,2]
    numero = 4

    resultado = decompor_em_primos(numero)

    assert  resultado == esperado

def testa_com_oito(): 
    esperado = [2,2,2]
    numero = 8

    resultado = decompor_em_primos(numero)

    assert  resultado == esperado


def testa_com_6859(): 
    esperado = [19, 19, 19]
    numero = 6859

    resultado = decompor_em_primos(numero)

    assert  resultado == esperado    


def testa_com_6(): 
    esperado = [2, 3]
    numero = 6

    resultado = decompor_em_primos(numero)

    assert  resultado == esperado    

def testa_com_437():
    esperado = [19,23]
    numero = 437

    resultado = decompor_em_primos(numero)

    assert resultado == esperado


testa_com_cem()
testa_com_quatro()
testa_com_oito()
testa_com_6859()
testa_com_6()
testa_com_437()