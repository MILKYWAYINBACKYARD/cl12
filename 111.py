l=list()
print('\n\tMenu Driven Program')
print('\n\tList Manupilation')
print('1 Create a list of Numbers.')
print('2 Display list')
choice=int(input("enter your choice:"))
if choice==1:
    while True:
        x=int(input('enter a number:'))
        if x==0:
            break
        l.append(x)
elif choice==2:
    print(l)
else:
    print('inalid choice!! Please try again')
