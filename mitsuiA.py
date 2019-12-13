# def read_data():
# 	m1, d1, m2, d2 = map(int, open(0).read().split())
def solve():
	m1, d1, m2, d2 = map(int, open(0).read().split())
	if m1 != m2:
		print('1')
	else:
		print('0')
solve()