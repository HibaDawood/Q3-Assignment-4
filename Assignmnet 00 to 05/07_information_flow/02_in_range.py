                                        ## Problem Statement

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high)
#   """
#   Returns True if n is between low and high, inclusive. 
#   high is guaranteed to be greater than low.
#   """

                                        ## Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()

                                        ## Solution
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    """
    return low <= n <= high  # Checks if n is within the range

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()
