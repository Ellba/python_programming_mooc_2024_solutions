# Write your solution here

def dict_of_numbers():
    twenty = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty",
    "seventy", "eighty", "ninety"]

    nums = list(range(0,100))

    main_dict = {nums[i]: twenty[i] for i in range(0, 20)}
    ninety = []
    
    for i in tens:
        ninety.append(i)
        for n in twenty[1:10]:       
            ninety.append(i+'-'+n)
    
    new_dict = dict(zip(nums[20:],ninety))

    main_dict.update(new_dict)
    return main_dict
    

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[89])
