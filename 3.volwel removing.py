b=[];  c=" "
n="Guvi Geeks Network Private Limited"
print("Guvi Geeks Network Private Limited")
m=len(n)
for i in n:
          b.append(i)
a=['a','e','i','o','u','A','E','I','O','U']                                  
for i in range(0,m):
          if b[i] not in a:
                    c=c+b[i]
print("Removed Volwel : ",c)
