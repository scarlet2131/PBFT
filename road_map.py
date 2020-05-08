import sys

class road_map:
	def __init__(self, file_name):
		self.file_name = file_name
		self.N = 0
		self.X,self.Y,self.W = [],[],[]

	def gen_graph(self):
		f = open(self.file_name, "r")
		lines = f.readlines()
		self.adj = {}
		for z in lines:
			x,y,w = z.split()
			x,y,w = int(x),int(y),int(w)
			self.X.append(x)
			self.Y.append(y)
			self.W.append(w)
			self.N = max(self.N,x,y)
			# print(x,y,w)
			if x in self.adj:
				self.adj[x].append([y,w])
			else:
				self.adj[x] = [ [y,w] ]
			if y in self.adj:
				self.adj[y].append([x,w])
			else:
				self.adj[y] = [ [x,w] ]
		# for x in self.adj:
			# print(x,self.adj[x])	




		# for k,v in adj.items():
		# 	print(k,v)





