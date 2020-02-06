'''Code Using Division'''
def Mult_Division(arr):
    for i in range(len(arr)):
        Multiplication = Multiplication * arr[i]
    for i in range(len(arr)):
        M = Multiplication // arr[i]
        arr[i] = M
    return arr
'''Code without using Division '''
def Product(arr):
    temp = 1
    n = len(arr)
    i = 1
    if n == 1:
        return 0
    product = [1 for i in range(n)]
    #Multiplying left side elements of the specified index
    for i in range(n):
        product[i] = temp
        temp *= arr[i]
    #Multiplying right side elements of the specified index
    temp = 1
    for i in range(n-1,-1,-1):
        product[i] *= temp
        temp *= arr[i]
    #printing the product array
    return product
n = int(input("Enter the Length of the Array"))
Array = list(map(int,input().strip().split()))[:n]
print(Product(Array))
