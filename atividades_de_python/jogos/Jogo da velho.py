#Jogo da Velha
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)


def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == ' ':
                return False
    return True


def main():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    turno = 0

    print("Bem-vindo ao Jogo da Velha!")

    while True:
        imprimir_tabuleiro(tabuleiro)
        jogador = jogadores[turno % 2]
        print(f"Vez do jogador {jogador}")

        while True:
            linha = int(input("Informe o número da linha (0, 1 ou 2): "))
            coluna = int(input("Informe o número da coluna (0, 1 ou 2): "))

            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador
                break
            else:
                print("Essa posição já está ocupada. Tente novamente.")

        if verificar_vencedor(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador} venceu!")
            break
        elif tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        turno += 1


if __name__ == "__main__":
    main()