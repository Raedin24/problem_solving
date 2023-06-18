# Correct syntax, runtime errors because of format of test cases
# Works if there's no space between input

t = int(input())
positions = [

]
for i in range(t):
    board = []
    for _ in range(8):
        rank = input().split()
        board.append(rank)
    

    for rank in range(6):
        a = board[rank][0]
        for j in range(8):
            if a[j] == '#' and  board[rank+2][0][j] == '#' and board[rank][0][j+2] == '#' and board[rank+2][0][j+2] == '#' :
                positions.append([rank+2, j+2])
for position in positions:
    print(*position)
                


"""
Works for this:
3
.....#..
#...#...
.#.#....
..#.....
.#.#....
#...#...
.....#..
......#.
#.#.....
.#......
#.#.....
...#....
....#...
.....#..
......#.
.......#
.#.....#
..#...#.
...#.#..
....#...
...#.#..
..#...#.
.#.....#
#.......

But not this:
3

.....#..
#...#...
.#.#....
..#.....
.#.#....
#...#...
.....#..
......#.

#.#.....
.#......
#.#.....
...#....
....#...
.....#..
......#.
.......#

.#.....#
..#...#.
...#.#..
....#...
...#.#..
..#...#.
.#.....#
#.......
"""