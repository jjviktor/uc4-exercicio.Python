#Placar do jogo de futebol
#Peça para o usuario dgitar a quantidade de gols que o time A e o time B marcaram em uma partida.
gols_time_a = int(input("Digite a quantidade de gols do time A: "))
gols_time_b = int(input("Digite a quantidade de gols do time B: "))
if gols_time_a > gols_time_b:
    print("O time A venceu a partida!")
elif gols_time_b > gols_time_a:
    print("O time B venceu a partida!")
else:
    print("A partida terminou empatada!")   