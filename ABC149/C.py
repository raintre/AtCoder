import math

def isPrime(x):
	if x <= 1:
		return False
	for i in range(2, int(math.sqrt(x) + 1)):
		if x % i == 0: return False
	return True

def solve():
	x = int(input())
	number = x
	while isPrime(number) != True:
		number += 1
	print(number)

solve()