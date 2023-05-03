list1,list2=[],[]
def integers_list(a,b):
    list=[]
    for i in list1:
        if i in list2:
            list.append(i)
    return list        


a=int(input('enter no of no.:'))
for i in range(a):
    b=int(input('enter no:'))
    list1.append(b)

c=int(input('enter no of no.:'))
for i in range(c):
    d=int(input('enter no plssss!!:'))
    list2.append(d)

print('THE COOMON NUMBERS ARE:',integers_list(list1,list2))