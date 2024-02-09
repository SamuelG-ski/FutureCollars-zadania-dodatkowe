print("\nCiąg Collatza\n")

x = int(input("Podaj liczbę od 1 do 100: "))

if 1 <= x <= 100:
    print("\nCiąg Collatza dla liczby", x, "to:\n")
    print(x, end=" ")
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        print(x, end=" ")
else:
    print("\nLiczba powinna być z przedziału od 1 do 100!")