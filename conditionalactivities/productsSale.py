maca = int(input("Digite a quantidade de maçãs: "))
banana = int(input("Digite a quantidade de bananas: "))

if maca > banana:
    print("Tem mais maçãs do que bananas.")
elif banana > maca:
    print("Tem mais bananas do que maçãs.")
else:
    print("Tem a mesma quantidade de maçãs e bananas.")