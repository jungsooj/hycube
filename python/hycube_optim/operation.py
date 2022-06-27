from mip import Model, BINARY, xsum
from itertools import product
import json

# list of operations
ops=[]

# Time set for operations
time=[]

S=[]


# Stocking thejson data in data (dict)
with open('data.json') as file:
    data = json.load(file)
  
# Getting keys and values of operations
for i in data['operations']:
    print(i,data['operations'][i])
    ops.append(i)
    time.append(data['operations'][i])
 
#just to verify
for i in range(len(ops)):
    print(ops[i])
    print(time[i])
 
S=data['precedences']

# Getting number of pics
num_pic=data["pic number"]


# Function to see if we can take a picture 
def takePic():
    if(bat_curr>bat_min):
        return True
    else:
        return False


#Battery 100%
bat_max = 756.8

#At start current battery = battery max
bat_curr= bat_max

#Battery 30%
bat_min = bat_max*0.3

#Max puiss that we can use 
p_max = 16

Jobs=[]
u=[]
    
# Time for each operation
p = [5,2,2,25]
c=[4.5,4.1,5.75,4.5]

#set of precedences between operations
S=[[0,1],[1,2],[4,3],[2,3],[4,5]]

T=range(100)
J=range(len(p))

for j in range(4):
    k= p[j] * c[j]
    u.append(k)
    
m = Model()

x= [[m.add_var(name="x{},{}".format(j,t),var_type=BINARY) for t in T] for j in J]


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
