numbers=1234
rev=""
while numbers>0:
    digit=numbers%10
    rev=rev*10+digit
    numbers=numbers//10
print(rev)