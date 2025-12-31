# A.-Special-Permutation
for _ in range(int(input())):
	n = int(input())
	lst = []
	for i in range(1,n+1):
		if i == n:
			lst.append(1)
		else:
			lst.append(i+1)
	print(*lst)
