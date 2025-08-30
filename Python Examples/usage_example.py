#!/usr/bin/env python3
"""
Example usage of the string_reverse module.

This script demonstrates how to import and use the string reversal functions
in your own Python projects.
"""

from string_reverse import (
    reverse_string,
    reverse_string_builtin,
    reverse_string_loop,
    reverse_string_recursive,
    reverse_string_join
)


def main():
    """Main function demonstrating various usage patterns."""
    
    print("String Reverse Function - Usage Examples")
    print("=" * 45)
    
    # Example 1: Basic usage
    print("\n1. Basic Usage:")
    text = "Hello, Python!"
    reversed_text = reverse_string(text)
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    
    # Example 2: Processing user input
    print("\n2. Interactive Example:")
    user_input = "Welcome to Python programming"
    print(f"Input: {user_input}")
    print(f"Output: {reverse_string(user_input)}")
    
    # Example 3: Checking for palindromes
    print("\n3. Palindrome Checker:")
    test_words = ["level", "hello", "radar", "python", "madam"]
    
    for word in test_words:
        reversed_word = reverse_string(word)
        is_palindrome = word.lower() == reversed_word.lower()
        status = "✓ Palindrome" if is_palindrome else "✗ Not a palindrome"
        print(f"{word:10} -> {reversed_word:10} {status}")
    
    # Example 4: Using different methods
    print("\n4. Comparing Different Methods:")
    test_string = "Python"
    methods = [
        ("Built-in (default)", reverse_string),
        ("Loop method", reverse_string_loop),
        ("Recursive method", reverse_string_recursive),
        ("Join method", reverse_string_join)
    ]
    
    for method_name, method_func in methods:
        result = method_func(test_string)
        print(f"{method_name:20}: {test_string} -> {result}")
    
    # Example 5: Error handling
    print("\n5. Error Handling:")
    invalid_inputs = [123, None, [], {}]
    
    for invalid_input in invalid_inputs:
        try:
            result = reverse_string(invalid_input)
            print(f"Input: {invalid_input} -> {result}")
        except TypeError as e:
            print(f"Input: {invalid_input} -> Error: {e}")
    
    # Example 6: Working with sentences
    print("\n6. Working with Sentences:")
    sentences = [
        "The quick brown fox",
        "Python is awesome!",
        "Programming is fun",
    ]
    
    for sentence in sentences:
        reversed_sentence = reverse_string(sentence)
        print(f"'{sentence}' -> '{reversed_sentence}'")


if __name__ == "__main__":
    main()