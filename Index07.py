def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s)-1==n:
        return s[n]
    else:
        return False
x = main("python",5)
print(x)
