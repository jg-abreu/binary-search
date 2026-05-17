def pesquisa_binaria_interativa():

    tamanho = int(input("Digite o tamanho da lista: "))
    item_procurado = int(input("Qual número deseja encontrar? "))

    lista = list(range(tamanho))

    baixo = 0
    alto = len(lista) - 1
    tentativas = 0

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item_procurado:
            print(f"\n✅ Sucesso! Encontrei o número {item_procurado}.")
            print(f"📍 Posição na lista (índice): {meio}")
            print(f"🔢 Total de tentativas: {tentativas}")
            return

        if chute > item_procurado:
            alto = meio - 1
        else:
            baixo = meio + 1

    print(f"\n❌ O número {item_procurado} não foi encontrado na lista.")
    print(f"🔢 Total de tentativas realizadas: {tentativas}")

pesquisa_binaria_interativa()