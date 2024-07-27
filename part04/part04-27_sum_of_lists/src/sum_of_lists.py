# Write your solution here
def list_sum(list1: list, list2: list):
    results = []
    for i in range(len(list1)):
        results.append(list1[i] + list2[i])
 
    return results

# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)

if __name__ == "__main__":
    list_sum()