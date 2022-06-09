from mip import Model, xsum, maximize, BINARY

p = [10, 13, 18, 31, 7, 15] #p: estimated profit (value)
w = [11, 15, 20, 35, 10, 33] # w: weight
c, I = 47, range(len(w)) # I: items ; c: Capacity

m = Model("knapsack")

# Container
x = [m.add_var(var_type=BINARY) for i in I]

# Objectif function for max profits
m.objective = maximize(xsum(p[i] * x[i] for i in I))

#Weights sum
m += xsum(w[i] * x[i] for i in I) <= c

m.optimize()

selected = [i for i in I if x[i].x >= 0.99]
print("selected items: {}".format(selected))