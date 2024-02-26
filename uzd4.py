import os
file_name = input("Ievadiet faila nosaukumu: ")
file_extension = input("Ievadiet faila formātu: ")

try:
    with open(file_name + '.' + file_extension, "r", encoding="utf-8") as file:
        file_content = file.read()
        print("Faila saturs:")
        print(file_content)
except FileNotFoundError:
    print("Kļūda: fails nav atrasts!")
except PermissionError:
    print("Kļūda: piekļuve failam ir liegta!")
except IOError:
    print("Kļūda: neparedzēta ievades/izvades kļūda!")