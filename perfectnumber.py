def is_perfect_number(number):
    if number <= 1:
        return False

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    if divisor_sum == number:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if is_perfect_number(n):
    print(n, "is a perfect number.")
else:
    print(n, "is not a perfect number.")
