def categoria_habilitacao(rodas, peso_bruto, qtd_pessoas):  # Definindo e criando uma função
    if rodas == 2 or rodas == 3:
        return "Categoria A"
    elif rodas == 4 and peso_bruto <= 3500 and qtd_pessoas <= 8:
        return "Categoria B"
    elif rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
        return "Categoria C"
    elif rodas >= 4 and qtd_pessoas > 8:
        return "Categoria D"
    elif rodas >= 4 and peso_bruto > 6000:
        return "Categoria E"
    else:
        return "Veículo não identificado"

rodas = int(input("Digite a quantidade de rodas do veículo: "))  # Criando os inputs
peso_bruto = float(input("Digite o peso bruto do veículo em quilogramas: "))
qtd_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

print("A categoria de habilitação para o veículo informado é:", categoria_habilitacao(rodas, peso_bruto, qtd_pessoas))
