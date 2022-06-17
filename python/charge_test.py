from mip import Model, BINARY, maximize, xsum

# Capacity Max / 30: time / 15: puissance max
c=16
w=4.5

t=10

# times
p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

I= range(len(p))

M=Model()

x=[M.add_var(var_type=BINARY) for i in I] 

M.objective = maximize(xsum(x[i] * p[i] * 4.5 for i in I))

M+= xsum(x[i] * p[i] for i in I) <= t

M+= xsum(x[i] * p[i] * 4.5 for i in I) <= c

M.optimize()

print("-----------------------------------------------------------------------")
print("result")
print("-----------------------------------------------------------------------")
result = [i for i in I if x[i].x >= 1]
time=0
puiss=0
for i in range(len(result)):
    time += p[result[i]]
puiss= time*4.5
print("in {} min, we charge {} w".format(time,puiss))
print("-----------------------------------------------------------------------")