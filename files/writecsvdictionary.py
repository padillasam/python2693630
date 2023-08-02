import csv
#conjunto={1,2,3,4}
diccio=[
    {'name':'Alice','age':18},
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
header=['name','age']

with open('files/people.csv','w',newline='') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    writer.writerows(diccio)
