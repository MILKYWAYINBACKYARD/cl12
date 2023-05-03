l=list()
while True:
    print('\n\tMenu Driven Program')
    print('\n\tList Manupilation')
    print('1 Create a list of Numbers.')
    print('2 Display list')
    print('3 display numbers divisble by 7')
    choice=int(input("enter your choice:"))
    if choice==1:
        while True:
            x=int(input('enter a number:'))
            if x==0:
                break
            l.append(x)
    elif choice==2:
        print(l)
    elif choice==3:
        sum=0
        for i in l:
            if i%7==0:
                sum=sum+i
            
        print('numbers divisble by 7:')
else:
         print('inalid choice!! Please try again')
