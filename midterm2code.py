#Chain matrix multiplication optimization

def chain_matrix_multiply(ordered_tuples):
	




#Problem 2: find the smallest lexicographic substring of length k

def prob2(s, k):
	subproblems = [[0 for x in range len(s)] for y in range k]






#Problenm 3: find the longest common increasing subsequence between 2 arrays#

def find(b, c):
	n = 0
	while n <= len(b) - 1:
		if b[n] == c:
			# print c
			return n
		n+=1
	return -1

def rFind(b, c, i):
	n = i
	while n >= 0:
		if b[n] == c:
			# print c
			return n
		n-=1
	return -1

def prob3(a, b):
	subproblems = [0 for x in range(len(a))]
	b_backIndices = [-1 for x in range(len(a))]
	
	n = len(a) - 1
	while n >= 0:
		b_backIndices[n] = rFind(b, a[n], len(b) - 1)
		# b_frontIndices[n] = find(b, a[n])
		c = n
		while c < len(a):
			if a[n] < a[c]:
				tempIndex = rFind(b, a[n], b_backIndices[c])
				b_backIndices[n] = max(b_backIndices[n], tempIndex)
				if tempIndex != -1:
					subproblems[n] = max(subproblems[n], subproblems[c])
			c+=1
		if b_backIndices[n] != -1:
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

print prob3(a, b)