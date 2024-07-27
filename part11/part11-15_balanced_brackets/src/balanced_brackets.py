
def balanced_brackets(my_string: str):
    def helper(s):
        if not s:
            return True
        if len(s) < 2 or (s[0] == '(' and s[-1] != ')') or (s[0] == '[' and s[-1] != ']'):
            return False
        return helper(s[1:-1])

    cleaned_string = "".join([char for char in my_string if char in '()[]'])
    return helper(cleaned_string)


if __name__ == "__main__":
    # ok = balanced_brackets("([([])])")
    # print(ok)

    # ok = balanced_brackets("(python version [3.7]) please use this one!")
    # print(ok)

    # this is no good, the closing bracket doesn't match
    # ok = balanced_brackets("(()]")
    # print(ok)

    # different types of brackets are mismatched
    # ok = balanced_brackets("([bad egg)]")
    ok = balanced_brackets("()")
    print(ok)