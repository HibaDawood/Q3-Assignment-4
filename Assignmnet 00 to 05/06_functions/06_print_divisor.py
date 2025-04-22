                                    # Problem Statement
# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

                                    # Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
                                    #Solution

def print_divisors(num):
    # Loop from 1 to num (inclusive) to find divisors
    for i in range(1, num + 1):
        if num % i == 0:  # If there is no remainder, it's a divisor
            print(i, end=' ')  # Print divisor

def main():
    num = int(input("Enter a number: "))  
    print("Here are the divisors of", num)
    print_divisors(num)  # Call the helper function to print divisors

if __name__ == '__main__':
    main()
