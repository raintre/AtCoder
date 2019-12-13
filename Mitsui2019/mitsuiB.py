def solve():
	N = int(input())
	for x in range(int(N/1.08), int((N + 1)/1.08) + 1):
		if int(x * 108 / 100) == N:
			print(x)
			exit()
	print(':(')
solve()