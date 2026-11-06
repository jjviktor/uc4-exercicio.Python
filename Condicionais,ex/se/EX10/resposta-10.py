#saudação por turno
#Peça para o usuario digitar o turno em que estuda ou trabalha usando apenas uma letra: M (Matutino), V (Vespertino) ou N (Noturno).
turno = input("Digite o turno em que estuda ou trabalha (M/V/N): ").upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa Tarde")
elif turno == "N":
    print ("Boa Trade")
else:
    print("Turno inválido. Por favor, digite M, V ou N.")