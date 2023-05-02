def power(a, b):
    """
    Recursive function to calculate the power of one integer to another.
    """
    # Base case: if b is 0, the result is always 1.
    if b == 0:
        return 1

    # If a or b is less than or equal to 0, return -1 to indicate an error.
    if a <= 0 or b <= 0:
        return -1

    # If b is odd, calculate a^(b-1) and multiply it by a.
    if b % 2 == 1:
        return a * power(a, b-1)

    # If b is even, calculate a^(b/2) and square it.
    else:
        return power(a, b//2) ** 2


    result = power(2, 3)
    print(result)  # Output: 8
    # This will calculate 2 to the power of 3, which is 8, and assign the result to the variable result.

    def binary_search(numbers, num, low, high):
        """
        Binary search using recursion.
        Finds the index of the element `num` in the list `numbers`.
        """
        # Base case: if `low` is greater than `high`, the element is not in the list.
        if low > high:
            return -1

        # Calculate the middle index.
        mid = (low + high) // 2

        # Check if the middle element is the element we're looking for.
        if numbers[mid] == num:
            return mid

        # If the middle element is greater than the element we're looking for,
        # search the left half of the list.
        elif numbers[mid] > num:
            return binary_search(numbers, num, low, mid - 1)

        # If the middle element is less than the element we're looking for,
        # search the right half of the list.
        else:
            return binary_search(numbers, num, mid + 1, high)

        numbers = [1, 3, 5, 7, 9]
        num = 5
        result = binary_search(numbers, num, 0, len(numbers) - 1)
        print(result)  # Output: 2