import time
import tracemalloc

def addEdge(adj, x, y):
	adj[x].append(y)
	adj[y].append(x)

def dfs(adj, dp, src, par):
	for child in adj[src]:
		if child != par:
			dfs(adj, dp, child, src)

	for child in adj[src]:
		if child != par:
			# not including source in the vertex cover
			dp[src][0] = dp[child][1] + dp[src][0]

			# including source in the vertex cover
			dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])

def minSizeVertexCover(adj, N):
	dp = [[0 for j in range(2)] for i in range(N+1)]
	for i in range(1, N+1):
		# 0 denotes not included in vertex cover
		dp[i][0] = 0

		# 1 denotes included in vertex cover
		dp[i][1] = 1

	dfs(adj, dp, 1, -1)

	# printing minimum size vertex cover
	print("Jumlah vertes minimum: ", min(dp[1][0], dp[1][1]))

size_data = [[10000, "kecil_dp"], [100000, "sedang_dp"], [1000000, "besar_dp"]]

for sidata in size_data:
	adj = [[] for i in range(sidata[0]+1)]

	with open(f"input\data_{sidata[1]}.txt", "r") as f:
		for data in f:
			clean = data.strip().split()
			edge = []
			
			datas = clean[1:]
			node = clean[0]

			for i in datas:
				if len(datas) >= 1:
					addEdge(adj, int(node)+1, int(i)+1)

	print(f"Dataset data_{sidata[1]}.txt")

	tracemalloc.start()
	start = time.time() * 1000
	minSizeVertexCover(adj, sidata[0])
	end = time.time() * 1000
	dp_m = tracemalloc.get_traced_memory()
	tracemalloc.stop()

	print("Waktu dynamic programming adalah adalah:", end - start, "ms")
	print("Memori dynamic programming adalah:", dp_m[1], "block")

	print("="*20)
