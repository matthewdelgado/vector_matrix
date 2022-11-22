# 1. Write and test a Python function trace(a), that returns the sum of the elements on the main diagonal (upper left to lower right) of a square matrix represented as a list of lists. (In linear algebra, this value is called the trace of the matrix.)
def trace(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i][i]
    return sum


if __name__ == '__main__':  # Run only as a stand-alone program,
    print("Problem 1\n")
    a = [[1.0, 2.0, 3.0],
         [0.4, 0.5, 0.6],
         [0.07, 0.08, 0.09]]
    print(trace(a))
    print("\n")

# 2. Write and test a function display_matrix(m) that takes a matrix and prints it neatly, as a rectangular matrix with aligned right-justified columns. Assume that all the entries in the matrix are positive integers with no more than two digits.


def display_matrix(m):
    print('\n'.join([''.join(['{:4}'.format(item)
          for item in row]) for row in m]))


if __name__ == '__main__':
    print("Problem 2\n")
    m = [[1, 2, 3],
         [11, 21, 31],
         [21, 22, 33]]
    display_matrix(m)
    print("\n")


# 3. Write a program read_matrix(file path) that reads a matrix of integers from a text file. Each line in the file holds integer values for the corresponding row of the matrix, separated by spaces, commas, or tabs. Hint: For testing, use the function from Question 2 to display the resulting matrix.


def read_matrix(pathname):
    matrix = [];
    with open(pathname) as f:
        for line in f:
            matrix.append(line.strip().split(' '))
        return matrix


if __name__ == '__main__':
    print("Problem 3\n")
    m = read_matrix('matrix.txt')
    display_matrix(m)
    print("\n")


# 4. Write and test a function transpose(a), that transposes a given square 𝑛 by 𝑛 matrix and returns the resulting matrix. In the transposed matrix, all elements are flipped symmetrically over the main diagonal: rows become columns and columns become rows.
def transpose(a):
    t = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    return t

if __name__ == '__main__':
    a = [[1, 2, 3],
         [11, 21, 31],
         [21, 22, 33]]
    print("Problem 4\n")
    display_matrix(a)
    print("\n")
    display_matrix(transpose(a))
    print("\n")


# 5. Write and test a function that takes two 𝑛 by 𝑛 matrices and returns their product.
def matrix_dot_matrix(a, b): 
    dot = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                dot[i][j] += a[i][k] * b[k][j]
    return dot
 

if __name__ == '__main__':
    A = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    B = [[1, 2, 3],
        [2, 3, 1],
        [3, 1, 2]]

print("Problem 5\n")
display_matrix(matrix_dot_matrix(A, B))
print("\n")

"""
# 6. (BONUS) System of linear equations
#    (a) Write a Python function determinant (a) that returns the determinant of a give 2 by 2 matrix.
def determinant(a):

# (b) Write a function solve(a, c) that takes a 2 by 2 matrix 𝐴 and a two-dimensional vector 𝑐⃗ as parameters and attempts to solve the system of two linear equations 𝐴𝑥⃗ = 𝑐⃗, using determinants. If the solution exists and is unique, the function should return the vector 𝑥⃗; otherwise the function should return(None, None).
def solve(a, c):

if __name__ == '__main__':
    a = [[2, -7],
        [3, -4]]

    print('determinant =', determinant(a)) 
    x, y = solve(a, [-11, 3])
    print('x =', x, 'y =', y)
"""