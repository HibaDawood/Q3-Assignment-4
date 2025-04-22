                                        ## Problem Statement

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() 
# method to call the subtract_seven helper function! If you're stuck, revisit the add_five 
# example from lecture.

                                        ## Starter Code

# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()


                                        ## Solution

# def main():
# 	num: int = 7
# 	num = subtract_seven(num)
# 	print("this should be zero: ", num)

# def subtract_seven(num):
# 	num = num - 7
# 	return num


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()

def subtract_seven(num):
    return num - 7  # Subtract 7 from the given number

def main():
    number = int(input("Enter a number: "))  # Take user input
    result = subtract_seven(number)  # Call the helper function
    print("Result after subtracting 7:", result)  # Display the result

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
