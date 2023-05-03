def count_string(boom,bastic):
    count=0
    for i in boom:
        if i in bastic:
            count+=1
    return count









boom=input('enter a string:')
bastic=input('enter a char:')
print('the count:',count_string(boom,bastic))