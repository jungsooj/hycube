from mip import Model, BINARY, xsum
from itertools import product

# Operations set
N = 15

# Ressources : we have 3 
u = [[0,0,0],[1,1,1],[1,2,1],[1,5,3],[3,4,1],[6,2,3],[2,3,1],[1,1,1],[2,3,1],[2,2,2],[6,8,6],
     [3,4,1],[3,5,1],[4,2,1],[4,5,6],[1,3,2],[0,0,0]]

# Max ressources
c= [15,100,30]
    
# Time for each operation
p = [0,5,2,3,10,2,3,5,2,3,30,2,3,3,2,25,0]

#set of precedences between operations
S=[[0,1],[1,2],[2,3],[3,4],[4,13],[13,5],[5,6],[6,14],[14,7],[7,8],[8,15],[15,9],
   [9,10],[10,16],[16,11],[11,12],[7,12]]

T=range(sum(p))
R=range(len(c))
J=range(len(p))

m = Model()

x= [[m.add_var(name="x{},{}".format(j,t),var_type=BINARY) for t in T] for j in J]

m.objective= xsum(t * x[N+1][t] for t in T)

for j in J:
    m+= xsum(x[j][t] for t in T) == 1
    
for(r,t) in product(R,T):
    m+=(xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))
<= c[r])
    
for(j,s) in S:
    m+= xsum(t * x[s][t] - t * x[j][t] for t in T ) >= p[j]
    
print("_______________________________________________________________________")
print("Schedule: ")
print("_______________________________________________________________________")
for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))
print("_______________________________________________________________________")
print("Makespan = {}".format(m.objective_value))