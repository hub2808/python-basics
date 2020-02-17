a=list(map(int,input().split(',')))
print(a)
b=a[0]
c=a[0]
for i in range (len(a)):
    if b < a[i]:
       b=a[i] 
print(b)
for i in range (len(a)):
    if c > a[i]:
       c=a[i]
print(c)
