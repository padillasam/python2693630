try:
    stream=open('files/intro.txt','r',encoding='utf-8')    
    #print(stream.readlines())
    for linea in stream.readlines():
        print(linea)
except IOError as e:
    print(e,'.....')