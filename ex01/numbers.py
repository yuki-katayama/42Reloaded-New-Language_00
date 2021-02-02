f = open("numbers.txt", "r")
data = f.readlines()
for value in data:
    value = value.strip(",\n")
    print(value)