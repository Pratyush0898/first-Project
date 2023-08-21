#a,b,obj is used to receive input from user
#if, elif and else is used to operate and print output

print ('Calculator')

a=int(input('enter the value1:'))
b=int(input('enter the value2:'))
opr=input('enter the opator:')

if opr=="+":
    print(a+b)
   
elif opr=="-":
    print(a-b)
    
elif opr=="*":
    print(a*b)
    
elif opr=="/":
    print(a/b)
    
else:
    print('invaled oprator')