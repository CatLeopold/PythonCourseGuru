#импорт модуля и всех его функций
from math import *

# round - округление числа
print(round(2.4367,2))
print(round(2.4567,2))
x=0
while x<180:
    x+=1
    #print(x)
    print("sin("+str(x)+")=",sin(radians(x)))

