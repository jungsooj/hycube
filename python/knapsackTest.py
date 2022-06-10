from mip import Model, BINARY, xsum, maximize

w=[8,13,5,23]
p=[88,23,15,3]
C = 33
I= range(len(p))

m=Model()

x=[m.add_var(var_type=BINARY) for i in I]

m.objective = maximize(xsum(p[i] * x[i] for i in I))

m+= xsum(w[i] * x[i] for i in I) <= C

m.optimize()

result=[i for i in I if x[i].x >= 1]

print("result = {}".format(result))


