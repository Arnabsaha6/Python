import random
f=open("int.txt","w")
for count in range(1,500):
    number=random.randint(1,500)
    f.write(str(number)+"\n")
f.close()
