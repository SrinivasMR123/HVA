def is_armstrongnumber(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = 0

    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits

    if sum_of_digits == number:
        return True
    else:
        return False
# Test the function
num = int(input("Enter a number: "))
if is_armstrongnumber(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
