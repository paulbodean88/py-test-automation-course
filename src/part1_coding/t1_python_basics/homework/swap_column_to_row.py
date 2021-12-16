"""
1. Define a variable containing a matrix with x rows, x columns
2. Swap the rows with the columns

Example
input
1, 2, 3, 2, 5
4, 1, 7, 2, 9
13, 2, 3, 2, 5
11, 1, 5, 1, 2
3, 6, 10, 12, 11

output
1, 4, 13, 11, 3
2, 1, 2, 1, 6
3, 7, 3, 5, 10
2, 2, 2, 1, 12
5, 9, 5, 2, 11
e.g. your variable
# matrix = [[1, 2, 3, 2, 5],
#           [4, 1, 7, 2, 9],
#           [13, 2, 3, 2, 5],
#           [11, 1, 5, 1, 2],
#           [3, 6, 10, 12, 11]]

"""

# Solution
matrix = [[1, 2, 3],
          [4, 1, 7],
          [13, 2, 3]]

new_matrix = []

for r in range(0, len(matrix)):
    print(matrix[r])
    new_row = []
    for c in range(0, len(matrix[r])):
        new_row.append(matrix[c][r])
    print(new_row, end='\n \n')
    new_matrix.append(new_row)
