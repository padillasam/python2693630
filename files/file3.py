try:
    stream=open('files/intro.txt','r',encoding='utf-8')    
    cont=1
    linea=stream.readline()
    c=1
    while linea!="":
        print(f"{c} {linea}")
        linea=stream.readline()
        c+=1
except IOError as e:
    print(e,'.....')