import time


def Fibonacci(idx):  # recursion Fibonacci
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx - 1) + Fibonacci(idx - 2)


def fibonacci(idx):  # iteration Fibonacci
    seq = [0, 1]
    for i in range(idx):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]


recursion = time.time()
print("Recursion - " + str(Fibonacci(30)))
print("Speed of Recursion method: " + str(time.time() - recursion))

iteration = time.time()
print("Iteration - " + str(fibonacci(30)))
print("Speed of Iteration method: " + str(time.time() - iteration))
