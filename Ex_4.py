import random
flower=['rose','sunflower','tulip']
colour=['red','green','blue','yellow','orange']
a=[]
for i in range(3):
    a.append(random.choice(colour))
print(list(zip(flower,a)))