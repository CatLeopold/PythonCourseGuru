#словари
#вариант1
mydict={'Name':'Без имени','Age':'-1'}
print(mydict)
#вариант2
mydict=dict(Name='Без имени',Age='-1')
print(mydict)
name=input('Введите свое имя:')
age=input('Введите свой возраст:')
print(mydict)
mydict['Name']=name
mydict['Age']=age
print(mydict)
for key in mydict:
    print(key,'=',mydict[key])


