def catalan(shape):
    """
    I want to create a recursive function that calculates a catalan number
    based on the number of a shape given.

    :param shape: The number of sides we want to calculate.
    :return: return 1 if the shape is less than 1 or return the catalan
    numbers if otherwise.
    """

    """
    This is the base case. We want to control if the shape is either 1 or less. 
    The program should return only 1 if it is 1 or less (in the case of it 
    being 0 or 1).
    """
    if shape <= 1:
        return 1

    """
    Create a For Loop that uses recursion to calculate the catalan numbers 
    for shapes greater than 1.
    """
    output = 0
    for index in range(shape):
        output += catalan(shape - index - 1) * catalan(index)
    return output

if __name__ == "__main__":
    """
    """
    for number in range(16):
        print(f"Order " + str(number) + " Catalan number = " + str(catalan(
            number)))
