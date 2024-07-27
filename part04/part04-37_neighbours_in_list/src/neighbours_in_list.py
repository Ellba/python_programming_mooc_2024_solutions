# Write your solution here
def longest_series_of_neighbours(l1):
    longest = 1
    result = 1
    print(range(1, len(l1))) 
    for i in range(1, len(l1)):
        if abs(l1[i-1]-l1[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
    return longest
        
    # return [l1[i:i + 2] for i in range(0, len(l1), 2)]



if __name__ == "__main__":
    # longest_series_of_neighbours()
    print(longest_series_of_neighbours([1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]))