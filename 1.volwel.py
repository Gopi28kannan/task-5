a=['a','e','i','o','u','A','E','I','O','U'];  b=[];
n="Guvi Geeks Network Private Limited"
print("Guvi Geeks Network Private Limited")
c=len(n); d=len(a); k=0; m=0
for i in n: b.append(i)
for i in range(0,d):
          for j in range(0,c):
                    if a[i]==b[j]: m=m+1
          for j in range(0,c):
                    if a[i]==b[j]: k=k+1; break
if k!=0 and m!=0:
          print(k," volwel declared. And total volwel count is ",m)
          for i in range(0,d):
                    l=0
                    for j in range(0,c):
                              if a[i]==b[j]:  l=l+1
                    for j in range(0,c):                   
                              if a[i]==b[j]:  print(b[j],'=',l); break
else: print("no volwel")
