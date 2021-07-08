"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

def _definir_metade(string):
    tamanho = len(string)
    metade = divmod(tamanho, 2)
    result = ""
    primeira_metade = ""
    segunda_metade = ""
    if metade[1] == 1:
        partes = metade[0] + 1
        primeira_metade = string[:partes]
        segunda_metade = string[partes:]
        result = (primeira_metade, segunda_metade)
        return result
    else:
        partes = metade[0]
        primeira_metade = string[0:partes]
        segunda_metade = string[partes:]
        result = (primeira_metade, segunda_metade)

    return result


def _misturar_strings(a,b):
    frase = f"{a[0]}{b[0]}{a[1]}{b[1]}"
    return frase

def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    result_a = _definir_metade(a)
    result_b = _definir_metade(b)
    return _misturar_strings(result_a, result_b)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
