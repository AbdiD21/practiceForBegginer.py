# Start with the number 2
i = 2

# Loop through numbers from 2 up to 24
while i < 25:
    # Start checking divisors from 2
    j = 2
    
    # Check if any number from 2 to i/j divides i evenly
    while j <= i / j:
        if i % j == 0:
            # If divisible, i is not prime, stop checking
            break
        j = j + 1
    
    # If no divisor found, i is prime
    if j > i / j:
        print(i, "is prime")
    
    # Move to the next number
    i = i + 1

