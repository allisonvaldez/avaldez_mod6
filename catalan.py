def main(shape):
    """
    I want to create a recursive function that calculates the catalan number
    based on the number of shapes given.

    :param shape: The number of sides we want to calculate.
    :return: return 1 if the shape is less than 1 and return catalan number if
    otherwise.
    """

    """
    This is the base case. We want to control if the shape is 1 or less. 
    The program should return only 1 if it is 1 or less (in the case of it 
    being 0 or 1 really).
    """
    if shape <= 1:
        return 1

    """
    Create a For Loop that uses recursion to calculate the catalan numbers 
    for shapes greater than 1.
    """
    output = 0
    for index in range(shape):
        output += main(index) * main(shape - index - 1)
    return output


if __name__ == "__main__":
    for number in range(16):
        print(f"Order " + str(number) + " Catalan number " + str({main(
            number)}))
