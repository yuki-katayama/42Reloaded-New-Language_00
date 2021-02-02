import sys

def make_dict(any_dict):
    rev_dict = {}
    for key, value in any_dict.items():
        rev_dict[value] = key
    return rev_dict

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

    rev_states = make_dict(states)
    rev_cities = make_dict(capital_cities)

    if(len(sys.argv) != 2):
        sys.exit()
    try:
        output = rev_states[rev_cities[sys.argv[1]]]
    except KeyError:
        output = "Unknown capital city"
    except:
        output = "Unknown capital city"
    print(output)

if __name__ == "__main__":
    main()