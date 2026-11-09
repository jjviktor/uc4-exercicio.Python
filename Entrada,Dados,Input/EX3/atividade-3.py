#verificação de temperatura
#Faça um algoritmo para ler a temperatura atual em C e verificar se ela é maior que 35 se for, o algoritmo deve somar 5 a essa temperatura. no final, o algoritmo deve imprimr o resultado da temperatura final.
temperatura = float(input("Digite a temperatura atual em Celsius: "))
if temperatura > 35:
    temperatura += 5
print(f" A temperatura final é: {temperatura:.1f}°C")