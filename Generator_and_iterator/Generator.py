#generator can be used to create custom seuence

def customgener(x,y):
    while x<y:
        yield x
        x+=1

result= customgener(10,20)

for i in result:
    print(i)