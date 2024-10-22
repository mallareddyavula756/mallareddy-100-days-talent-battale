def sum_of_digits(number):
    number = abs(number)
    
    total_sum = 0
    
    while number > 0:
        total_sum += number % 10 
        number //= 10 
        
    return total_sum
num = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits(num)}")