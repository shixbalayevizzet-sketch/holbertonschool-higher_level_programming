def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix of the same size.
    """
    # Create a new matrix to store the results without modifying the original
    new_matrix = []
    for row in matrix:
        # Create a new row with squared values using list comprehension
        new_row = [x ** 2 for x in row]
        # Append the processed row to our new matrix
        new_matrix.append(new_row)
    return new_matrix
