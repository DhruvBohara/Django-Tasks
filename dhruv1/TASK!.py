import random
import urllib.request
a = ""
x = input("Binary no")
c = ""
n = 0
m = 0
for y in x:
    if y == ',':
        n = n + 1
for z in x:
    if z != ',':
        a = a + z;
    elif m < n:
        m = m + 1
        b = int(a,2)
        if b % 5 == 0:
            if c != "":
                c = c + "," + a
                a = ""
            else:
                c = c + a
                a = ""
        else:
            a = ""
    else:
        continue

b = int(a,2)
if b % 5 == 0:
    c = c + "," + a
    a = ""
print(c)
