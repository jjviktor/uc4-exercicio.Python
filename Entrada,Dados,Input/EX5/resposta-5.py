#ajuste de estoque
#Faça um algoritmo para ler a quantidade de um produto em estoque e verificar se ela é menor que 20. se for, o algoritmo deve somar 50 a essa quantidade. No final, o algoritmo deve imprimir o resultado da quantidade atualizada do estoque
quantidade_estoque = int(input("Digite a quantidade do produto em estoque: "))
if quantidade_estoque < 20:
    quantidade_estoque += 50
print("A quantidade atualizada do estoque é:", quantidade_estoque)