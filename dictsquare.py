"""dict1={1:"Hello",2:"how",3:"are",4:"you"}
dict2={"x":"i","y":"am","z":"fine"}
print(dict1)
print(dict2)
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)"""
n=15
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
