try:
    stream=open('files/intro.txt','r',encoding='utf-8')    
    cont=1
    for linea in stream:
        print(f"{cont} {linea}")
        cont+=1   
except IOError as e:
    print(e,'.....')

#print(f"{cont} lineas")