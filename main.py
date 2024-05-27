# crie um programa que tenha 
'''
Crie um programa que tenha as opções:
 - Inserir pessoa na lista
 - Listar pessoas cadastradas
 - Pesquisar pelo nome de uma pessoa
 - Ordenar a lista por ordem alfabética
 - Atualizar nome
 - Deletar nome da lista
 - Sair do programa

Ao terminar, crie um repositório local e um remoto, e envie o link do repositório do GitHub.
'''

#lista de pessoas
pessoas_lista = ['Jaiane', 'Gabi', 'Maria', 'Pai', 'Mãe', 'Matheus', 'Vitinho', 'Marcia']
#insira uma pessoa na lista
while True:
    pessoas = input('insira uma pessoa na lista: ')
    if pessoas_lista != '':
        pessoas.append(pessoas)
        continue
#listar pessoas cadastradas
    print(pessoas_lista)
#pesquisar uma pessoa na lista
    pessoas = input('informe o nome que deseja pesquisar na lista: ')
#ordenar lista por ordem alfabética
    pessoas_lista.sort()
    for pessoas in pessoas_lista:
        print(pessoas)
#atualizar nome de pessoas da lista
    pessoa_a_atualizar = ('informe a pessoa que deseja atualizar: ')
    pessoas_lista[pessoas_lista.index(pessoa_a_atualizar)] = input('Informe o novo nome: ')
    for pessoas in pessoas_lista:
        print(pessoas)
#deletar pessoa da lista
    posicao = int(input('Informe a posicao da pessoa que deseja deletar (de 1 a 8): '))posicao -= 1
    try
            del(pessoas_lista[posição])
    except:
        print('Não foi possível deletar.')
        for pessoas in pessoas_lista:
            print(pessoas)
# tenta deletar o item na posição informada
        try:
        del(pessoas_lista[posicao])
        except:
        print('Não foi possível deletar.')
# exibe a nova lista
        for pessoa in pessoas_lista:
            print(pessoas)
#sair do programa
        break