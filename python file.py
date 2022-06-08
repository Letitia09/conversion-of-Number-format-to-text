l={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
a=int(input())
k=[]
while(a!=0):
    r=a%10
    a=a//10
    k.append(l[r])
print(" ".join(k[::-1]))
