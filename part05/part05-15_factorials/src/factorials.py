# Write your solution here
import math
def factorials(n: int):
    result = {}
    for i in range(1,n+1):
        result[i] = math.factorial(i)
    return result

if __name__ == "__main__":
    k = factorials(1)
    print(k[1])
    print(k[3])
    print(k[5])
    # factorials()