current_reading = int(input("enter current reading: "))
previous_reading = int(input("enter previous reading: "))
units = abs(previous_reading - current_reading)
gender = input('Enter a Gender:   ')



if(units >= 500):
    if(gender == 'M'):
        print("The unit rate for Male : ",10*units)
    else:
        print("The unit rate for Female : ",8*units)
        
elif(units >= 400 and units <500):
    if(gender == 'M'):
        print("The unit rate for Male : ",8*units)
    else:
        print("The unit rate for Female : ",7*units)
        
if(units >= 300 and units <400):
    if(gender == 'M'):
        print("The unit rate for Male : ",7*units)
    else:
        print("The unit rate for Female : ",6*units)
        
if(units >= 100 and units <300):
    if(gender == 'M'):
        print("The unit rate for Male : ",4*units)
    else:
        print("The unit rate for Female : ",2*units)
        
if(units >= 0 and units <100):
    if(gender == 'M'):
        print("The unit rate for Male : ",1*units)
    else:
        print("The unit rate for Female : ",0*units)





    
        
