# Picture grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
'''
Copy the previous grid value, and write code that uses it to print the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
Hint: You will need to use a loop in a loop in order to print grid[0][0], 
then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
This will finish the first row, so then print a newline.
Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on.
The last thing your program will print is grid[8][5].
'''

print('This is grid 0.')
print(grid[0])
print('This is grid 1.')
print(grid[1])
print('This is grid 2.')
print(grid[2])
print('This is grid 3.')
print(grid[3])
print('This is grid 4.')
print(grid[4])
print('This is grid 5.')
print(grid[5])
print('This is grid 6.')
print(grid[6])
print('This is grid 7.')
print(grid[7])
print('This is grid 8.')
print(grid[8])

print('This is the length of the grid.')
print(len(grid))

for y in range(len(grid[0])):
        for x in range(len(grid)):
                print(grid[x][y], end='')
        print('')
