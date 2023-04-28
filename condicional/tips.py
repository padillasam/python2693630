#Tip para solucionar numeral 14
u,d,c=0,0,0
for i in range(100,1000):
    #256
    num=i
    u=num%10
    num=num//10
    d=num%10
    c=num//10
    #print(f'{u}  {d}  {c}')
    cubo=(u**3)+(d**3)+(c**3)    
    #print(f'cubo {cubo}')
    #print(f'num {num}')
    if cubo==i:
        print(i)


