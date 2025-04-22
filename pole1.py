pole = ["jedna","dva","tři","čtyři","pět","šest"]

delka = len(pole)
print(delka)

for i in pole:
    print(i)

dalsiPole = input("zadej dalsi pole: ")
pole.append(dalsiPole)

pole.sort()

pole.reverse()
print()