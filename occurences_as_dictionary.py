##Convert list into dictionary and find the occurences
s = ['keyboard','mouse','laptop','bag','bag']

output = {}

for i in s:
    if(i in output):
        output[i]= output[i]+1
    else:
        output[i] = 1
print(output)
