def list_divide(numbers, divide = 2):
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count
# The function returns the number of elements in the numbers list that are divisibleby divide

class ListDivideException(Exception):
        pass
# The ListDivideException class is defined to handle exceptions that may occur when the list_divide function is called

def test_list_divide():
    # Test list_divide
     
# Test list_divide with the following test cases: Numbers divisible by 2
    if list_divide([1,2,3,4,5]) != 2:
        raise ListDivideException("Test case 1 failed!")

# Test list_divide with the following test cases: Numbers divisible by 2
    if list_divide([2,4,6,8,10]) != 5:
        raise ListDivideException("Test case 2 failed!")

# Test list_divide with the following test cases: Numbers divisible by 10
    if list_divide([30, 54, 63,98, 100], divide=10) != 2:
        raise ListDivideException("Test case 3 failed!")

# Test list_divide with the following test cases: Empty list
    if list_divide([]) != 0:
        raise ListDivideException("Test case 4 failed!")

# Test list_divide with the following test cases: Numbers divisible by 1
    if list_divide([1,2,3,4,5], 1) != 5:
        raise ListDivideException("Test case 5 failed!")    
   
if __name__ == "__main__":
    try:
        test_list_divide()
        print("All test cases passed!")
    except ListDivideException as x:
        print(f"An error occurred!: {x}")