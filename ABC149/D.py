n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = str(input())
score = 0
win = ["others" for i in range(len(t))]
for i in range(n):
	if t[i] == "r":
		if win[i - k] != "p":
			win[i] = "p"
		else:
			win[i] = "others"
	elif t[i] == "s":
		if win[i - k] != "r":
			win[i] = "r"
		else:
			win[i] = "others"
	elif t[i] == "p":
		if win[i - k] != "s":
			win[i] = "s"
		else:
			win[i] = "others"
#print(win)
for i in range(n):
	if win[i] == "r": score += r
	elif win[i] == "s": score += s
	elif win[i] == "p": score += p 
	else: continue
print(score)