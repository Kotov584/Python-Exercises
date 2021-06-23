n1 = int(input("Enter a first number:"))
n2 = int(input("Enter a second number:"))
n3 = int(input("Enter a third number:"))
listnumbers = [n1,n2,n3]

'''# 1st way

for i in range(3):
    listnumbers[i]=int(input("Enter ', i+1, 'number:"))'''

'''# 2nd way (list comprehension)

listnumbers=[int(input("Enter number:") for i in range(3)]
'''

odd_count = 0
  
for num in listnumbers: 
      
    if num % 2 != 0: 
        odd_count += 1
          
print("Odd numbers in the list: ", odd_count) 
