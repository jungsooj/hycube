from mip import Model, BINARY, maximize, xsum

# Capacity Max / 30: time / 15 : puissance
c=[30,16]

# times
p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

u = []

for i in range(len(p)):
    y= p[i]*4.5
    u.append(y)

I= range(len(p))

M=Model()

x=[M.add_var(var_type=BINARY) for i in I] 

M.objective = maximize(xsum(x[i] * u[i] for i in I))

M+= xsum(x[i] * p[i] for i in I) <= c[0]

M+= xsum(x[i] * u[i] for i in I) <= c[1]

M.optimize()

print("-----------------------------------------------------------------------")
print("result")
print("-----------------------------------------------------------------------")
result = [i for i in I if x[i].x >= 1]
time=0
puiss=0
for i in range(len(result)):
    time += p[result[i]]
    puiss += u[result[i]]
print("in {} min, we use {} w".format(time,puiss))
print("-----------------------------------------------------------------------")