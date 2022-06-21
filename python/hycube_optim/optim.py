from mip import Model, xsum, BINARY, maximize
import json

#electrical power for charging
w=4.5

# times
p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Battery 100%
bat_max = 756.8

#At start current battery = battery max
bat_curr=756.8

#Battery 30%
bat_min = 226.8

#Max puiss that we can use 
p_max = 16

Jobs=[]
b=[]

#number of jobs
n=16

#time set for each job
t=[0,5,2,3,10,3,5,3,30,3,3,25,7,2,2,2,2,0]

# Electrical power 
w1=[0.0,16.0,4.5,5.75,4.1,4.5,4.1,5.75,4.1,5.75,5.75,16,4.1,4.5,4.5,4.5,4.5,0.0]

S=[[1,2],[2,3],[3,4],[4,13],[5,6],[6,14],[7,8],[8,15],[9,10],[10,16],
   [13,5],[14,7],[15,9],[16,11]]

J= range(len(t))
T=range(sum(t))
time=0

def minCheck(bat):
    if bat <= bat_min:
        return True
    else:
        return False
    
def maxCharging(c,p,w,t):
    I= range(len(p))
    M=Model()
    x=[M.add_var(var_type=BINARY) for i in I] 
    M.objective = maximize(xsum(x[i] * p[i] * 4.5 for i in I))
    M+= xsum(x[i] * p[i] for i in I) <= t
    M+= xsum(x[i] * p[i] * w for i in I) <= c
    M.optimize()
    result= [i for i in I if x[i].x >= 0.99]
    time= 0
    for i in range(len(result)):
        time += p[result[i]]
    return time * 4.5
        

def takePic(bat):
    if(minCheck(bat)):
        return False
    else:
        return True

for i in range(len(t)):
    x= t[i] * w1[i]
    b.append(x)

for j in J:
    print(minCheck(bat_curr))
    if(j == 2 or j == 4 or j == 6 or j == 8):
        if(takePic(bat_curr) == True):
            bat_curr+= 4.59 * maxCharging(16,p,w,t[j])
            Jobs.append(j)
        else:
            bat_curr -= 4.1
    else:
        Jobs.append(j)
        bat_curr -= b[j]

dicts={}
print("_____________________ Jobs ___________________________")
print("______________________________________________________")
for j in J:
    print("job {} starts at {} and finish at {}".format(Jobs[j],time,time+t[j]))
    time+= t[j]
    dicts[Jobs[j]] = [time, time+t[j]]
print("______________________________________________________")

with open("dicts.json", 'w') as output:
    json.dump(dicts,output)
































    
    
    
    
    
