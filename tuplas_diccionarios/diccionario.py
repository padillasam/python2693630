d1={}
print(type(d1))
x,y,z=(),[],{}
print(type(x))
print(type(y))
print(type(z))
ejemplo={'nombre':'SENA',
         0:(1,2),
         1.5:'Soacha'
         }

ejemplo1={3:'tres',
         0:'cero',
         1:'uno'
         }
print(ejemplo1[0])

dictionary = {"gato": "chat", 
              "perro": "chien", 
              "caballo": "cheval"}
print(dictionary)
#print(dictionary['zorro'])
dictionary['gato'] = 'minou'
dictionary['cisne'] ='cygne'
dictionary.update({"pato": "canard",'gato2': 'chat'})

print(dictionary)
#print('cisne' not in dictionary)

words = ['gato', 'león', 'caballo','perro','cisne']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

for key in dictionary.keys():
    print(key, "->", dictionary[key])

print('......',dictionary.items())

for s, f in dictionary.items():
    print(s, "->", f)

for key in sorted(dictionary.keys()):
    print(key)