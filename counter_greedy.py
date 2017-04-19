import numpy as np 

itemNumber = 0
weight = 2**32
budget = 2**32
numberItems = 90000
numberConstraints = 1000
charSet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']

file = open("problem1.in", "w")

file.write(str(weight))
file.write("\n")
file.write(str(budget))
file.write("\n")
file.write(str(numberItems))
file.write("\n")
file.write(str(numberConstraints))
file.write("\n")

def generateName(itemNumber):
	itemName = ""
	while itemNumber >= 0:
		if itemNumber == 0:
			itemName = itemName + '0'
			break;
		itemName = itemName + charSet[itemNumber%63]
		itemNumber = itemNumber//63
	return itemName

projectedAverageCost = budget/numberItems * 1.5
sd = budget/numberItems + 0.0

projectedAverageWeight = weight/numberItems * 1.5


def generateCost():
	return np.around(max(0, np.random.normal(projectedAverageCost, sd)), decimals=2)

def generateResaleGood():
	return np.around(max(0, np.random.normal(20, 18)), decimals=2)

def generateResaleBad():
	return np.around(max(0, np.random.normal(2, 1)), decimals=2)

def generateClass():
	return str(itemNumber)

def generateWeightGood():
	return np.around(max(0, np.random.normal(projectedAverageWeight * 0.7, sd)), decimals=2)

def generateWeightBad():
	return np.around(max(0, np.random.normal(projectedAverageWeight * 1.3, sd)), decimals=2)

def generateConstraints():
	constraints = ""
	for x in range (0, numberConstraints):
		newConstraint = ""
		num = np.random.randint(2, 6, dtype="int")
		for y in range (0, num):
			newConstraint += str(np.random.randint(0, numberItems - 1, dtype="int"))
			newConstraint += ", "
		newConstraint = newConstraint[:-2]
		constraints+=newConstraint
		constraints+="\n"
	return constraints

while itemNumber < numberItems//4:
	cost = generateCost()
	resale = cost + generateResaleGood()
	file.write(str(generateName(itemNumber)) + "; " + str(generateClass()) + "; " + str(generateWeightGood()) + "; " + str(cost) + "; " + str(resale) + "\n")
	itemNumber+=1

while itemNumber < numberItems:
	cost = generateCost()
	resale = cost + generateResaleBad()
	file.write(str(generateName(itemNumber)) + "; " + str(generateClass()) + "; " + str(generateWeightBad()) + "; " + str(cost) + "; " + str(resale) + "\n")
	itemNumber+=1


file.write(generateConstraints())

file.close()
