"""
SpiritAnimal UserID: BlackKangaroo
Date last edited: 12/11/2019
Challenge number: Final Challenge

Sources: 1) Rotating numpy matrices. StackOverflow
         2) CSCI 343 Neural Netwok Slides
    
    
"""

import neuro
import numpy as np
from itertools import chain


ones=[]
twos=[]
threes=[]
fours=[]
fives=[]
sixes=[]

moreones=[]
moretwos=[]
morethrees=[]
morefours=[]
morefives=[]
moresixes=[]

onesl=[]
twosl=[]
threesl=[]
foursl=[]
fivesl=[]
sixesl=[]

finalones=[]
finaltwos=[]
finalthrees=[]
finalfours=[]
finalfives=[]
finalsixes=[]
finalfloatones=[[]]
finalfloattwos=[[]]
finalfloatthrees=[[]]
finalfloatfours=[[]]
finalfloatfives=[[]]
finalfloatsixes=[[]]



five=np.matrix([[1,1,1,1,1,0,0,0,0,0],  
      [1,0,1,0,1,0,0,0,0,0],
      [1,1,0,1,1,0,0,0,0,0],
      [1,0,1,0,1,0,0,0,0,0],
      [1,1,1,1,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]])


one=np.matrix([[1,1,1,1,1,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,0],
     [1,1,0,1,1,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]])

two=np.matrix([[1,1,1,1,1,0,0,0,0,0],
     [1,0,1,1,1,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,0],
     [1,1,1,0,1,0,0,0,0,0],
     [1,1,1,1,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]])

three=np.matrix([[1,1,1,1,1,0,0,0,0,0],
       [1,0,1,1,1,0,0,0,0,0],
       [1,1,0,1,1,0,0,0,0,0],
       [1,1,1,0,1,0,0,0,0,0],
       [1,1,1,1,1,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]])

four=np.matrix([[1,1,1,1,1,0,0,0,0,0],
      [1,0,1,0,1,0,0,0,0,0],
      [1,1,1,1,1,0,0,0,0,0],
      [1,0,1,0,1,0,0,0,0,0],
      [1,1,1,1,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]])

six=np.matrix([[1,1,1,1,1,0,0,0,0,0],
      [1,0,1,0,1,0,0,0,0,0],
      [1,0,1,0,1,0,0,0,0,0],
      [1,0,1,0,1,0,0,0,0,0],
      [1,1,1,1,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0]])


for x in range(6):
    
    ones.append(np.roll(one,x,axis=1))

    twos.append(np.roll(two,x,axis=1))
    threes.append(np.roll(three,x,axis=1))
    fours.append(np.roll(four,x,axis=1))
    fives.append(np.roll(five,x,axis=1))
    sixes.append(np.roll(six,x, axis=1))


for x in ones:
    for  i in range(6):
        moreones.append(x)
        moreones.append(np.roll(x,i,axis=0))
        moreones.append(np.rot90(x,1))
        moreones.append(np.rot90(x,2))
        moreones.append(np.rot90(x,3))
        moreones.append(np.rot90(x,4))
for x in twos:
    for  i in range(6):
        moretwos.append(x)
        moretwos.append(np.roll(x,i,axis=0))
        moretwos.append(np.rot90(x,1))
        moretwos.append(np.rot90(x,2))
        moretwos.append(np.rot90(x,3))
        moretwos.append(np.rot90(x,4))
        
for x in threes:
    for  i in range(6):
        morethrees.append(x)
        morethrees.append(np.roll(x,i,axis=0))
        morethrees.append(np.rot90(x,1))
        morethrees.append(np.rot90(x,2))
        morethrees.append(np.rot90(x,3))
        morethrees.append(np.rot90(x,4))
        
        
for x in fours:
    for  i in range(6):
        morefours.append(x)
        morefours.append(np.roll(x,i,axis=0))
        morefours.append(np.rot90(x,1))
        morefours.append(np.rot90(x,2))
        morefours.append(np.rot90(x,3))
        morefours.append(np.rot90(x,4))
       
