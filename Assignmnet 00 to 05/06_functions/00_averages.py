                                    ## Problem Statement

# Write a function that takes two numbers and finds the average between the two.

                                    ## Starter Code

# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()

                                    ## Solution

def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    # Ask user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Call the function to find average
    avg = find_average(num1, num2)

    print("The average is:", avg)

if __name__ == '__main__':
    main()
