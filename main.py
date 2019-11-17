Input = "1113222113"
#Input = "1"
def looknsay(x):
    x = str(x)+" "
    total = ""
    temp = ""
    num = 0
    for i in x:
        if i == temp:
            num+=1
        else:
            if temp != "":
                total = total + str(num) + temp
            temp = i
            num = 1
    return(total)
o = Input
for i in range(40):
    print(i+1)
    o = looknsay(o)
t = Input
print("start t")
for i in range(50):
    print(i+1)
    t = looknsay(t)
print("Part 1:",len(o))
print("Part 2:",len(t))