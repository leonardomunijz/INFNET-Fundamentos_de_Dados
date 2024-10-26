def combinar_nomes():
    nome1 = input("Digite um primeiro nome: ").strip()
    nome2 = input("Digite um segundo nome: ").strip()

    novo_nome1 = nome1[:len(nome1) // 2] + nome2[len(nome2) // 2:]
    novo_nome2 = nome2[:len(nome2) // 2] + nome1[len(nome1) // 2:]

    print(f"O novo primeiro nome é: {novo_nome1}")
    print(f"O novo segundo nome é: {novo_nome2}")

combinar_nomes()