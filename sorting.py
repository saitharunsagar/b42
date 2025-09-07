print("Try programiz.pro")
s = [1,2,3,4,1,2,3,4,1,2,3,5]
s1 = []
s2 =[]
s3 = []
s4 = []
s5 = []
s6 = []

for i in s:
    if i == 1:
        s1.append(i)
    if i == 2:
        s2.append(i)
    if i == 3:
        s3.append(i)
    if i == 4:
        s4.append(i)
    if i ==5:
        s5.append(i)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
s6 = s1+s2+s3+s4+s5
print(s6)
