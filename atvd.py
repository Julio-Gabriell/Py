preco = float(input("Digite o preço da sua compra: "))
opcao = int(input("Qual foi a opcao de pagamento - 1 Débito, 2 Credito, 3 Parcelado, 4 PIX "))

match opcao:
    case 1: 
        print(f"Como crédito ficara {preco}")
    case 2: 
        print(f"Como débito ficara {preco}")
    case 3: 
        vezes = int(input("Quantas vezes voce vai parcelar? "))
        if vezes <= 3:
            print(f"Como parcelado até em 3 ficara {preco}")
        elif vezes <= 7:
            print(f"Como parcelado até em 7 ficara {preco * 0.05 + preco}")
        elif vezes > 7:
            print(f"Como parcelado até em mais de 7 ficara {preco * 0.1 + preco}")

    case 4: 
        print(f"Como pix ficara {preco - preco * 0.05}")
    case _: 
        print("Essa opção não existe") 