himno=''
try:
    stream=open('files/intro.txt','r',encoding='utf-8')    
    #print(stream.read())
    himno=stream.read()
    print('...',himno)
    stream.close()
except IOError as e:
    print(e,'.....')
except ValueError as ve:
    print(ve,'+++++')    

print('---',himno)