try:
    vards = input("Lūdzu ievadiet savu vārdu: ")
    with open("uzd5.txt", "w") as file:
        file.write(vards)
    print("Vārds ierakstīts failā.")
