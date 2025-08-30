# Python Examples

This directory contains Python code examples and utility functions that demonstrate various programming concepts and techniques.

## Files

### `string_reverse.py`

A comprehensive implementation of string reversal functions in Python, showcasing multiple approaches:

#### Functions Available:

1. **`reverse_string(text)`** - Main function (uses built-in slicing)
2. **`reverse_string_builtin(text)`** - Uses Python's slicing notation `[::-1]`
3. **`reverse_string_loop(text)`** - Uses a for loop to build the reversed string
4. **`reverse_string_recursive(text)`** - Uses recursion to reverse the string
5. **`reverse_string_join(text)`** - Uses `reversed()` function with `join()`

#### Usage Examples:

```python
from string_reverse import reverse_string

# Basic usage
result = reverse_string("Hello, World!")
print(result)  # Output: !dlroW ,olleH

# Empty string
result = reverse_string("")
print(result)  # Output: 

# Single character
result = reverse_string("a")
print(result)  # Output: a
```

#### Running the Script:

You can run the script directly to see a demonstration of all methods:

```bash
python string_reverse.py
```

This will display:
- Comparison of all reversal methods with various test strings
- Interactive examples showing palindrome detection
- Performance demonstrations

#### Error Handling:

All functions include proper error handling and will raise a `TypeError` if the input is not a string:

```python
try:
    result = reverse_string(123)  # This will raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

#### Method Comparison:

- **Built-in slicing (`[::-1]`)**: Most efficient and Pythonic
- **For loop**: Educational, shows manual string building
- **Recursive**: Demonstrates recursion concept (watch out for deep recursion)
- **Join with reversed()**: Alternative built-in approach

Choose `reverse_string()` or `reverse_string_builtin()` for production code as they are the most efficient.