# Prototipo-faculdade-zombie-dice

O projeto consiste em desenvolver o jogo zombie dice em uma versão simplifacada, na qual cada jogador joga uma rodada, utilizando principalmente variáveis e condicionais, ou seja, utilizando conceitos mais básicos do python

Regras do jogo
- O jogo possui 13 dados e esses dados ficam dentro de um tubo
- É preciso marcar os pontos de alguma maneira
- É necessário pelo menos dois jogadores

- 13 DADOS: cada um com 6 lados
  Dado Verde: 3 cérebros, 1 tiro, 2 passos
  Dado Vermelho: 1 cérebro, 3 tiros, 2 passos
  Dado Amarelo: 2 cérebros, 2 tiros, 2 passos

- TUBO: No tubo existem
  6 dados verdes
  4 dados amarelos
  3 dados vermelhos

- No seu turno agite o tubo e pegue 3 dados.
- Rolar os 3 dados e veja a face que ficou para cima
    - Cérebro - separe um dado e ganhe um ponto
    - Espingarda - Sua vitma revidou, menos uma vida (total 3 vidas no turno)
    - Pegadas - Manter o dado na mão (REGRA NÃO IMPLEMENTADA)
    - O jogador precisa rodar sempre pelo menos 3 dados, caso o tubo fique vazio, anote a quantidade de cérebros,
e coloque os dados de volta na tubo, exceto os que tiverem a face espingarda para cima. (REGRA NÃO IMPLEMENTADA)

    - se em qualquer momento do jogo tiver 3 espignardas viradas para cima, seu turno acabou e você perde todos os
pontos (cérebros) coletados durante o turno.
    - Caso contrário, você pode optar por parar e marcar pontos(1 cérebro = 1 ponto), ou, continuar a jogar

    - Se escolher continuar: 
        - você não devolve os dados ao tubo (REGRA NÃO IMPLEMENTADA)
        - você sempre rola três por vez
        - primeiro pega os dados que tem a face PEGADAS virada para cima depois completa os dados na mão se necessário
        - depois de pegar nove dados você não pode decidir não jogar (REGRA NÃO IMPLEMENTADA)

    - Jogue até alguem fazer 13 pontos, termine a rodada, todos devem jogar o mesmo número de rodadas, quem tiver mais
     cérebros, é o vencedor (REGRA NÃO IMPLEMENTADA)
