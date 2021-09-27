def openInput(file_name):

	f = open(file_name, 'r')
	lines = f.read().splitlines()
	f.close()

	return lines

def maxProfit(lenghts_tree_trunks):

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

	return cumulative_profit

def printOrder(lenghts_tree_trunks):

	possible_orders = []

	if len(lenghts_tree_trunks) == 1:

		possible_orders.append(lenghts_tree_trunks) 

	if len(lenghts_tree_trunks) == 2:

		list1 = lenghts_tree_trunks
		list2 = [lenghts_tree_trunks[1], lenghts_tree_trunks[0]]
		possible_orders.append(list1)
		possible_orders.append(list2)

	if len(lenghts_tree_trunks) == 3:

		list1 = lenghts_tree_trunks
		list2 = [lenghts_tree_trunks[1], lenghts_tree_trunks[2], lenghts_tree_trunks[0]]
		list3 = [lenghts_tree_trunks[2], lenghts_tree_trunks[0], lenghts_tree_trunks[1]]
		possible_orders.append(list1)
		possible_orders.append(list2)
		possible_orders.append(list3)

	if len(lenghts_tree_trunks) == 4:

		list1 = lenghts_tree_trunks
		list2 = [lenghts_tree_trunks[1], lenghts_tree_trunks[2], lenghts_tree_trunks[3], lenghts_tree_trunks[0]]
		list3 = [lenghts_tree_trunks[2], lenghts_tree_trunks[3], lenghts_tree_trunks[0], lenghts_tree_trunks[1]]
		list4 = [lenghts_tree_trunks[3], lenghts_tree_trunks[0], lenghts_tree_trunks[1], lenghts_tree_trunks[2]]
		possible_orders.append(list1)
		possible_orders.append(list2)
		possible_orders.append(list3)
		possible_orders.append(list4)

	return possible_orders



file_name = 'example_input.txt'
lines = openInput(file_name)

i = 0

while True:

	orders = []
	total_profit = 0

	if len(lines[i]) == 1:

		if int(lines[i]) == 0:
			
			break

	if len(lines[i]) == 1:

		nb_sawmills = lines[i]
		print(f'Case {nb_sawmills}')

		i += 1

	else:

		while len(lines[i]) != 1:

			nb_tree_trunks = lines[i].split()[0]
			lenghts_tree_trunks = [int(i) for i in lines[i].split()[1:]]

			total_profit += maxProfit(lenghts_tree_trunks)

			orders.extend(printOrder(lenghts_tree_trunks))

			i += 1

		print(f'Max profit: {total_profit}')	
		print(f'Order: {orders}')