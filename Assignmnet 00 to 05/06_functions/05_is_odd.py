                                    # Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

                                    # Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
                                    # Solution

def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if i % 2 == 0:
            print(f'{i} even')  # Print 'even' for even numbers
        else:
            print(f'{i} odd')   # Print 'odd' for odd numbers

if __name__ == '__main__':
    main()
