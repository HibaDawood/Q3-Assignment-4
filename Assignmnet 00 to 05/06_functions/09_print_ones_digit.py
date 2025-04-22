                                    # Problem Statement
# Write a function called print_ones_digit , which takes as a parameter an integer num and 
# prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. 
# Call your function from main()!

# Here's a sample run (user input is in blue):
# Enter a number: 42 The ones digit is 2

                                    # Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
                                    # Solution

def print_ones_digit(num):
    # Get the ones digit using the modulo operator
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Take user input for the number
    print_ones_digit(num) 

if __name__ == '__main__':
    main()
