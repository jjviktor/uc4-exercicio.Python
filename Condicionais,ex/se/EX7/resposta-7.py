#sistema de triagem de hospital
#Peça para o usuario digitar a cor da pulseira de triagem recebida pelo paciente no hospital.
cor_pulseira = input("Digite a cor da pulseira de triagem: ").lower()

if cor_pulseira == "vermelho":
    print("Atendimento Maximo.")
elif cor_pulseira == "amarelo":
    print("Paciente com prioridade média.")
elif cor_pulseira == "verde":
    print("Paciente com prioridade baixa.")
else:
    print("Cor de pulseira inválida.")  