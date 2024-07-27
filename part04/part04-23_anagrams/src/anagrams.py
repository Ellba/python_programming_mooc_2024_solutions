# Write your solution here

def anagrams(str1: str, str2: str):
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    anagrams("test", "tset")