import sys

def main():
    states = {
    	"Oregon" : "OR",
	    "Alabama" : "AL",
    	"New Jersey": "NJ",
	    "Colorado" : "CO"
	}
    capital_cities = {
    	"OR": "Salem",
	    "AL": "Montgomery",
    	"NJ": "Trenton",
	    "CO": "Denver"
    }

    if(len(sys.argv) != 2):
        sys.exit()
    try:
        output = capital_cities[states[sys.argv[1]]]
    except KeyError:
        output = "Unknown state"
    except:
        output = "Unknown state"
    print(output)

if __name__ == "__main__":
    main()