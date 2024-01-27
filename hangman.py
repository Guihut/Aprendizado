import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "inteligencia", "artificial", "dados"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    forca = [
        '''
           +---+
               |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    return forca[tentativas]

def jogar_forca():
    palavra = escolher_palavra().lower()
    letras_certas = ['_'] * len(palavra)
    tentativas = 0
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")

    while True:
        print(exibir_forca(tentativas))
        print("Palavra: " + " ".join(letras_certas))
        print("Letras erradas: " + " ".join(letras_erradas))

        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_certas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if palpite in palavra:
            for i in range(len(palavra)):
                if palavra[i] == palpite:
                    letras_certas[i] = palpite
        else:
            letras_erradas.append(palpite)
            tentativas += 1

        if "_" not in letras_certas:
            print("Parabéns! Você venceu. A palavra é:", palavra)
            break

        if tentativas == len(exibir_forca(0)) - 1:
            print(exibir_forca(tentativas))
            print("Você perdeu! A palavra correta era:", palavra)
            break

if __name__ == "__main__":
    jogar_forca()
