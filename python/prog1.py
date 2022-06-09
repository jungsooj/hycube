from mip import Model, BINARY, INTEGER, xsum,minimize, maximize
m=Model()
x=m.add_var()
n=10
x=[m.add_var(var_type=BINARY) for i in range(n)]
print(n)
z = m.add_var(name='zCost', var_type=INTEGER, lb=-10, ub=10)
print(z)
vz = m.var_by_name('zCost')
vz.ub = 5
c=[1,2,3,4,7,5,6,8,9,5]
m.objective= minimize(xsum(c[i]*x[i] for i in range(n)))
m.objective= maximize(xsum(c[i]*x[i] for i in range(n)))
m.write('model.lp')
m.read('model.lp')
print('model has {} vars, {} contraints and {} nzs'.format(m.num_cols, m.num_rows, m.num_nz))