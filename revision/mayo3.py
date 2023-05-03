num1=1
while num1 <=1000:
    i=1
    sum=0
    while i<num1:
        if num1%i==0:
            sum+=i
        i+=1
    if num1==sum:
        print(f'{sum} es perfecto')
    num1+=1