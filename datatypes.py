## Datatypes

#Sequence data type
name = 'vaarahi'
print(name)
print(name[0])
print(name[2:5])
print(name[2:])
print(name *2)
print(name + 'INSTITUTE')

'''

#byte datatype
a = [1,20,30,40,50,40]
b = bytes(a)
print(b)

print(b[0])

a = [1,30,200,20,30]
b = bytes(a)
print(b)
'''


''' bytes can store only numbers range 0,256

a = [1,300,200,20,30]
b = bytes(a)
print(b)

* strings or any other datatypes wont accept
a = ['sai',10,200]
print(a)
b = bytes(a)
print(b) '''



#bytearray
a = [20,30,256,456,144]
c = bytearray(a)
print(c)




