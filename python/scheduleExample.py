from mip import Model, BINARY, xsum
from itertools import product

n=3

c=[5]

p=[0,3,2,1,0]

S=[[0,1],[1,2],[1,3],[3,2]]
u=[[0],[3],[4],[2],[0]]

T=range(sum(p))
J=range(len(p))
R=range(len(c))

M= Model()

x=[[M.add_var(name="x{},{}".format(t,j), var_type=BINARY) for t in T] for j in J]

M.objective= xsum(t * x[n+1][t] for t in T)

for j in J:
    M+= xsum(x[j][t] for t in T) == 1
    
for(r,t) in product(R,T):
    M+=(xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))
<= c[r])
    
for(j,s) in S:
    M+= xsum(t * x[s][t] - t * x[j][t] for t in T ) >= p[j]
    

M.optimize()

print("_______________________________________________________________________")
print("Schedule: ")
print("_______________________________________________________________________")
for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))
print("_______________________________________________________________________")
print("Makespan = {}".format(M.objective_value))
