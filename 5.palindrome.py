b=[]; c=''
st=input("enter string : ")
for i in st:
          b.append(i)
b.reverse()
for i in b:
          c=c+i
if st==c:
          print(st,' is ',c,".  True is polindrome")
else:
          print(st,' is not ',c,".  False is not polindrome")
