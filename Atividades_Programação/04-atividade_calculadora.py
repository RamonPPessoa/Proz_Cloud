def calculadora():
    while True:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = int(input("Digite o número para realizar a operação : "))

        if opcao == 0:
            break
        elif opcao < 1 or opcao > 4:
            print("Essa opção não existe")
            continue

        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        if opcao == 1:
            resultado = num1 + num2
            print(f"O resultado da soma é {resultado}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"O resultado da subtração é {resultado}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"O resultado da multiplicação é {resultado}")
        elif opcao == 4:
            if num2 == 0:
                print("Não é possível dividir por zero")
                continue
            resultado = num1 / num2
            print(f"O resultado da divisão é {resultado}")

calculadora()