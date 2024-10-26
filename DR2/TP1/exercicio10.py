import random

def criar_historia():
    personagens = ["um gato", "um astronauta", "uma princesa", "um robô", "um dragão"]
    acoes = ["descobriu um segredo", "encontrou um mapa misterioso", "fez amizade com um alienígena", "participou de uma competição", "salvou o dia"]
    locais = ["em uma floresta mágica", "no espaço sideral", "em um castelo encantado", "em uma cidade futurista", "em uma ilha deserta"]

    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)

    historia = f"Era uma vez {personagem} que {acao} {local}."
    return historia

while True:
    print(criar_historia())
    criar_historia_novamente = input("Deseja criar outra história? (s/n) ").strip().lower()
    if criar_historia_novamente != "s":
        print("Obrigado por usar o programa! Até a próxima!")
        break