def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s) < n:
        return False
    elif len(s)==n:
        return s[n-1]
    elif len(s)>n:
        return s[n-1]
x = main("pythonuz",9)
print(x)
