import numpy as np
from more_itertools import distinct_permutations
state=np.empty(72,dtype='int')
s=[0,0,0,0,0,0,0,1,2]
perm=list(distinct_permutations(s))
def state_to_number(seq):
    num=0
    for val in seq:
        num=num+(3**seq.index(val))*val
    return num

#for i in range(72):
 #   print(perm[i])
#data=state_to_number(perm[69])
#print(data)

print(len(perm))
for i in range(72):
    state[i]=state_to_number(perm[i])

print(state)

