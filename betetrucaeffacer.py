import game
import gameerror
l1=[]
l2=[]
for i in range(32):
    l1.append(i)
    
for i in range(64):
    l2.append(i)
state2={"layers": ["LUR", "LRG"],"current": 0,"board": [l1,l2]}
print(len(l2))
print(len(l1))
print(range(32))