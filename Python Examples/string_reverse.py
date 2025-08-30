"""
String Reverse Function Implementation

This module provides various methods to reverse a string in Python.
Each method demonstrates different approaches and techniques.
"""


def reverse_string_builtin(text):
    """
    Reverse a string using Python's built-in slicing notation.
    
    This is the most Pythonic and efficient way to reverse a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string_builtin("hello")
        'olleh'
        >>> reverse_string_builtin("Python")
        'nohtyP'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text[::-1]


def reverse_string_loop(text):
    """
    Reverse a string using a for loop.
    
    This method manually iterates through the string and builds
    the reversed version character by character.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string_loop("hello")
        'olleh'
        >>> reverse_string_loop("world")
        'dlrow'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    
    return reversed_text


def reverse_string_recursive(text):
    """
    Reverse a string using recursion.
    
    This method demonstrates a recursive approach to string reversal.
    Note: For very long strings, this might hit Python's recursion limit.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string_recursive("hello")
        'olleh'
        >>> reverse_string_recursive("abc")
        'cba'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(text) <= 1:
        return text
    
    # Recursive case: last character + reverse of the rest
    return text[-1] + reverse_string_recursive(text[:-1])


def reverse_string_join(text):
    """
    Reverse a string using reversed() function and join().
    
    This method uses Python's built-in reversed() function
    with str.join() to create the reversed string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Example:
        >>> reverse_string_join("hello")
        'olleh'
        >>> reverse_string_join("test")
        'tset'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(reversed(text))


# Main function that uses the most efficient method
def reverse_string(text):
    """
    Reverse a string (main function).
    
    This is the primary function that uses the most efficient
    method (slicing) to reverse a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Raises:
        TypeError: If input is not a string
        
    Example:
        >>> reverse_string("Hello, World!")
        '!dlroW ,olleH'
        >>> reverse_string("")
        ''
        >>> reverse_string("a")
        'a'
    """
    return reverse_string_builtin(text)


def demonstrate_all_methods():
    """
    Demonstrate all string reversal methods with example inputs.
    """
    test_strings = [
        "Hello, World!",
        "Python",
        "12345",
        "A man a plan a canal Panama",
        "",
        "a"
    ]
    
    methods = [
        ("Built-in slicing", reverse_string_builtin),
        ("For loop", reverse_string_loop),
        ("Recursive", reverse_string_recursive),
        ("Join with reversed()", reverse_string_join)
    ]
    
    print("String Reversal Demonstration")
    print("=" * 40)
    
    for test_string in test_strings:
        print(f"\nOriginal: '{test_string}'")
        for method_name, method_func in methods:
            try:
                result = method_func(test_string)
                print(f"{method_name:20}: '{result}'")
            except Exception as e:
                print(f"{method_name:20}: Error - {e}")


if __name__ == "__main__":
    # Run demonstration when script is executed directly
    demonstrate_all_methods()
    
    # Interactive examples
    print("\n" + "=" * 40)
    print("Interactive Examples:")
    print("=" * 40)
    
    examples = [
        "hello",
        "Python Programming",
        "12321",  # palindrome
        "racecar"  # palindrome
    ]
    
    for example in examples:
        reversed_str = reverse_string(example)
        is_palindrome = example.lower() == reversed_str.lower()
        print(f"'{example}' -> '{reversed_str}' (Palindrome: {is_palindrome})")