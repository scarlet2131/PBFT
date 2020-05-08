import sys
from pbft import *

class shortest_path:
	def __init__(self,graph,src,dest):
		self.graph = graph
		self.INF = 10**18
		self.src = src
		self.dest = dest
		self.edge = []
	def getMinNode(self,dist,visited):
		m = self.INF
		for i in range(len(dist)):
			if dist[i]<m and not visited[i]:
				m,ind = dist[i],i
		return ind

	def get_path(self):
		n = self.graph.N
		visited = [False for i in range(n+1)]
		dist = [self.INF for i in range(n+1)]
		parent = [ -1 for i in range(n+1)]
		dist[self.src] = 0
		for i in range(n):
			u = self.getMinNode(dist,visited)
			visited[u] = True
			for node,weight in self.graph.adj[u]:
				if not visited[node]:
					if dist[node]>dist[u]+weight:
						dist[node] = dist[u]+weight
						parent[node]= u
					
		# print(dist)
		# print(parent)

		path = self.tracePath(parent)
		# print("shortest path from src to dest from the graph: ",path)
		return path,dist[self.dest]

	def tracePath(self,parent):
		curr = self.dest
		path = []
		while parent[curr]!=-1:
			path.append(curr)
			curr = parent[curr]
		path.append(self.src)
		path =path[::-1]
		for i in range(1,len(path)):
			x,y=path[i-1],path[i]
			self.edge.append([x,y])
		# print("PATHHH:  ",self.edge)
		return path



		'''
		1 2 3
		2 4 6
		3 2 6
		X = 1,2,3
		Y = 2,4,2
		W = 3,6,6
		'''
	



