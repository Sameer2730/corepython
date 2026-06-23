num=2002
original=str(num)
reverse=original[::-1]
if original==reverse:
    print("palindrome")
else:
    print("not a palindrome")
##########################################33
n=2002
rev=0
while n>=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if n==rev:
    print("palindrome")
else:
    