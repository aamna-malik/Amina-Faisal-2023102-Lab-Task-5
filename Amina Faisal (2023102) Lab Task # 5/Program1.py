dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Error: Cannot divide by zero.")
else:
    quotient = 0
    is_negative = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if is_negative:
        quotient = -quotient

    print(f"The result of the division is {quotient}.")