'''
Leetcode problem: reverse int,
reverse the input integer from front to back, so 23 to 32
POSSIBLE TEST INPUTS
76, 89, 100, -90
PSEUDO
- Convert int to string
- loop over in a reverse way index- total length
- convert string to int and return value
'''


def reverse(number):
    """
    Variable table:
    * reverse = 54
    * index = 2
    """
    reverse = ''
    for index in range(len(str(number))):
        reverse += str(number)[(len(str(number))-1)-index]
    return int(reverse)


'''
Leetcode problem: Given a sorted list and a target, return index of the target given
POSSIBLE TEST INPUTS
([1,2,3,4,5], 3), ([10,22,45], 10))
PSEUDO
- Use Binary search
- Begin by middle and determin if target is less or greater than its neighbors
- Continue splitting itself by 2
'''


def binary_search(array, item):
    """ Assuming array is already Sorted"""
    """
    Variable table:
    * start = 5
    * end = 6
    * target = 5
    * temp_list = [5,6]
    """
    start = 0
    end = len(array) - 1
    target = (len(array) - 1)//2
    while True:
        if target == len(array) or target < 0:
            return None
        temp_list = [array[target], item]
        temp_list.sort()
        if array[start] == item:
            return start
        elif array[end] == item:
            return end
        if array[target] == item:
            return target
        elif temp_list[0] == array[target]:
            # Going Right
            start = target
            target = (target + end)//2
            end -= 1
        elif temp_list[0] == item:
            # Going Left
            end = target
            target = abs((target - start)//2)
            start += 1


TestCase_reverse = 54
TestCase_binary = ([1, 2, 3, 4, 5, 6, 7], 6)
if __name__ == "__main__":
    assert reverse(TestCase_reverse) == 45
    print(reverse(TestCase_reverse))
    assert binary_search(TestCase_binary[0], TestCase_binary[1]) == 5
    print(binary_search(TestCase_binary[0], TestCase_binary[1]))
