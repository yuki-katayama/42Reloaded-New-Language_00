def main():
    f = open("numbers.txt", "r")
    data = f.readlines()
    for value in data:
        value = value.strip(",\n")
        print(value)

if __name__ == "__main__":
    main()
