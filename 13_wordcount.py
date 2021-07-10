"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
import re
import collections



# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).

def clean_data(filename):
    words = []
    arquivo = open(filename, "r")
    bag_words = []
    lines = arquivo.readlines()
    arquivo.close()


    for line in lines:
        string = re.sub(r"\s+", "", line.lower())
        words.append(string)

    for w in words:
        tamanho = len(w)
        i = 0
        while i < tamanho:
            bag_words.append(w[i])
            i += 1
        i = 0
    return bag_words


def dict_words(words):

    unicas = set(words)
    dicionario = dict.fromkeys(unicas, 0)

    for i in unicas:
        count = words.count(i)
        dicionario[i] = count

    return dicionario


def print_words(filename):
    bag_words = clean_data(filename)
    dicionario = dict_words(bag_words)

    dict_sorted = dict(sorted(dicionario.items(), key=lambda item: item[1]))
    for k, v in dict_sorted.items():
        print(k, v)
    '''
    
    for item in sorted(dicionario, key=dicionario.get):
        print(item, dicionario[item])
    '''


def print_top(filename):
    bag_words = clean_data(filename)
    dicionario = dict_words(bag_words)

    dict_sorted = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
    for k, v in dict_sorted.items():
        print(k, v)




# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
