def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)==5:
        return int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4])
x = main("12345")
print(x)