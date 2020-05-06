"""
Leetcode Problem:
Implement function ToLowerCase() that has a string parameter str, and
returns the same string in lowercase.
Example: This -> this
Time complexity: O(n) where n is the amount of characters in a string
"""


def toLowerCase(str):
    output = ""
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            output += chr(ord(char)+32)
        else:
            output += char
    return output


assert toLowerCase("THIS WILL BE SMALL") == "this will be small"
print(toLowerCase("THIS WILL BE SMALL")) #  -> this will be small


"""
LeetCode problem:
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of
weight y has new weight y-x.
At the end, there is at most 1 stone left.
Return the weight of this stone (or 0 if there are no stones left.)
Time complexity: O(n + nlogn) where n is the amount of items in the collection and nlogn
comes from the .sort Time complexity
"""


def lastStone(stones):
    for _ in range(len(stones) - 1):
        stones.sort()
        temp = stones[-1] - stones[-2]
        stones[-1], stones[-2] = temp, -1
    return (stones[-1])


ExampleList = [2, 7, 4, 1, 8, 1]
assert lastStone(ExampleList) == 1
print(lastStone(ExampleList))  #  This will change since we changed the ExampleList above
