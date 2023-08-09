'''

Thrilling Teleporters allows players to randomize the teleporters each game. However, during development they found that sometimes this can lead to boards where a player cannot get to the end of the board. We want to figure out if this has happened.

You'll be given the following inputs:
- A collection of teleporter strings
- The number of sides on the die
- The square the player starts on
- The last square on the board

Write a function that returns whether or not it is possible to get to the last square from the starting square in any number of turns.

Examples:
teleporters1 = ["10,8", "11,5", "12,7", "13,9"]
               +------------------+
               |        +-----+   |
               v        v     |   |
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
                     ^     ^          |   |
                     +-----|----------+   |
                           +--------------+

With a 4 sided die, starting at square 0 with a board ending at square 20 (as pictured above)
No matter what you roll, it's not possible to get past the teleporters from 10-13.
finishable(teleporters1, 4, 0, 20) => False

If an additional teleporter was added from square 2 to square 15, this would be possible to finish.
teleporters2 = ["10,8", "11,5", "12,7", "13,9", "2,15"]
finishable(teleporters2, 4, 0, 20) => True

But if we started on square 9, then it is still impossible as square 20 cannot be reached.
finishable(teleporters2, 4, 9, 20) => False



Additional Input:
teleporters3 = ["10,8", "11,5", "12,1", "13,9", "2,15"]
teleporters4 = ["2,4", "9,8", "11,7", "12,6", "18,14",
                "19,16", "20,9", "21,14", "22,6", "23,26",
                "25,10", "28,19", "29,27", "31,29", "38,33",
                "39,17", "41,30", "42,28", "45,44", "46,36"]
teleporters5 = ["4,21", "11,18", "13,17", "16,17", "18,21",
                "22,11", "26,25", "27,9", "31,38", "32,43",
                "34,19", "35,19", "36,39", "38,25", "41,31"]

Complexity variable:
B = size of the board
Note: The number of teleporters, T, and the size of the die, D, are bounded by B.

All Test Cases:
                        die, start, end
finishable(teleporters1, 4,   0,    20)  => False (Above)
finishable(teleporters2, 4,   0,    20)  => True  (Above)
finishable(teleporters2, 4,   9,    20)  => False (Above)
finishable(teleporters3, 4,   9,    20)  => True
finishable(teleporters4, 4,   0,    50)  => False
finishable(teleporters4, 6,   0,    50)  => True
finishable(teleporters5, 4,   0,    50)  => True
finishable(teleporters5, 2,   0,    50)  => False

'''

teleporters1 = ["10,8", "11,5", "12,7", "13,9"]
teleporters2 = ["10,8", "11,5", "12,7", "13,9", "2,15"]
teleporters3 = ["10,8", "11,5", "12,1", "13,9", "2,15"]
teleporters4 = ["2,4", "9,8", "11,7", "12,6", "18,14",
                  "19,16", "20,9", "21,14", "22,6", "23,26",
                  "25,10", "28,19", "29,27", "31,29", "38,33",
                  "39,17", "41,30", "42,28", "45,44", "46,36"]
teleporters5 = ["4,21", "11,18", "13,17", "16,17", "18,21",
                  "22,11", "26,25", "27,9", "31,38", "32,43",
                  "34,19", "35,19", "36,39", "38,25", "41,31"]


from collections import defaultdict
                
def destinations(teleporters, die, start, end):
    dic = defaultdict()
    for t in teleporters:
        x = t.split(',')
        dic[x[0]] = x[1]
    res = set()
    # print(dic)
    for i in range (1, die+1):
        if i+start >= end:
            res.add(end) 
        if str(i+start) in dic.keys():
            res.add(int(dic[str(i+start)]))
        else:
            if i+start >= end:
                res.add(end) 
            else:
                res.add(i+start)
    return list(res)
    
def finishable(teleporters, die, start, end):
    def dfs(square, visited):
        if square == end:
            return True
        visited.add(square)

        dest = destinations(teleporters, die, start, end)
        print(dest)

        for val in destinations(teleporters, die, start, end):
            if val <= end and val not in visited and dfs(val, visited):
                return True
        return False

        # for i in range(1, die + 1):
        #     next_square = square + i
        #     if next_square in visited:
        #         continue

        #     for t in teleporters:
        #         t_start, t_end = map(int, t.split(','))
        #         if next_square == t_start:
        #             next_square = t_end
        #             break

        #     if next_square <= end and next_square not in visited and dfs(next_square, visited):
        #         return True

        # return False

    return dfs(start, set())
    



# print(destinations(teleporters1,  6,   0,    20))
# print(destinations(teleporters2,  6,  46,   100))
# print(destinations(teleporters2, 10,   0,    50))
# print(destinations(teleporters3, 10,  95,   100))
# print(destinations(teleporters3, 10,  70,   100))
# print(destinations(teleporters4,  6,   0,   100))

print(finishable(teleporters1, 4,   0,    20))
print(finishable(teleporters2, 4,   0,    20))
print(finishable(teleporters2, 4,   9,    20))
print(finishable(teleporters3, 4,   9,    20))
print(finishable(teleporters4, 4,   0,    50))
print(finishable(teleporters4, 6,   0,    50))
print(finishable(teleporters5, 4,   0,    50))
print(finishable(teleporters5, 2,   0,    50))