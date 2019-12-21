# coding: utf-8
# Your code here!
def solve():
	mod = 10 ** 9 + 7
	#input
	N, M, *a = map(int, open(0).read().split())

	dp = [0] * (N + 2)
	dp[0] = 0 # i = -1 don't exist 
	dp[1] = 1
	
	#not destroyed
	ok = sorted(set(range(1, N + 1)) - set(a))

	for i in ok:
		dp[i + 1] += (dp[i] + dp[i - 1]) % mod
	print(dp[-1])
solve()
