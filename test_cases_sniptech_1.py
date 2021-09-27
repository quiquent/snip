#test case (txt file lines)

lines = open('example_input.txt', 'r').read().splitlines()
input(lines)

#-> unit test, first line should be integer > 0
#-> second line should be length > 1 AND first digit equal the number of digits after AND number of digits after all >0 AND <= 4
#-> for each line if len(lines[i])==1 then next lines[i+1] should be length > 1 AND first digit equal the number of digits after AND number of digits after all >0 AND <= 4
#-> last line lines[-1] should be 0

def maxProfit(nb_tree_trunks, lenghts_tree_trunks):

	profits = {
		1: -1,
		2: 3,
		3: 1
	}

	cumulative_profit = 0
	
	counter = 0
	cuts = []

	#initialize last cut
	last_cut = 0

	for i in lenghts_tree_trunks:

		if i == 1:

			cumulative_profit += profits[i]

		if i == 2:

			cumulative_profit += profits[i]

		if i == 3:

			#can cut in 2 
			if last_cut == 3 or last_cut == 4:

				cumulative_profit += profits[2]

			else:

				cumulative_profit += profits[i]

		if i == 4:


			if last_cut == 3 or last_cut == 4:

				cumulative_profit += 2 * profits[2]

		#remember last cut
		last_cut = i

	print(f'Max profit: {cumulative_profit}')

	return cumulative_profit

i = 0
total_profit = 0

while True:

	if len(lines[i]) == 1:

		if int(lines[i]) == 0:
			
			break

	#print(f'lines[i]: {lines[i]}')

	if len(lines[i]) == 1:

		nb_sawmills = lines[i]
		print(f'Case {nb_sawmills}')

	else:

		nb_tree_trunks = lines[i].split()[0]
		lenghts_tree_trunks = [int(i) for i in lines[i].split()[1:]]

		input(f'lenghts_tree_trunks: {lenghts_tree_trunks}')

		total_profit += maxProfit(nb_tree_trunks, lenghts_tree_trunks)

		print(f'total_profit: {total_profit}')

	i += 1

print(f'Process finished with total_profit: {total_profit}')
