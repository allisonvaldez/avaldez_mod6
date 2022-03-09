def pascal(number):
    """
    I want to create a recursive function that calculates the pascal triangle
    based on the number given.

    :param number: the number to calculate
    :return: the pascal triangle for that particular number
    """

    """
    This is the base case. We want to control if the number is either 0 or 1, 
    the program should return only 1 (if it encounters either). The else 
    component of the code  is in charge of calling the recursive function to 
    calculate the numbers of the Pascal triangle.
    """
    if number == 1 or number == 0:
        return [1]

    else:
        """
        We know that this is not for the base case so calculate for the row
        starting at 1.
        """
        current_row = [1]

        # Create the recursive aspect of the code
        calculate_previous_row = pascal(number - 1)

        # Set up a loop to calculate the triangle
        for index in range(len(calculate_previous_row) - 1):
            current_row.append(calculate_previous_row[index] + calculate_previous_row[index + 1])
            current_row += [1]

    # Return the calculations of the recursive function
    return current_row

if __name__ == "__main__":
    for index in range(10):
        print(pascal(index))