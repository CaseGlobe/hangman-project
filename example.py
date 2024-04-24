import math 

# a take in the value of a from the function
# b take in the value of b from the function
# c take in the value of c from the function


a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

root1 = (-b + math.sqrt((b*b) - (4*a*c)))/(2*a)
root2 = (-b - math.sqrt((b*b) - (4*a*c)))/(2*a)

print(f"Root1 is: {root1}") # should be 9
print(f"Root2 is: {root1}") # should be -1

