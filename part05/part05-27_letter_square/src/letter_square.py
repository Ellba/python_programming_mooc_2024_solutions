# Write your solution here


# upper = list(string.ascii_uppercase) 
n = int(input("Layers: "))
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alphabets = "01234567891011121314151617"
# print(alphabets)
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between

# print("n =",n)
# print(k,'= k - the location of next character in alphabets')
# print(m,'= m - the number of characters in between')
# print(alphabets[n], "= alphabets[n]")
# print(alphabets[k], "= alphabets[k]")

while k >= 1:
    left = left + alphabets[k]
    # print(left, "= left")
    right = alphabets[k] + right
    # print(right, "= right")
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1

while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1
