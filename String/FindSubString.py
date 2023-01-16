#find All position

s= "Take up one idea and make that idea you life."

subs = "idea"
flag = False
pos = -1
length = len(s)
while True:
    pos = s.find(subs, pos+1, length)
    if pos ==-1:
        break
    print("found at ", pos)
    flag = True
    if flag == False:
        print("Not found")
