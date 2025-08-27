#Prime number checker
def check(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    else:
        return True
num = int(input("enter:"))
if check(num):
    print("Its a prime.")
else:
    print("Not a prime.")
