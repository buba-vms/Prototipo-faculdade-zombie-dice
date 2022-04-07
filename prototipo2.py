import random
from random import shuffle


# Função para criar jogadores:

def criar_jogadores():
    players_list = []
    n_players = 0
    while n_players < 2:
        try:
            n_players = int(input("Digite quantas pessoas foram infectadas: "))
            if n_players < 2:
                print("É necessário digitar um número interio e ter pelo menos 2 zombies para iniciar!!!")
        except ValueError:
            print("!!!Só é permitido digitar números inteiros!!!")

    for i in range(n_players):
        name = str(input(f"Digite o nome do Infectado Nº{i + 1}: ").title())
        players_list.append(name)
    # Ordem aleatória de jogadores
    shuffle(players_list)
    print("Ordem de jogadores aleatórios")
    for i, player in enumerate(players_list):
        print(f"{i + 1}ª {player}")

    return players_list


# Criação dos Dados e o copo, embaralaha os dados dentro do copo

def enxer_copo():
    copo = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_amarelo, dado_amarelo,
            dado_amarelo, dado_amarelo, dado_vermelho, dado_vermelho, dado_vermelho]

    shuffle(copo)

    return copo


# Pegar os dados na mão e informa ao usuario quais cores dos dados pegos

def pegar_dados(copo):
    dados_na_mao = []
    while len(dados_na_mao) < 3:
        if len(dados_na_mao) + len(copo) >= 3:
            dados_na_mao.append(copo.pop())
        else:
            copo = enxer_copo()
            print("O jogador colocou todos os dados no copo")
    cor_dado = [cor for dado in dados_na_mao for cor in dado.keys()]
    print(f"{'-' * 50}\nOs dados na mão do jogador {jogador} são:\n\n{cor_dado[0]},\n{cor_dado[1]},\n{cor_dado[2]}\n\n{'-' * 50}")
    return dados_na_mao, copo


# joga os dados e fala para o usuario os lados que ele tirou

def jogar_dados():
    lados_sorteados = [dado[face][random.randint(0, 5)] for dado in dados_na_mao for face in dado]

    print(f"\nO jogador obteve as seguintes faces dos dados: \n{'-' * 50}")
    for i in lados_sorteados:
        if i == 'C':
            print('Você comeu o Cérebro da sua vítima')
        elif i == 'E':
            print('Você tomou um tiro, sua vitma se defendeu')
        else:
            print('Sua Vitima conseguiu correr, e continua correndo')
    print('-' * 50)
    return lados_sorteados


# Função que contabiliza os pontos

def pontuar(lados_sorteados):
    for lado in lados_sorteados:
        if lado == 'C':
            score_atual['Cérebros'] += 1
        elif lado == 'E':
            score_atual['Tiros'] += 1
        else:
            score_atual['Passos'] += 1
    print(score_atual)
    return score_atual


# Devolver dados no copo ou mante-lôs na mão

def devolver_dados(lados_sorteados, dados_na_mao):
    for i in range(2, -1, -1):
        if lados_sorteados[i] != 'P':
            dados_na_mao.pop(i)
    cor_dado = [cor for dado in dados_na_mao for cor in dado.keys()]
    print(f"{'-' * 50}\nO jogador permance com {len(dados_na_mao)} dados na mão: \n\n{[i for i in cor_dado]}\n")
    return dados_na_mao


# Criação dos Dados
dado_verde = {'Dado Verde': ('C', 'C', 'C', 'E', 'P', 'P')}
dado_vermelho = {'Dado Vermelho': ('C', 'E', 'E', 'E', 'P', 'P')}
dado_amarelo = {'Dado Amarelo': ('C', 'C', 'E', 'E', 'P', 'P')}

# Jogo
jogadores = criar_jogadores()
copo = enxer_copo()
game_over = False

ponto_total = [{jogador: 0} for jogador in jogadores]

while not game_over:
    for i, jogador in enumerate(jogadores):
        print(f"\nA pontuaço total no momento é:\n{ponto_total}\n")
        print(f"{'-' * 50}\nVez do jogador {jogador}\n{'-' * 50}")
        score_atual = {'Cérebros': 0, 'Tiros': 0, 'Passos': 0}
        copo = enxer_copo()
        while True:

            if ponto_total[i][jogador] >= 13:
                game_over = True
                break

            else:
                input(f"\n{jogador}, Enter para pegar os dados do copo")
                dados_na_mao, copo = pegar_dados(copo)

                input(f'\n{jogador}, Enter para jogar os dados')
                lados_sorteados = jogar_dados()

                score_atual = pontuar(lados_sorteados)
                devolver_dados(lados_sorteados, dados_na_mao)

                if score_atual['Tiros'] >= 3:
                    print(f"\n{jogador} tomou 3 tiros e perdeu todos os pontos da rodada\n\n")

                    break

                elif score_atual['Cérebros'] + ponto_total[i][jogador] >= 13:
                    ponto_total[i][jogador] += score_atual['Cérebros']
                    print(
                        f"\nO Jogador {jogador} possui pontos o suficiente para ganhar\nRodada de {jogador} Encerrada!!!\n")
                    game_over = True
                    break
                else:
                    continuar = input(f"Aperte Enter para continuar, Digite N para armazenar seus pontos? (y/n)").casefold().strip()

                if continuar == 'n':
                    ponto_total[i][jogador] += score_atual['Cérebros']
                    break

print(ponto_total)
