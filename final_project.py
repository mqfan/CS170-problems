import numpy as np

seen_classes = Set()
incompatibilities = {}

for constraint in constraints:
	for clas in constraint:
		if clas not in seen_classes:
			seen_classes.add(clas)
			incompatibilities[clas] = Set()
		for cl in constraint:
			incompatibilities[clas].add(cl)


def greedy_alg1(money, weight, items) {
	num_items = items.length
	items_remaining = num_items // 10
	while (items_remaining > 0)
		indices = np.random.randint(0, high=items.length, size=num_items//10)

	
}