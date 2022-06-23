from mip import Model, BINARY, xsum
from itertools import product
import json


with open('data.json') as file:
    data = json.load(file)
    
#print(data['operations'])
#for key, value in data["operations"]:
    #print(key)
 
dicts={"TM download" : 16,
"sun pointing" : 2,
"picture" : 3,
"station pointing" : 5}

for i in dicts:
    print(i, dicts[i])

pic=data["pic number"]
print(pic)

J=range(4)

def takePic():
    return True

#pic_number= int(input("enter number of pictures"))

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


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
