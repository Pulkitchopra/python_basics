num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
c=input("Enter the operator +,-,*,/ : ")

if (c=='+' and num1==56 and num2==9):
    print('77')
elif (c=='*' and num1==45 and num2==3):
    print('555')
elif (c=='/' and num1==56 and num2==4):
    print('4')
elif c=='+':
    print(int(num1)+int(num2))
elif c=='-':
    print(int(num1)-int(num2))
elif c=='*':
    print(int(num1)*int(num2))
elif c=='/':
    print(int(num1)/int(num2))
