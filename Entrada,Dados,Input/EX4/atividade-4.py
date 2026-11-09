#meta de pontuação
#Faça um algoritmo para ler a pontuação de um jogador e verificar se ela é maior ou igual  a 500. se for, o algoritmo deve somar 100 a essa pontuação. No final, o algoritmo deve imprimir o resultado da pontuação final.
pontuacao = float(input("Digite a pontuação do jogador: "))
if pontuacao >= 500:
    pontuacao += 100
print("A pontuação final do jogador é:", pontuacao)