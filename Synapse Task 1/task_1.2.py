lst=['0001','0011','0101','1011','1101','1111']
new_list=[]

for i in lst:
    x=int(i,2)
    new_list.append(x)

print(new_list)
for i in range(len(new_list)-5):
     
      sum=new_list[i]+new_list[i+5]
      
      new_list.append(sum)
      new_list.pop(i)
      new_list.pop(i+4)
print(new_list)
    
for i in range(len(new_list)-4):
     sum=new_list[i]+new_list[i+1]
     new_list.append(sum)
     new_list.pop(i)
     new_list.pop(i)
    
print(new_list)

for i in range (len(new_list)-3):
     sum=new_list[i]+ new_list[i+1]
     new_list.append(sum)
     new_list.pop(i)
     new_list.pop(i)

print(new_list)

for i in range (len(new_list)-2):
     sum=new_list[i]+ new_list[i+1]
     new_list.append(sum)
     new_list.pop(i)
     new_list.pop(i)

print(new_list)