for x in fives:
    for  i in range(6):
        morefives.append(x)
        morefives.append(np.roll(x,i,axis=0))
        morefives.append(np.rot90(x,1))
        morefives.append(np.rot90(x,2))
        morefives.append(np.rot90(x,3))
        morefives.append(np.rot90(x,4))
       
        
for x in sixes:
    for  i in range(6):
        moresixes.append(x)
        moresixes.append(np.roll(x,i,axis=0))  
        moresixes.append(np.rot90(x,1))
        moresixes.append(np.rot90(x,2))
        moresixes.append(np.rot90(x,3))
        moresixes.append(np.rot90(x,4))
       


list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]

for x in moreones:
    x=x.tolist()
    onesl.append(x)
    
for x in onesl:
    finalones.append(list(chain.from_iterable(x)))
    


for x in finalones:
    for i in x:
        for y in range(len(finalfloatones)):
            finalfloatones[y].append(float(i))
finalfl = finalfloatones[0]            

temp=[]
count=0

for elem in finalfl:
        temp.append(elem)
        count=count+1
        if count==100:
            list1.append(temp)
            count=0
            temp = []
                 
     
    
for x in moretwos:
    x=x.tolist()
    twosl.append(x)
    
for x in twosl:
    finaltwos.append(list(chain.from_iterable(x)))
    
for x in finaltwos:
    for i in x:
        for y in range(len(finalfloattwos)):
            finalfloattwos[y].append(float(i))


finalfl2 = finalfloattwos[0]            



for elem in finalfl2:
        temp.append(elem)
        count=count+1
        if count==100:
            list2.append(temp)
            count=0
            temp = []
                     

  

for x in morethrees:
    x=x.tolist()
    threesl.append(x)
    
for x in threesl:
    finalthrees.append(list(chain.from_iterable(x)))

for x in finalthrees:
    for i in x:
        for y in range(len(finalfloatthrees)):
            finalfloatthrees[y].append(float(i))


finalfl3 = finalfloatthrees[0]            



for elem in finalfl3:
        temp.append(elem)
        count=count+1
        if count==100:
            list3.append(temp)
            count=0
            temp = []    





for x in morefours:
    x=x.tolist()
    foursl.append(x)
    
for x in foursl:
    finalfours.append(list(chain.from_iterable(x)))
    
for x in finalfours:
    for i in x:
        for y in range(len(finalfloatfours)):
            finalfloatfours[y].append(float(i))


finalfl4 = finalfloatfours[0]            



for elem in finalfl4:
        temp.append(elem)
        count=count+1
        if count==100:
            list4.append(temp)
            count=0
            temp = []         



for x in morefives:
    x=x.tolist()
    fivesl.append(x)
    
for x in fivesl:
    finalfives.append(list(chain.from_iterable(x)))
    
for x in finalfives:
    for i in x:
        for y in range(len(finalfloatfives)):
            finalfloatfives[y].append(float(i))


finalfl5 = finalfloatfives[0]            



for elem in finalfl5:
        temp.append(elem)
        count=count+1
        if count==100:
            list5.append(temp)
            count=0
            temp = []  
            


for x in moresixes:
    x=x.tolist()
    sixesl.append(x)
    
for x in sixesl:
    finalsixes.append(list(chain.from_iterable(x)))
    
for x in finalsixes:
    for i in x:
        for y in range(len(finalfloatsixes)):
            finalfloatsixes[y].append(float(i))


finalfl6 = finalfloatsixes[0]            



for elem in finalfl6:
        temp.append(elem)
        count=count+1
        if count==100:
            list6.append(temp)
            count=0
            temp = []  
               
inputs=[]
targets=[]
for x in list1:
    inputs.append(x)
    targets.append([0.1])

for x in list2:
    inputs.append(x)
    targets.append([0.2])
for x in list3:
    inputs.append(x)
    targets.append([0.3])
for x in list4:
    inputs.append(x)
    targets.append([0.4])
for x in list5:
    inputs.append(x)
    targets.append([0.5])
for x in list6:
   inputs.append(x)
   targets.append([0.6])
    

reps=10000
network=[] 
network=neuro.setup_network(inputs)

neuro.train(network, inputs, targets, reps)
neuro.writeNetworkToFile("myNetwork.net", network)

