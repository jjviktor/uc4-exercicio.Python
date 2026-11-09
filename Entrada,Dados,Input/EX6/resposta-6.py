#taxa de processamento
#faça um algoritmo para ler o valor de uma transferencia bancaria e verificar se ele é maior que 1000. se for, o algoritmo deve somar 15 a esse valor. no final, o algoritmo deve imprimir o resultado do valor total a ser pago.
valores_transferencia = float(input("Digite o valor da transferência bancária: "))
if valores_transferencia > 1000:
    valores_transferencia += 15
print("O valor total a ser pago é:", valores_transferencia)