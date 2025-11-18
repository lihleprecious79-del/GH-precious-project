num1=int(input("enter first:"))
num2=int(input("enter second"))

operator=input("enter operator(+,-,*,/):")

if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    if num2==0:
        print("error:cannot divide by zero!")
    else:
        result=num1*num2

else:
    print("invalid operation selection")

print(f"the result is:{result}")
