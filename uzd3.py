with open("uzd3.txt", "r", encoding="utf-8") as f:
    rinda = f.readlines()
    if len(rinda) >= 3:
        print(rinda[2])
    else:
        print("Teksta failā nav tik daudz rindu.")