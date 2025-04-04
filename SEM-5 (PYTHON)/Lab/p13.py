n=int(input("Enter a five digit number : "))
value=10000
while value > 0:
            digit = n// value 
            print(digit,end=' ') 
            n %= value
            value //= 10 