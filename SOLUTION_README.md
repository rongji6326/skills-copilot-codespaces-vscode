# Matrix Reading Problem Solution

This repository contains solutions to a competitive programming problem from NowCoder (牛客网).

## Problem Description

Given a parameter `x` and an `n×n` matrix, output the matrix elements in a specific order based on the value of `x`:

- **x = 0**: Output the single element (for 1×1 matrix)
- **x = 45 or 47**: Read the matrix row by row (left to right, top to bottom)
- **x = 124**: Read the matrix in spiral order (clockwise from outside to inside)

### Input Format
- First line: integer `x` (where `x ∈ {0, 45, 47, 124}`)
- Second line: integer `n` (1 ≤ n³ ≤ 667,428), the dimension of the square matrix (n is always odd)
- Next n lines: n integers each, representing the matrix elements (1 ≤ a[i,j] ≤ 667,428)

### Output Format
- One line containing n×n integers separated by spaces

## Solutions

This repository provides three implementations:

1. **C++ Solution** (`solution.cpp`)
2. **Python Solution** (`solution.py`)
3. **Java Solution** (`Solution.java`)

All solutions implement the same logic:
- For x=0: Return the single element
- For x=45 or x=47: Read row by row
- For x=124: Read in spiral order (outside to inside, clockwise)

## Examples

### Example 1 (x=45)
```
Input:
45
3
1 2 1
2 1 2
1 2 1

Output:
1 2 1 2 1 2 1 2 1
```

### Example 2 (x=47)
```
Input:
47
3
1 2 1
2 1 2
1 2 1

Output:
1 2 1 2 1 2 1 2 1
```

### Example 3 (x=124)
```
Input:
124
5
1 2 4 2 1
1 2 1 3 1
2 1 4 1 2
1 2 1 3 1
3 1 2 1 3

Output:
1 2 4 2 1 1 2 1 3 1 2 1 3 1 2 1 2 1 3 1 3 1 2 1 4
```

### Example 4 (x=0)
```
Input:
0
1
6

Output:
6
```

## How to Run

### C++
```bash
g++ -o solution solution.cpp
./solution < input.txt
```

### Python
```bash
python3 solution.py < input.txt
```

### Java
```bash
javac Solution.java
java Solution < input.txt
```

## Algorithm Explanation

### Row by Row (x=45, x=47)
Simple nested loop iteration through rows and columns.

### Spiral Order (x=124)
Use four pointers (top, bottom, left, right) to track boundaries:
1. Read top row from left to right
2. Read right column from top to bottom
3. Read bottom row from right to left
4. Read left column from bottom to top
5. Move boundaries inward and repeat

Time Complexity: O(n²)
Space Complexity: O(n²) for storing the result
