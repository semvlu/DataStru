class Graph:
    def __init__(self, v):
        # #vert
        self.v = v
        # adj list
        self.adj = [0] * v
        for i in range(self.v):
            self.adj[i] = []

    def add(self, i,j):
        self.adj[i].append(j)

    def isCyclic(self):
        visited = [False] * self.v
        helper = [False] * self.v
        for i in range(self.v):
            if visited[i] == False:
                ans = self.DFS(i,visited,helper)
                if ans == True:
                    return True
        return False


    def DFS(self, i, visited, helper):
        visited[i] = True
        helper[i] = True
        neighbours = self.adj[i]

        for k in range(len(neighbours)):
            cur = neighbours[k]

            if helper[cur] == True:
                return True

            if visited[cur] == False:
                ans = self.DFS(cur,visited,helper)
                if ans == True:
                    return True
        helper[i] = False
        return False


n = input()
n = int(n)
g = Graph(n)


while True:
    try:
        e = list(map(int, input().split()))
        if len(e) == 0:
            break
        else:
            g.add(e[0], e[1])
    except EOFError:
        break

if g.isCyclic() == 1:
    print("Cycle")
else:
    print("No Cycle")