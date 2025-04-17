'''
write a simple Python code snippet that accepts n number of elements from the user to create an array, 
then calculates and prints the sum and average of the elements.

'''

# Function to calculate sum and average of an array


def calculate_sum_and_average():
    # Accept number of elements
    n = int(input("Enter the number of elements in the array: "))

    # Initialize an empty array
    array = []

    # Accept elements of the array
    for i in range(n):
        element = float(input(f"Enter element {i + 1}: "))
        array.append(element)

    # Calculate sum and average
    total_sum = sum(array)
    average = total_sum / n if n > 0 else 0

    # Print results
    print(f"Sum of the array elements: {total_sum}")
    print(f"Average of the array elements: {average}")


# Call the function
calculate_sum_and_average()


