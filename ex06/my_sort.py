def BubbleSort(num):
    for i in range(len(num)):
        for j in range(len(num)-1, i, -1):
            if int(num[j][1]) < int(num[j-1][1]):
                num[j], num[j-1] = num[j-1], num[j]
    return num

def main():
	d = {
	'Hendrix':'1942',
	'Allman':'1946',
	'King':'1925',
	'Clapton':'1945',
	'Johnson':'1911',
	'Berry':'1926',
	'Vaughan':'1954',
	'Cooder':'1947',
	'Page':'1944',
	'Richards':'1943',
	'Hammett':'1962',
	'Cobain':'1967',
	'Garcia':'1942',
	'Beck':'1944',
	'Santana':'1947',
	'Ramone':'1948',
	'White':'1975',
	'Frusciante':'1970',
	'Thompson':'1949',
	'Burton':'1939',
	}

	score_sorted = sorted(d.items(), key=lambda x:x[0])
	BubbleSort(score_sorted)
	for s in score_sorted:
	    print(s[0])

if __name__ == '__main__':
    main()