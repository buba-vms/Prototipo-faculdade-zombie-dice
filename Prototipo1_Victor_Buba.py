import random

print("(¬x_x)¬ ( ¬º-°)¬ (¬x_x)¬ [¬º-°]¬ (¬x_x)¬ヽ(ﾟДﾟ)ﾉ ヽ(ﾟДﾟ) \n")
print("Vocês foram infectados!!! Bem Vindos ao Zombie Dice!!!\n")
print("(¬x_x)¬ ( ¬º-°)¬ (¬x_x)¬ [¬º-°]¬ (¬x_x)¬ヽ(ﾟДﾟ)ﾉ ヽ(ﾟДﾟ) \n")

print("----------REGRAS DO jOGO----------")
print("\nVence o primeiro que comer 13 cérebros, ou então, quem comer mais cérebros!!! Caso tome 3 tiros você perde seu turno e seus pontos!!!\n")


# nessa seção foi criada as variáveis de número de jogadores, lista de jogadores e os nomes que preenchem essa lista.
n_players = 0
players_list = []

while (n_players < 2):
    n_players = int(input("Digite quantas pessoas foram infectadas: "))
    if n_players < 2:
        print("\nÉ necessário digitar um número interi e ter pelo menos 2 zombies para iniciar!!!")

for i in range(n_players):
    name = str(input(f"Digite o nome do Infecatado Nº{i+1}: ").title())
    players_list.append(name)

print("\n" + "(¬x_x)¬ ( ¬º-°)¬ (¬x_x)¬ ヽ(ﾟДﾟ)ﾉ [¬º-°]¬ (¬x_x)¬ [¬º-°]¬ ヽ(ﾟДﾟ)ﾉ \n")
print("Tudo Cérebros, Bora começar\n""")


# Criação dos dados e do tubo:
dado_verde = "CCCEPP"
dado_vermelho = "CEEEPP"
dado_amarelo = "CCEEPP"

tubo = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo, dado_vermelho, dado_vermelho, dado_vermelho]

# Criação das variáveis da rodada

dados_na_mao = []
turno_do_jogador = 0
cerebros = 0
espingardas = 0
passos = 0

# Modelo do turno unico
while True:
    print(f"Turno do jogador {players_list[turno_do_jogador]}\n")
    print("(¬x_x)¬ ( ¬º-°)¬ (¬x_x)¬ [¬º-°]¬ (¬x_x)¬ヽ(ﾟДﾟ)ﾉ ヽ(ﾟДﾟ) \n")

    for i in range(3):
        dado_sorteado = random.randint(0,12)
        dados_na_mao.append(tubo[dado_sorteado])

    # Sorteio dos dados na mão e mostra para o úsuario os dados selecionados

    msg_cordosdados = []

    for i in dados_na_mao:
        if i == "CCCEPP":
            msg_cordosdados.append('Dado Verde')
        elif i == "CEEEPP":
            msg_cordosdados.append('Dado Vermelho')
        else:
            msg_cordosdados.append('Dado Amarelo')

    print(f"Você possui na sua mão um {msg_cordosdados[0]}, um {msg_cordosdados[1]} e um {msg_cordosdados[2]}")

    #Jogador joga os dados e vizualiza as faces que tirou:
    input("Digite sua palavra da sorte para jogar os dados: \n")

    lados_sorteados = []
    for i in range(3):
        lado_sorteado = random.choice(dados_na_mao[i])
        lados_sorteados.append(lado_sorteado)
    for i in lados_sorteados:
        if i == "C":
            cerebros += 1
        elif i == "E":
            espingardas += 1
        else:
            passos += 1

    print(f"O(A) Jogador(a) {players_list[turno_do_jogador]}, comeu {cerebros} Cérebro(s), tomou {espingardas} tiro(s) e teve {passos} vítima(s) escapando\n")

    continuar = str(input("Você deseja jogar outro turno? Digite 'S' para sim e 'N' para passar a vez: \n")).strip().upper()
    if continuar == "N":
        turno_do_jogador += 1
        dados_na_mao = []
        espingardas = 0
        cerebros = 0
        passos = 0
        if turno_do_jogador == len(players_list):
            print("Jogo encerrado!!!")
            break
        else:
            print("Iniciando mais uma rodada do jogador atual\n")
            dados_na_mao = []



