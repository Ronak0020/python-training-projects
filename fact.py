number = int(input("Enter the number to fidn the factorial of: "))
answer = 1
while number > 0:
    answer *= number
    number -= 1
if number <= 0:
    print("The answer is 0. It does not have a factorial value.")
print(f"The answer is: {answer}")