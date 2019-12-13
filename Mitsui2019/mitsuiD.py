def solve():
    ans = 1
    N = int(input())
    s = input()
    ans = 0
    for i in range(1000):
    	t = str(i).zfill(3)
    	t_index = 0
    	for s_index in range(N):
    		if s[s_index] == t[t_index]:
    			t_index += 1
    			if t_index == 3:
    				break
    	if t_index == 3:
    		ans += 1
    print(ans)
solve()

def solve():
    ans = 1
    N = int(input())
    s = input()
    ans = 0
    for i in range(1000):
    	t = str(i).zfill(3)
    	t_index = 0
    	for s_element in s:
    		if s_element == t[t_index]:
    			t_index += 1
    			if t_index == 3:
    				break
    	if t_index == 3:
    		ans += 1
    print(ans)
solve()
