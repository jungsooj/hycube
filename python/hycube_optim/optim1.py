from mip import Model, xsum, BINARY, maximize, minimize
from itertools import product

def minCheck(bat):
    if bat <= 30:
        return True
    else:
        return False
    
def maxCharging(c,p,w,t):
    I= range(len(p))
    M=Model()
    x=[M.add_var(var_type=BINARY) for i in I] 
    M.objective = maximize(xsum(x[i] * p[i] * 4.5 for i in I))
    M+= xsum(x[i] * p[i] for i in I) <= t
    M+= xsum(x[i] * p[i] * 4.5 for i in I) <= c
    M.optimize()
    
def takePic(bat):
    if(minCheck(bat)):
        return False
    else:
        return True

# 10: time / 15: puissance max
c=16
w=4.5
t=10
# times
p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Battery 100%
bat_max = 756.8
bat_curr=756.8
#Battery 30%
bat_min = 226.8
p_max = 16
n=16



#time set for each job
time=[0,5,2,3,10,3,5,3,30,3,3,25,7,2,2,2,2,0]

# Electrical power 
w1=[0.0,16.0,4.5,5.75,4.1,4.5,4.1,5.75,4.1,5.75,5.75,16,4.1,4.5,4.5,4.5,4.5,0.0]
b=[]
for i in range(len(time)):
    x= time[i] * w1[i]
    b.append(x)

S=[[0,1],[1,2],[2,3],[3,4],[4,13],[5,6],[6,14],[7,8],[8,15],[9,10],[10,16],
   [13,5],[14,7],[15,9],[16,11],[16,17]]

J= range(len(p))

M= Model()

x= [[M.add_var(name="x{},{}".format(j,t),var_type=BINARY) for t in range(sum(time))] for j in J]

M.objective= minimize(xsum(x[n+1][i] * w1[i] for i in range(sum(time))))


  
for j in J:
    bat_curr -= b[j]
    if(j == 4):
        bat_curr+= 4.5*10
    print(bat_curr)
    if(takePic(bat_curr) == False):
        j+=1
    M+= xsum(x[j] * w1[j] for j in J) <= 16
    M+= xsum(x[j] * b[j] for j in J) >= bat_min
    
for(j,s) in S:
    M+= xsum(t * x[s][t] - t * x[j][t] for t in range(sum(time)) ) >= time[j]

        
selected = [j for j in J if x[j] >= 0.99]
print("selected items: {}".format(selected))
    