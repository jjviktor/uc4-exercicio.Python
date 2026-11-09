#Aumento salarial
#faça um algoritmo para ler o salario de um funcionario e verificar se ele é menor  de 1500. se for, o algoritmo deve somar 200 a esse salario. No final, o algoritmo deve4 imprimir o resultado do valor final do salario.
salario = float(input("Digite o salário do funcionário: "))
if salario < 1500:
    salario += 200
print(f"O salário final é: R$ {salario:.2f}")