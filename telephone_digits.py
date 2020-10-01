# Goal: Create a function that creates character combinations from
# telephone numbers.
my_input = 69488

def find_telephone(number):
	# Define the letters and corresponding numbers
	letter_combinations = [['a','b','c'],['d','e','f'],['g','h','i'],
							['j','k','l'],['m','n','o'],['p','q','r','s'],
							['t','u','v'],['w','x','y','z']]
	number_combinations = list(range(2,10))

	# Put letters into a dictionary corresponding to the number
	letter_dict = {}
	for i in range(len(letter_combinations)):
		letter_dict[number_combinations[i]]=letter_combinations[i]

	# Take input and create possible letters for each number input
	input_str = str(number)
	possible_letters = [letter_dict[int(i)] for i in input_str]
	print('The possible letters for each digit are:')
	print(possible_letters)

	# Create possible combinations
	possible_combos = []
	import itertools
	possible_combos = list(itertools.product(*possible_letters))
	print('The possible combinations are: \n')
	print([list(possible_combo) for possible_combo in possible_combos])

find_telephone(my_input)
