def vowels_counts(a):
    count=0
    for i in a:
        if i in 'aeiouAEIOU' :
            count+=1
    return count       




string=input('enter a string:')
print('vowels=',vowels_counts(string))