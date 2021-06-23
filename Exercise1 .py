n1 = int(input("Type your first number:"))
n2 = int(input("Type your second number:"))
n3 = int(input("Type your third number:"))
numbers = [n1,n2,n3]
result = sorted(numbers,reverse=False)
print("Sorted numbers:", result)
print("Not Sorted numbers:", n1,n2,n3)


