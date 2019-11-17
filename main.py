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
for i in range(5):
    print(i)
    o = looknsay(o)
print("Part 1:",o)