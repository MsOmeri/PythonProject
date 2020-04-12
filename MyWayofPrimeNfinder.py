start=int(input("Type the start point: "))
end=int(input("Type the end point: "))

lis1=[]
lis2=[]

for i in range(start,end + 1):
  for j in range(1,i+1):
    if i%j == 0:
      lis1.append(j)
    #print(lis1)
  if len(lis1)==2:
      lis2.append(i)
  lis1=[]
print(lis2)
