a=[]; b=[]; k=0
st=input("enter string : ")
for i in st:  a.append(ord(i))
n=len(a)
for i in range(0,n):
          for j in range(i+1,n):
                    if a[i]==a[j]:
                              b.append(chr(a[j]))
                              k=1
b=set(b)
if k==1:
          print('The most frequent character : ',end='')
          for i in b:  print(i,end=' ')
else: print("no frequent character")
