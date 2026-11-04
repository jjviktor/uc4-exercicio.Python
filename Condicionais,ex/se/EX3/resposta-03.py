ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2026 - ano_nascimento
print("Sua idade em 2026 será:", idade)
if idade >= 16:
    print("Você poderá votar em 2026.")
else:
    print("Você não poderá votar em 2026.")