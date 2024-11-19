import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Node():
    def __init__(self):
        self.u = 0

class Uniform_Grid():
    def __init__(self, N, L):
        self.nodes = [Node() for _ in range(N)]
        self.N = N
        self.L = L
        self.h = L / (N-1)
        for i in range(N // 3, 2 * (N // 3)):
            self.nodes[i].u = 1
    def getNode(self,i):
        return self.nodes[i]
    def getN(self):
        return self.N
class Solver:
    def __init__(self, grid, K, t, lamb):
        self.grid = grid
        self.t = t
        self.K = K
        self.lamb = lamb
    def solve(self):
        N = self.grid.getN()
        for k in range(self.K): # time steps
            tmp = self.grid.nodes[N-1]
            for i in range(N):
                cn = self.grid.nodes[i]
                pn = tmp
                self.grid.nodes[i].u = (1 - self.lamb * self.t / self.grid.h) * cn.u + (self.lamb * self.t / self.grid.h) * pn.u
                tmp = cn
            fig = plt.plot([e.u for e in self.grid.nodes])
            ani  = anim.FuncAnimation(fig=fig, func= self.solve())
            plt.show()
class Saver():
    def __init__(self, grid):
        self.grid = grid
    def save(self):
        print(self.grid.nodes)

gridn = Uniform_Grid(11, 18)
sol = Solver(gridn, 100, 0.1, 5)
sol.solve()
saver = Saver(gridn)
saver.save()
