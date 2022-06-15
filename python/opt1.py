from mip import Model, BINARY, maximize, xsum

n=3
b=[0,7,3,14,0] #estimated charge
p=[0,10,5,25,0] #time
c=[15,60,100]

J=range(len(p))


M= Model()

x = [ M.add_var(var_type=BINARY) for j in J]

#objective function for max charging
M.objective = maximize(xsum(x[j] * p[j] for j in J))

M += xsum(b[j] * x[j] for j in J) <= c[1]

M.optimize()

selected = [j for j in J if x[j].x >= 0.99]
print("selected items: {}".format(selected))

