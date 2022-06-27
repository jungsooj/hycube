import json

c=16.5

#electrical power for charging
p=11.5

#Battery 100%
bat_max = 756.8
bat_max = 1000



#At start current battery = battery max
bat_curr= bat_max

#Battery 70% minimum (30%DoD)
bat_min = bat_max*0.7

#Max puiss that we can use 
p_max = 16

Jobs=[]
b=[]

#number of jobs
n=15

#time set for each job
t=[0,5,2,3,10,3,5,3,30,3,3,25,2,2,2,2,0]

# Electrical power 
w=[0.0,4.1,4.5,5.75,4.5,5.75,4.5,5.75,4.5,5.75,4.5,16,4.5,4.5,4.5,4.5,0.0]



S=[[0,1],[1,2],[2,3],[3,4],[4,12],[5,6],[6,13],[7,8],[8,14],[9,10],[10,15],
   [11,16],[12,5],[13,7],[14,9],[15,11]]

J= range(len(t))
T=range(sum(t))
time=0

#functions definition
def minCheck(bat):
    if bat <= bat_min:
        return True
    else:
        return False
    
def maxCharging(t):
    return p*t
        
def takePic(bat):
    if(minCheck(bat)):
        return False
    else:
        return True
    

#filling the battery conception
for i in range(len(t)):
    x= t[i] * w[i]
    b.append(x)

for j in J:
    if(j == 2 or j == 4 or j == 6 or j == 8):
        if(takePic(bat_curr) == True):
            bat_curr+= 4.59 * maxCharging(t[j])
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
































    
    
    
    
    
