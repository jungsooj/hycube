from itertools import product
from mip import Model, xsum, BINARY


n = 20  # 18 tasks but add two 'dummy' ones

p = [0, 0, 2, 4, 0, 2, 2, 2, 0, 2, 0, 3, 0, 3, 0, 0, 3, 0, 0, 2, 0, 0] # duratopn of each task

u = [[0], [1], [3], [5], [1], [2], [2], [2], [1], [2], [1], [3], [1], [3], [1], [1], [3], [1], [1], [2], [1], [0]] # amount of ressources to process the task

c = [6] # capacity of the ressource

S = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [5, 6], [6, 7], [8, 9], [9, 10],
     [12, 13], [13, 14], [15, 16], [16, 17], [18, 19], [19, 20], [20, 1]] # tasks dependencies

(R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

model = Model()

x = [[model.add_var(name="x({},{})".format(j, t), var_type=BINARY) for t in T] for j in J]

model.objective = xsum(t * x[n + 1][t] for t in T)

for j in J:
    model += xsum(x[j][t] for t in T) == 1

for (r, t) in product(R, T):
    model += (
        xsum(u[j][r] * x[j][t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))
        <= c[r])

for (j, s) in S:
    model += xsum(t * x[s][t] - t * x[j][t] for t in T) >= p[j]

model.optimize()

print("Schedule: ")
for (j, t) in product(J, T):
    if x[j][t].x >= 0.99:
        print("Job {}: begins at t={} and finishes at t={}".format(j, t, t+p[j]))
print("Makespan = {}".format(model.objective_value))
