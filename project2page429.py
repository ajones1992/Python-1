'''
Program: project2page429.txt
Author: Alex Jones
Date: 12/06/21
Purpose: Design a function that reverse the order of a list.
'''

def reverse(lyst):
    if len(lyst) % 2 == 1:
        middle = len(lyst) // 2
        count = 0
        i = 0
        j = 1
        swap = len(lyst)-j
        while i < (middle+1):
            if lyst[i] == lyst[swap]:
                j += 1
                i += 1
                swap = len(lyst)-j
            else:
                placeholder = lyst[i]
                lyst[i] = lyst[swap]
                lyst[swap] = placeholder
                j += 1
                i += 1
                swap = len(lyst)-j
                count += 1
        return lyst, count
    else:
        count = 0
        i = 0
        j = 1
        swap = len(lyst)-j
        while i <= (len(lyst) // 2 - 1):
            if lyst[i] == lyst[swap]:
                j += 1
                i += 1
                swap = len(lyst)-j
            else:
                placeholder = lyst[i]
                lyst[i] = lyst[swap]
                lyst[swap] = placeholder
                j += 1
                i += 1
                swap = len(lyst)-j
                count += 1
        return lyst, count

test = [1, 2, 3, 4, 5]
test2 = ['bob', 'steve', 'ron', 'beth']
test3 = [1,1,1]
test4 = ['bob','bob','bob']
test5 = [1, 2, 3, 4, 5, 1]

print(reverse(test))
print(reverse(test2))
print(reverse(test3))
print(reverse(test4))
print(reverse(test5))
print("This function is O(n/2) in every case.")
