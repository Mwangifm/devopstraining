num1=int(input("Enter the 1st number: "))
op1=input("Enter any of these operator for operation +, -, *, /: ")
num2=int(input("Enter the 2nd number: "))
if op1=='+':
    result1=num1 + num2;
elif op1=='-':
    result1=num1 - num2;
elif op1=='*':
    result1=num1 * num2;
elif op1=='/':
    result1=num1 / num2;
else:
   print("operator is not supported");
op2=input("Enter any of these operator for operation+, -, *, /: ")
num3=int(input("Enter the 3rd number: "))

if op2=='-':
    result=result1 - num3;
elif op2=='+':
    result=result1 + num3
elif op2=='*':
    result=result1 * num3
elif op2=='/':
    result=result1 / num3
else:
   print("operator is not supported");
print(num1,op1,num2,op2,num3,"= ",result)