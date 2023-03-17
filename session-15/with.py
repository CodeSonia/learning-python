pythonistas = ["Rosa", "Sonia", "Alex", "Gray"]

with open("pythonistas.txt", "w") as file:
    for pythonista in pythonistas:
        file.write(pythonista)
        file.write("\n")

with open("pythonistas.txt", "r") as file:
    print(file.readlines())
