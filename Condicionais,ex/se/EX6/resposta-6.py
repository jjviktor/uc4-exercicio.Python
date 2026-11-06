#desconto em compras
#se a quantidade de maças compradas for menor que 12, cada uma custa R$ 1,30
#se a quantidade de maças compradas for maior ou igual a 12, cada uma custa R$ 1,00
quantidade = int(input("Digite a quantidade de maças compradas: "))
if quantidade < 12:
    preco_unitario = 1.30
else:
    preco_unitario = 1.00
preco_total = quantidade * preco_unitario
print(f"O preço total da compra é R$ {preco_total:.2f}.")