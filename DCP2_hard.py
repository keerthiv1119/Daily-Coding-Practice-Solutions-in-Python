Array = [3,2,1]
Multiplication = 1
for i in range(len(Array)):
    Multiplication = Multiplication * Array[i]
for i in range(len(Array)):
    M = Multiplication // Array[i]
    Array[i] = M
print(Array)
