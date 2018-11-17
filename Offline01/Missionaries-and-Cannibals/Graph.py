from collections import defaultdict

from State import TERMINAL_STATE

import time


class Graph:

	def __init__(self):

		# default dictionary to store graph
		self.expandedDFS = 0
		self.bfs_path = None
		self.graph = defaultdict(list)
		self.bfs_parent = {}
		self.dfs_parent = {}
		self.expandedBFS = 0
		self.exploredBFS = 0

	def addEdge(self, u, v):
		if not u in self.graph.keys():
			self.graph[u] = []
		self.graph[u].append(v)

	def BFS(self, s):
		self.expandedBFS = 0

		self.bfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}
		s.level = 0

		start_time = time.time()
		queue = [s]
		while queue:
			self.expandedBFS += 1

			u = queue.pop(0)

			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				queue.clear()
				self.bfs_parent[TERMINAL_STATE] = u
				return self.bfs_parent

			t = time.time() - start_time
			if t > u.CONSTANTS.MAX_TIME or self.expandedBFS > u.CONSTANTS.MAX_NODES:
				if t > u.CONSTANTS.MAX_TIME:
					print("%.2fs EXCEEDED TIME LIMIT of %.2fs" % (t, u.CONSTANTS.MAX_TIME))
				else:
					print("EXCEEDED NODE LIMIT of %d" % u.CONSTANTS.MAX_NODES)
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				queue.clear()
				return []

			for v in u.successors(False):
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					self.bfs_parent[v] = u
					v.level = u.level + 1
					queue.append(v)
					visited[(v.missionaries, v.cannibals, v.dir)] = True

		self.bfs_parent = {}
		return []

	def DFS(self, s):
		self.dfs_parent[s] = None
		visited = {(s.missionaries, s.cannibals, s.dir): True}

		start_time = time.time()
		stack = [s]
		while stack:
			u = stack.pop()
			self.expandedDFS += 1

			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.expandedDFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				self.dfs_parent[TERMINAL_STATE] = u
				stack.clear()
				return self.dfs_parent

			t = time.time() - start_time
			if t > u.CONSTANTS.MAX_TIME or self.expandedDFS > u.CONSTANTS.MAX_NODES:
				if t > u.CONSTANTS.MAX_TIME:
					print("%.2fs EXCEEDED TIME LIMIT of %.2fs" % (t, u.CONSTANTS.MAX_TIME))
				else:
					print("EXCEEDED NODE LIMIT of %d" % u.CONSTANTS.MAX_NODES)
				print("No of Expanded Nodes: " + str(self.expandedDFS))
				print("No of Explored Nodes: " + str(visited.__len__()))
				stack.clear()
				return []

			for v in u.successors(True):
				if (v.missionaries, v.cannibals, v.dir) not in visited.keys():
					visited[(v.missionaries, v.cannibals, v.dir)] = True
					self.dfs_parent[v] = u
					stack.append(v)
		return []

	def printPath(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		self.printPath(parentList, parentList[tail])
		if tail != TERMINAL_STATE: print(tail)

	def printPathL(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		if tail == TERMINAL_STATE: tail = parentList[tail]

		stack = []

		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]

		while stack:
			print(stack.pop())
