n="Guvi Geeks Network Private Limited"
print("Guvi Geeks Network Private Limited")
c=len(n); a=[]; b=[]; d=[]
for i in n:
          a.append(i)
for i in range(0,c):
          for j in range(i+1,c):
                    if a[i]==a[j]:
                              b.append(a[j])
          if a[i] not in b:
                    d.append(a[i])
print("unique character is : ",end=' ')
for i in d:
          print(i,end='  ')
