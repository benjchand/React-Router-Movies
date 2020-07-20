from collections import deque


def twoSum(nums, target):
    numsDict = dict()
    for x in range(len(nums)):
        firstHalf = nums[x]
        missingHalf = target - firstHalf
        if missingHalf in numsDict.keys():
            return [numsDict[missingHalf], x]
        if nums[x] in numsDict.keys():
            if target-x is x:
                return [numsDict[nums[x]], x]
            continue
        numsDict[firstHalf] = x
    print(numsDict)
    return "The parts of the target are not present in this array"


def myAtoi(str):
    # Whitespace checker variable
    # leftSide, rightSide = 0, 0
    # Convert the string to an array
    # Run through whitespace until you hit a character.
    # Switch Whitespace checker to true
    # switch Minus checker to true
    # Check if the 48 <= ord(character) <= 57
    whiteSpace = False
    leftSide, rightSide = 0, 0
    array = str.split()
    print(array)


# myAtoi("Where are all the good men?")


def rottingOranges(grid):
    queue = deque()
    ROWS, COLS = len(grid), len(grid[0])
    freshOranges = 0
    iterationsCount = -1
    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y] == 2:
                queue.append((x, y))
            if grid[x][y] == 1:
                freshOranges += 1
    queue.append((-1, -1))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        row, col = queue.popleft()
        if row == -1:
            iterationsCount += 1
            if queue:
                queue.append((-1, -1))


print(rottingOranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(rottingOranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))


print(1//2)
