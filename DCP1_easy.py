'''
We are here to learn a simple programming question which can return true if any sequence of two numbers is equal to the required sum.
Example: array = [1,2,3,4,5] Sum = 6 since 1+5 = 6,2+4 = 6 we are going to return true.

Naive Approach(Algorithm):

for i in range(0,length(array):
    for j in range(1,length(array)):
        if array[i] + array[j] == sum:
              return true
        else:
              return false
Here We have
Time complexity = O(n^2)
Space Complexity = O(n) //Since for storing array elements.

Using hash tables:
def Summed(array,Sum):
    dictionary = {}
    for i in range(length(array)):
        if Sum - array[i] not in dictionary:
            dicitonary[i] = Sum - array[i]
        else:
            return true

Here we have
Time Complexity = O(n)
Space Complexity = O(n) // for dictionary elements.
'''
def Summed(array,Sum):
    dictionary = {}
    position = 0
    while position < len(array):
        if Sum - array[position] not in dictionary:
            dictionary[array[position]] =  position
            position += 1
        else:
            return True
    return False
Array = [15,10,3,1]
Sum = 11
print(Summed(Array,Sum))
