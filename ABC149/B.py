def solve():
	a, b, k = map(int, input().split())
	if k <= a:
		print(max(0, a - k), b)
	elif k <= a + b:
		print(0, max(0, b - (k - a)))
	else:
		print(0, 0)
solve()