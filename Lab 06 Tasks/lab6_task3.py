#Task 03
def even(n):
    for i in range(1,n):
        if(i%2==0 or i%3==0):
            print(i,end=', ')
    return
even(17)