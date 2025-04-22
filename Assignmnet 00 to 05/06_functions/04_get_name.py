                                        ## Problem Statement

# Fill out the get_name() function to return your name as a string! We've written a main() 
# function for you which calls your function to retrieve your name and then prints it in a 
# greeting.

# Here's a sample run of the program where the name we've decided to return is Sophia 
# (the autograder expects the returned name to be Sophia):

# Howdy Sophia ! 🤠

                                        ## Starter Code

# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()

                                        ## Solution

def get_name():
    name = input("Enter your name: ")
    return name

def main():
    name = get_name()
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()
