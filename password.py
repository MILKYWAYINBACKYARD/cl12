print('hello')
while True:
    password=input('enter password: ')
    if (len(password)<8):
        print('make sure ur password has atleast 8 character')
        continue
    digit=False
    upper=False
    spsyl=False
    special_symbol='!@#$%=-^&*()_+{}|\;\'"::/?.,'
    for y in password:
        if y.isdigit():
            digit=True
        if y.isupper():
            upper=True
        if y in special_symbol:
            spsyl=True
    if digit==False:
        if true 
        print('password must have atleast one digit!!')
        continue
    if upper==False:
        print('password must have atleast one upper case!!')
        continue
    if spsyl==False:
        print('password must contain atleast 1 spsyl!!')
        continue
    print('\n\n Success ur password is valid')
