import datetime

while True:
    nome = input("Digite seu nome completo: ")
    ano_nascimento = input("Digite seu ano de nascimento (entre 1922 e 2021): ")
    try:
        ano_nascimento = int(ano_nascimento)
        if 1922 <= ano_nascimento <= 2021:
            break
        else:
            print("Ano inválido. Tente novamente.")
    except ValueError:
        print("Valor inválido. Tente novamente.")

idade = datetime.date.today().year - ano_nascimento

print(f"Olá {nome}, você tem {idade} anos.")
