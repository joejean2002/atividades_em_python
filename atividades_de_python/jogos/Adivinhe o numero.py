numero_coringa = 37

tentativas_maximas = 5

print("Bem-vindo ao jogo Adivinhe o Número!")
print(f"O número oculto está entre 0 e 100. Você tem {tentativas_maximas} tentativas.")

for tent in range(1, tentativas_maximas + 1):
    # Solicite ao jogador que insira sua tentativa
    tentativa_jogador = int(input(f"Tentativa {tent}: Digite um número: "))

    if tentativa_jogador == numero_coringa:
        print(f"Parabéns! Você acertou. O número oculto era {numero_coringa}.")
        break
    elif tent < tentativas_maximas:
        if tentativa_jogador < numero_coringa:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
    else:
        print(f"Fim do jogo! O número oculto era {numero_coringa}. Game Over.")