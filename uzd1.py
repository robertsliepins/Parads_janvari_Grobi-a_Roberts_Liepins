file_path = "uzd1.txt"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Failu nevar atrast.")
except IOError:
    print("Kļūda lasot failu.")

