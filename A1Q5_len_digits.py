n = int(input("Enter the number:"))
w = 0
while n!=0:
    n //= 10
    w += 1

print("digits:"+str(w))
