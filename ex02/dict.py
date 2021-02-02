def main():
    data = [['Caleb' , 24],
            ['Calixte' , 84],
            ['Calliste', 65],
			['Calvin' , 12],
			['Cameron' , 54],
			['Camil' , 32],
			['Camille' , 5],
			['Can' , 52],
			['Caner' , 56],
			['Cantin' , 4],
			['Carl' , 1],
			['Carlito' , 23],
			['Carlo' , 19],
			['Carlos' , 26],
			['Carter' , 54],
			['Casey' , 2]]
    output = {}

    for value in data:
        output[value[1]] = value[0]
    for k, v in output.items():
        print("{key} : {value}".format(key = k, value = v))

if __name__ == "__main__":
    main()