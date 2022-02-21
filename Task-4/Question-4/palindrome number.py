#checking the given number is a palindrome number or not
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    num=n%10
    rev=rev*10+num
    n=n//10
if(temp==rev):
    print('True')
else:
    print('False')