num1=int(input("Enter the number"))
num2=int(input("Enter the number2"))
x=[]
for i in range (1,min(num2,num1)+1):
    if num1%i==0 and num2%i==0:
      x.append(i)
print(max(x))

    
