## program to sort the list with out using sort function
s =[1,0,0,1,1,1,0,1,0]
s1=[]
s2 =[]
s3 =[]
for i in s:
    if s[i]==0:
        s1.append(s[i])
    else:
        s2.append(s[i])
s3 = s1+s2
print(s1)
print(s2)
print(s3)
