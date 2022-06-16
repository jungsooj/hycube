from mip import Model, xsum, BINARY, maximize, minimize

def minCheck(bat):
    if bat <= 30:
        return True
    else:
        return False
    
def maxCharging(c,p,u,i):
    M=Model()
    x=[M.add_var(var_type=BINARY) for i in I]
    M.objective = maximize(xsum(x[i] * u[i] for i in I))
    M+= xsum(x[i] * p[i] for i in I) <= c[0]
    M+= xsum(x[i] * u[i] for i in I) <= c[1]
    M.optimize()
    
def takePic(bat):
    if(minCheck(bat)):
        return False
    else:
        return True


# Capacity Max / 30: time / 15 : puissance
c=[30,15]
# times
p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
u=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30] 
I= range(len(p)) 


c2=[15,100,100]

u[[5,4,4],[2,1,1],[3,2,2],[10,7,7],[3,2,2],[5,4,4],[3,2,2],
  [30,14,10],[3,2,2],[3,2,2],[25,12,12],[7,6,6],[2,1,1],[2,1,1],
  [2,1,1],[2,1,1]]

S=[[1,2],[2,3],[3,4],[4,13],[5,6],[6,14],[7,8],[8,15],[9,10],[10,16],
   [13,5],[14,7],[15,9],[16,11]]

J= range(len(u))

M= Model()

x= [M.add_var(var_type=BINARY) for i in I]

M.objective= minimize(xsum(x[i] * p[i] for i in I))

 



