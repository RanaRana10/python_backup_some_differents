import re

def find_numbers_using_regex(text):
    """
    Finds all numbers (integers and decimals) in a string using regular expressions.
    
    Args:
    - text (str): The input string to search for numbers.
    
    Returns:
    - list: A list of numbers found in the string.
    """
    return list(map(float, re.findall(r'\d+\.\d+|\d+', text)))

def find_numbers_using_split(text):
    """
    Finds all integer numbers in a string by splitting the string.
    
    Args:
    - text (str): The input string to search for numbers.
    
    Returns:
    - list: A list of integer numbers found in the string.
    """
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers

# Example usage
str1 = "There are 21 oranges, 13 apples 8.7 and 18 Bananas in the basket"
print("Using regex:", find_numbers_using_regex(str1))

str2 = "There are 21 oranges, 13 apples and 18 Bananas 909 in the basket"
print("Using split:", find_numbers_using_split(str2))
