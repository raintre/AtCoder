def imos():
	H, W = map(int, input().split())
	
	for y in range(H):
		for x in range(W):
			tiles[y][x] = 0

	for i in range(N):
		tiles[C[i]][A[i]] += 1
		tiles[C[i]][B[i]] -= 1
		tiles[D[i]][A[i]] -= 1
		tiles[C[i]][B[i]] += 1	

	for y in range(H):
		for x in range(1, W):
			tiles[y][x] += tiles[y][x - 1]

	for y in range(1, H):
		for x in range(W):
			tiles[y][x] += tiles[y - 1][x]

	tile_max = 0

	for y in range(H):
		for x in range(W):
			if tile_max < tiles[y][x]:
				tile_max = tiles[y][x]