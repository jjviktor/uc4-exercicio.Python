#desconto em compra
#faça um algortimo para ler o valor total de uma compra e verifcar se ele é maior que 200. se for o algortimo deve subtrair 30 desse valor. no final, o algoritmo deve imprimr o resultado do valor a pagar.
valor_total = float(input("Digite o valor total da compra: "))
if valor_total > 200:
    valor_total -= 30
print(f"O valor a pagar é: R$ {valor_total:.2f}")