def addNumbers(n):
    answer = 0
    while n > 0:
        answer += n
        n -= 1
    return answer

number = int(input("Enter the number: "))
print(addNumbers(number))