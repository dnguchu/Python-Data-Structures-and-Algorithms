#Problem 1
"""
To stop a recursive function from turning to an infinite loop,
we need to have a base case that will stop the function from calling itself over and over.
"""
def recurTest(low, high):
    if low <= high:
        print(low)
        recurTest(low + 1, high)

recurTest(1, 10)