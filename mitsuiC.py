def solve():
	X = int(input())
	for i in range(X + 1):
		rest = X - i * 100
		if 0 <= rest and rest <= 5 * i:
			print(1)
			exit()
		if rest < 0:
			break
	print(0)
solve()

def solve():
	X = int(input())
	quotient = X // 100
	remainder = X % 100
	if 0 <= remainder and remainder <= 5 * quotient:
		print(1)
		exit()
	print(0)
solve()

