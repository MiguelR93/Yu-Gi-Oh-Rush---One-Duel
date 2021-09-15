import random, os
player  = [
    [], # 0 deck
    [], # 1 GY
    [], # 2 left s/t zone
    [], # 3 center s/t zone
    [], # 4 right s/t zone
    [], # 5 left monster zone
    [], # 6 center monster zone
    [], # 7 right monster zone
    [], # 8 extra deck
    [], # 9 field spell card zone
    [], # 10 hand
    [], # 11 banish zone
    [], # 12 show to your oponent from hand/deck
    [], # 13 side deck
    8000, # 14 LP
]




def openDeck():
    with open("./deck.txt", "r", encoding="utf-8") as card:
        for i in card:
            player[0].append(i[:len(i) - 1])
    print("\n\n\nterminamos")
    print(player[0])
    random.shuffle(player[0])
    print(f"\n\n\n\n\n{player[0]}")


def drawing():
    if len(player[10]) < 5:
        while len(player[10]) < 5:
            player[10].append(player[0][0])
            player[0].remove(player[0][0])
    elif len(player[10]) >= 5:
        player[10].append(player[0][0])
        player[0].remove(player[0][0])
    print(f"\n\n\n\nHand: {player[10]}")
    print(f"\n\n\n\nDeck: {player[0]}")




def run():
    os.system("clear")
    openDeck()
    print(f"\n\n\nFirst turn -----------------")
    drawing()
    print(f"\n\n\nNext turn -----------------")
    drawing()


if __name__ == "__main__":
    run()