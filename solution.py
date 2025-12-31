def read_row_by_row(matrix, n):
    result = []
    for i in range(n):
        for j in range(n):
            result.append(matrix[i][j])
    return result

def read_spiral(matrix, n):
    result = []
    top, bottom, left, right = 0, n - 1, 0, n - 1
    
    while top <= bottom and left <= right:
        # Read top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Read right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Read bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Read left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

def main():
    x = int(input())
    n = int(input())
    
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    result = []
    
    if x == 0:
        # For single element
        result.append(matrix[0][0])
    elif x == 45 or x == 47:
        # Read row by row
        result = read_row_by_row(matrix, n)
    elif x == 124:
        # Read in spiral order
        result = read_spiral(matrix, n)
    
    # Output the result
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
