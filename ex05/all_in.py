import sys


def make_dict(any_dict):
    rev_dict = {}
    for key, value in any_dict.items():
        rev_dict[value] = key
    return rev_dict

def shift_lower_key(any_dict):
    dict_lower_key= {}
    for key, value in any_dict.items():
        dict_lower_key[str.lower(key)] = value
    return dict_lower_key

def main():
    states = {
    	"Oregon": "OR",
	    "Alabama": "AL",
    	"New Jersey": "NJ",
	    "Colorado": "CO"
	}
    capital_cities = {
    	"OR": "Salem",
	    "AL": "Montgomery",
    	"NJ": "Trenton",
	    "CO": "Denver"
    }
    rev_states = make_dict(states)
    rev_cities = make_dict(capital_cities)
    rev_cities = shift_lower_key(rev_cities)
    states = shift_lower_key(states)
    input_value = sys.argv[1].split(",")
    input_value = [s.strip() for s in input_value if len(s) >= 2]
    input_value_lower = [str.lower(s) for s in input_value]
    for i, value in enumerate(input_value_lower):
        if(value in states):
            output_city = capital_cities[states[value]]
            output_state = rev_states[rev_cities[str.lower(output_city)]]
            print("{city} is the capital of {state}".format(city=output_city, state=output_state))
        elif(value in rev_cities):
            output_state = rev_states[rev_cities[value]]
            output_city = capital_cities[states[str.lower(output_state)]]
            print("{city} is the capital of {state}".format(city=output_city, state=output_state))
        else:
            print("{value} is neither a capital city nor a state".format(value = input_value[i]))

if __name__ == "__main__":
    main()
