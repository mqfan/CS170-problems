#Problenm 3: find the longest common increasing subsequence between 2 arrays#

def find(b, c):
	n = 0
	while n <= len(b) - 1:
		if b[n] == c:
			# print c
			return n
		n+=1
	return -1

def rFind(b, c):
	n = len(b) - 1
	while n >= 0:
		if b[n] == c:
			# print c
			return n
		n-=1
	return -1

def prob(a, b):
	subproblems = [0 for x in range(len(a))]
	b_backIndices = [0 for x in range(len(a))]
	b_frontIndices = [0 for x in range(len(a))]
	
	n = len(a) - 1
	while n >= 0:
		b_backIndices[n] = rFind(b, a[n])
		b_frontIndices[n] = find(b, a[n])
		c = n
		while c < len(a):
			if a[n] < a[c] and b_frontIndices[n] < b_backIndices[c]:
				subproblems[n] = max(subproblems[n], subproblems[c])
			c+=1
		if b_frontIndices[n] != -1:
			subproblems[n] = subproblems[n] + 1
		n-=1

	# for n in range(0, len(a)):
	# 	print subproblems[n]
	# print "_______"
	# for n in range(0, len(a)):
	# 	print b_indices[n]
	return subproblems[0]


a = [1, 2, 4, 2, 1, 6, 8]
b = [2, 1, 4, 2, 4, 4, 2, 6]

print prob(a, b)