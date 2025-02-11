# 1. This function counts how many even numbers there are from num to 0. howManyEven(9) would return 5. 
# 2. isOdd(3) returns True because 3 is an odd number and it has a modulo of 1. 
# 3. 
def factorial(num):
    total = 1
    if num < 0:
        num *= -1  
    while num > 0:
        total *= num
        num -= 1
        return total
# 4. The fraction 3/4 is equal to 3 divided by 4 and therefore using floor divison turns the fraction into an integer. n = 3 // 4


#input: a number
#output: the number of even numbers between that number and 0 (including 0 and the number)
def howManyEven(num):
    count = 0
    if num < 0:
        num *= -1
    while(num >= 0):
        if isEven(num):
            count += 1
        num -= 1
    return count
    
#input: a number
#output: true/false depending on whether the number is even or not
def isEven(num):
    return num % 2 == 0
    
#input: a number
#output: true/false depending on whether the number is odd or not
def isOdd(num):
    return num % 2 != 0
  
def noChange(cents):
    dollars = cents // 100  
    if cents % 100 == 0:  
        print("Hoorah!")
    else:
        print("Keep the change!")
     return dollars
  


#input: num–an int of some kind
#output: the positive factorial of num
def oldFactorial(num):
    total = 1
    if num < 0:
        num = num * (-1)
    while(num == num):
        if num <= 0:
            break
        else:
            total = total * num
            num = num - 1
    return total
  
print("TESTING", noChange(100)) 
print("TESTING", noChange(225))    
def main():
    print(howManyEven(4))
    print(howManyEven(9))
    print(isOdd(12))
    print(isEven(12))
    
if __name__ == "__main__":
    main()
