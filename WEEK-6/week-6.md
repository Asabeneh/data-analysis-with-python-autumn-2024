
- [Introduction to Map, Filter, and Reduce in Python](#introduction-to-map-filter-and-reduce-in-python)
  - [The `map()` Function](#the-map-function)
  - [The `filter()` Function](#the-filter-function)
  - [The `reduce()` Function](#the-reduce-function)
- [List Comprehension](#list-comprehension)
- [Real-World Applications: Country Data Processing](#real-world-applications-country-data-processing)
  - [Functional Programming Summary](#functional-programming-summary)
- [Python Error Types](#python-error-types)
  - [1. SyntaxError](#1-syntaxerror)
  - [2. IndentationError](#2-indentationerror)
  - [3. TypeError](#3-typeerror)
  - [4. NameError](#4-nameerror)
  - [5. IndexError](#5-indexerror)
  - [6. KeyError](#6-keyerror)
  - [7. ValueError](#7-valueerror)
  - [8. AttributeError](#8-attributeerror)
  - [9. ZeroDivisionError](#9-zerodivisionerror)
  - [10. ImportError / ModuleNotFoundError](#10-importerror--modulenotfounderror)
  - [11. FileNotFoundError](#11-filenotfounderror)
  - [12. RuntimeError](#12-runtimeerror)
  - [13. StopIteration](#13-stopiteration)
  - [14. OverflowError](#14-overflowerror)
  - [15. MemoryError](#15-memoryerror)
  - [16. AssertionError](#16-assertionerror)
  - [Handling Errors with `try-except` Blocks](#handling-errors-with-try-except-blocks)
  - [Python Errors summary](#python-errors-summary)
  - [File Handling in Python](#file-handling-in-python)
  - [Basic Concepts of File Handling](#basic-concepts-of-file-handling)
  - [Example: Reading and Counting Words in a File](#example-reading-and-counting-words-in-a-file)
    - [Code Example](#code-example)
  - [File Modes in Detail](#file-modes-in-detail)
  - [Best Practices for File Handling](#best-practices-for-file-handling)
  - [File handling Summary](#file-handling-summary)
  - [Self Study](#self-study)
- [Exercises](#exercises)

## Introduction to Map, Filter, and Reduce in Python

In Python, functional programming techniques such as `map()`, `filter()`, and `reduce()` allow us to process and transform collections of data efficiently. This reading material will guide you through the practical use of these functions with real-world examples.

### The `map()` Function

The `map()` function applies a given function to all items in an input list (or any iterable). It returns a map object, which can be converted into a list.

Example 1: Squaring Numbers

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, nums))
print(squares)  # Output: [1, 4, 9, 16, 25]
```

Example 2: Extracting Country Names
Here, we use `map()` to extract country names from a dataset.

```python
country_names = list(map(lambda country: country['name'], countries_data))
```

**Challenge:**
Using the same dataset, modify the `map()` function to extract country languages:

```python
languages = list(map(lambda country: country['languages'], countries_data))
```

To handle the list of lists, flatten the languages into one big list and convert it into a set for unique values:

```python
all_languages = []
for language in languages:
    all_languages.extend(language)

unique_languages = set(all_languages)
print(len(unique_languages))  # Count of unique languages
```

### The `filter()` Function

The `filter()` function is used to filter out elements from a list (or any iterable) based on a condition. It returns an iterator, which can be converted into a list.

Example 1: Filtering Even Numbers

```python
nums = [0, -5, 2, 4, 10, 3]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)  # Output: [0, 2, 4, 10]
```

Example 2: Filtering Countries Containing 'land'

```python
countries_with_land = list(filter(lambda country: 'land' in country['name'], country_names))
```

Example 3: Filtering European Countries

```python
european_countries = list(filter(lambda country: country['region'] == 'Europe', countries_data_big))
```

### The `reduce()` Function

The `reduce()` function, from the `functools` module, reduces a list to a single value by applying a function cumulatively to the items in the list. Unlike `map()` and `filter()`, `reduce()` does not return an iterable but a single result.

Example: Product of All Numbers

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda acc, cur: acc * cur, nums)
print(product)  # Output: 120
```

## List Comprehension

Python's list comprehensions offer a concise way to create lists. It's often more readable and faster than using `map()` or `filter()`.

Example 1: List Comprehension for Squaring Numbers

```python
squares = [num ** 2 for num in nums]
print('squares:', squares)  # Output: [1, 4, 9, 16, 25]
```

Example 2: Flattening a List of Lists

```python
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [n for sublist in lst for n in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Real-World Applications: Country Data Processing

Let's say we have a dataset of countries with properties like name, capital, and population. Using the techniques discussed, we can process this data efficiently.

Example: Extracting Country Details

```python
data = [{
    'name': country['name'], 
    'capital': country['capital'], 
    'population': country['population']
} for country in countries_data]
```

You can filter countries with 'land' in their name:

```python
land_countries = [country['name'] for country in countries_data if 'land' in country['name']]
```

### Functional Programming Summary

The functions `map()`, `filter()`, and `reduce()`, along with list comprehensions, are powerful tools for transforming and analyzing data in Python. These techniques allow for clean, readable, and efficient code, especially when dealing with large datasets.

## Python Error Types

Errors and exceptions are integral parts of programming. They occur when Python encounters a problem during the execution of a program. Understanding these errors and knowing how to handle them can significantly improve your coding skills. This guide will cover all the common Python error types and how to deal with them effectively.

---

### 1. SyntaxError

A **SyntaxError** arises when the code you write does not follow the proper syntax rules of Python. It usually happens when there are missing symbols (like parentheses or colons) or incorrect indentation.

Example 1:

```py
# Missing closing parenthesis
print("Hello, world"
```

Output:

```sh
SyntaxError: unexpected EOF while parsing
```

**How to fix:** Review the code to ensure that it follows proper Python syntax. Check for missing punctuation, mismatched parentheses, or incorrect indentation.

Example 2:

```python
# Missing colon at the end of the function definition
def greet()
    print("Hello, world!")
```

**Output:**

```sh
SyntaxError: invalid syntax
```

**How to fix:** Check your code for missing punctuation, such as colons, parentheses, or incorrect indentation.

---

### 2. IndentationError

Python relies on indentation to define the structure of code. An **IndentationError** occurs when the code is not properly indented.

Example:

```python
def greet():
print("Hello, world!")
```

**Output:**

```sh
IndentationError: expected an indented block
```

**How to fix:** Ensure that blocks of code within functions, loops, and conditionals are indented properly. Use consistent spaces (usually four) for indentation.

---

### 3. TypeError

A **TypeError** occurs when an operation or function is applied to an object of inappropriate type. For example, trying to perform arithmetic on a string and an integer will raise this error.

**Example:**

```python
num = 5
print("The number is: " + num)
```

**Output:**

```sh
TypeError: can only concatenate str (not "int") to str
```

**How to fix:** Ensure that operations are applied to compatible data types. In this case, convert the integer to a string before concatenating:

```python
print("The number is: " + str(num))
```

---

### 4. NameError

A **NameError** occurs when a variable or function name is used without being defined.

**Example:**

```python
print(message)
```

**Output:**

```sh
NameError: name 'message' is not defined
```

**How to fix:** Ensure that the variable or function is defined before using it. Check for typos or scope issues.

---

### 5. IndexError

An **IndexError** occurs when you try to access an element in a list or sequence using an invalid index.

**Example:**

```python
my_list = [1, 2, 3]
print(my_list[5])
```

**Output:**

```sh
IndexError: list index out of range
```

**How to fix:** Always check the length of the list before accessing an index. Use `len()` to ensure the index is within range:

```python
if len(my_list) > 5:
    print(my_list[5])
```

---

### 6. KeyError

A **KeyError** occurs when trying to access a key that does not exist in a dictionary.

**Example:**

```python
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['gender'])
```

**Output:**

```sh
KeyError: 'gender'
```

**How to fix:** You can use the `.get()` method to avoid `KeyError` or check if the key exists before accessing it:

```python
print(my_dict.get('gender', 'Key not found'))
```

---

### 7. ValueError

A **ValueError** occurs when a function receives an argument of the correct type but an inappropriate value.

**Example:**

```python
number = int("ten")
```

**Output:**

```sh
ValueError: invalid literal for int() with base 10: 'ten'
```

**How to fix:** Ensure the input is of the correct format and valid value. In this case, the string should contain digits to be converted to an integer:

```python
number = int("10")
```

---

### 8. AttributeError

An **AttributeError** occurs when you try to access or call an attribute or method that does not exist on an object.

**Example:**

```python
my_list = [1, 2, 3]
my_list.push(4)
```

**Output:**

```sh
AttributeError: 'list' object has no attribute 'push'
```

**How to fix:** Check the correct method or attribute for the object type. For lists, use `append()` instead of `push()`:

```python
my_list.append(4)
```

---

### 9. ZeroDivisionError

A **ZeroDivisionError** occurs when you attempt to divide a number by zero, which is mathematically undefined.

**Example:**

```python
result = 10 / 0
```

**Output:**

```sh
ZeroDivisionError: division by zero
```

**How to fix:** Ensure the denominator is not zero before performing division:

```python
if denominator != 0:
    result = numerator / denominator
else:
    print("Cannot divide by zero!")
```

---

### 10. ImportError / ModuleNotFoundError

An **ImportError** occurs when a module or specific function from a module cannot be imported. A **ModuleNotFoundError** is a subclass of `ImportError` and occurs when the Python interpreter cannot find the specified module.

**Example:**

```python
import non_existent_module
```

**Output:**

```sh
ModuleNotFoundError: No module named 'non_existent_module'
```

**How to fix:** Ensure the module is installed and the import statement is correct. You can install missing modules using pip:

```bash
pip install module_name
```

---

### 11. FileNotFoundError

A **FileNotFoundError** occurs when trying to access or open a file that does not exist.

**Example:**

```python
file = open('non_existent_file.txt', 'r')
```

**Output:**

```sh
FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
```

**How to fix:** Ensure the file path is correct, and the file exists before trying to open it. You can handle this error with a `try-except` block:

```python
try:
    file = open('file.txt', 'r')
except FileNotFoundError:
    print("File not found!")
```

---

### 12. RuntimeError

A **RuntimeError** is a generic error that occurs when something goes wrong during program execution but doesn't fit into any other specific error categories.

**Example:**

```python
raise RuntimeError("An unexpected error occurred!")
```

**Output:**

```sh
RuntimeError: An unexpected error occurred!
```

**How to fix:** Investigate the code that triggers the error. Runtime errors often require debugging and analyzing the program flow.

---

### 13. StopIteration

A **StopIteration** error occurs when the next item of an iterator is requested, but there are no more items to return. This typically happens in loops or when manually handling iterators.

**Example:**

```python
my_iterator = iter([1, 2, 3])
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  # No more items left
```

**Output:**

```sh
StopIteration
```

**How to fix:** Handle iterators properly using a loop that checks when the iteration is finished, such as a `for` loop, which handles `StopIteration` automatically.

---

### 14. OverflowError

An **OverflowError** occurs when a numerical calculation exceeds the limits for a numeric type.

**Example:**

```python
import math
result = math.exp(1000)
```

**Output:**

```sh
OverflowError: math range error
```

**How to fix:** Check your calculations to ensure they don't exceed the limits of the data type. For large numbers, use appropriate data types like `decimal` or handle the situation with approximate calculations.

---

### 15. MemoryError

A **MemoryError** occurs when the system runs out of memory to execute an operation, such as trying to create a massive data structure.

**Example:**

```python
huge_list = [1] * (10 ** 10)
```

**Output:**

```sh
MemoryError
```

**How to fix:** Optimize your code to use memory efficiently. Break down large tasks or use data structures with lower memory overhead.

---

### 16. AssertionError

An **AssertionError** occurs when an assertion statement, `assert`, fails. Assertions are used for debugging and testing.

**Example:**

```python
x = 5
assert x > 10, "x should be greater than 10"
```

**Output:**

```sh
AssertionError: x should be greater than 10
```

**How to fix:** Ensure that the condition in the `assert` statement is true. Assertions are mainly used for internal consistency checks.

---

### Handling Errors with `try-except` Blocks

To avoid abrupt program termination due to errors, you can use `try-except` blocks to handle exceptions gracefully.

**Example:**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

By handling exceptions, you can ensure your program behaves predictably even when errors occur.

---

### Python Errors summary

Python provides a wide range of error types to help programmers understand and resolve issues that arise during execution. Familiarity with these errors enables better debugging and the ability to write more reliable and resilient programs. Make use of `try-except` blocks

### File Handling in Python

File handling is an essential operation in programming that allows developers to work with files for tasks such as reading, writing, and modifying their contents. Python provides a simple yet powerful way to handle files using built-in functions and methods. Let's break down the key concepts with an example.

### Basic Concepts of File Handling

1. **Opening a File**:
   To open a file in Python, the `open()` function is used. This function requires two parameters:
   - The file name or path.
   - The mode in which you want to open the file.

   The common modes include:
   - `'r'`: Open a file for **reading**. This is the default mode.
   - `'w'`: Open a file for **writing** (creates a new file or truncates an existing file).
   - `'a'`: Open a file for **appending** data at the end.
   - `'r+'`: Open a file for both **reading and writing**.

2. **Reading from a File**:
   Python provides multiple ways to read the contents of a file:
   - `read()`: Reads the entire content of the file.
   - `readline()`: Reads one line at a time.
   - `readlines()`: Reads all lines and returns them as a list of strings.

3. **Writing to a File**:
   To write data to a file, you can use the `write()` or `writelines()` method. Be cautious when using write mode (`'w'`), as it will overwrite the file.

4. **Closing a File**:
   It is essential to close a file after its operations are completed using the `close()` method. This ensures that resources are freed and changes to the file are saved.

5. **With Statement**:
   Using the `with` statement is the recommended way to handle files in Python, as it automatically closes the file after the block of code is executed.

### Example: Reading and Counting Words in a File

Let's take an example to demonstrate file reading, processing, and word counting using Python.

Sample File Content (`notes.txt`):

```sh
Hello, welcome to file handling in Python.
File handling allows you to read and write files.
This is useful for text processing and data storage.
```

#### Code Example

```python
# Opening and reading a file
with open('notes.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list

total_words = []  # To store all words from the file

# Processing each line
for line in lines:
    # Strip leading/trailing spaces, convert to lowercase, and split into words
    words = line.strip().lower().replace(',', '').replace('.', '').split()
    total_words.extend(words)  # Add words to the total list

print("Words in the file:", total_words)
```

**Explanation**:

1. The file `notes.txt` is opened in read mode using the `with` statement.
2. `readlines()` is used to read all lines from the file and store them in the `lines` list.
3. Each line is processed by:
   - Stripping extra spaces with `strip()`.
   - Converting to lowercase using `lower()`.
   - Replacing punctuation (``,` and `.`) with empty strings.
   - Splitting the line into individual words using `split()`.
4. The resulting words are added to the `total_words` list, which is printed at the end.

**Output**:

```
Words in the file: ['hello', 'welcome', 'to', 'file', 'handling', 'in', 'python', 'file', 'handling', 'allows', 'you', 'to', 'read', 'and', 'write', 'files', 'this', 'is', 'useful', 'for', 'text', 'processing', 'and', 'data', 'storage']
```

Example: Writing to a File

To write data into a file, you can use the `write()` method. Here's an example:

```python
# Writing to a file
with open('output.txt', 'w') as file:
    file.write("This is a test file.\n")
    file.write("File handling in Python is simple and intuitive.\n")
```

This code will create a new file named `output.txt` (or overwrite it if it exists) and write the specified lines into it.

### File Modes in Detail

| Mode | Description                                                                 |
|------|-----------------------------------------------------------------------------|
| `'r'`  | Opens a file for reading (default mode). Raises an error if the file doesn't exist. |
| `'w'`  | Opens a file for writing. Creates a new file if it doesn't exist or truncates it if it does. |
| `'a'`  | Opens a file for appending. Creates a new file if it doesn't exist.        |
| `'r+'` | Opens a file for reading and writing. Raises an error if the file doesn't exist. |
| `'b'`  | Can be added to any mode for binary file handling (e.g., `'rb'`, `'wb'`). |

### Best Practices for File Handling

- **Use the `with` statement**: It ensures that the file is automatically closed after the block of code is executed, even if an error occurs.
- **Always close files**: If you don't use `with`, explicitly close the file using `close()`.
- **Check if the file exists**: If you're unsure whether a file exists or not, you can handle potential errors using `try-except` blocks.

Example with Error Handling

```python
try:
    with open('unknown_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
```

This code tries to open a file, but if it doesn't exist, it catches the `FileNotFoundError` and prints an error message.

### File handling Summary

File handling in Python is a straightforward process that plays a crucial role in many applications, such as reading configuration files, processing data, and logging. Understanding how to work with different file modes and operations like reading, writing, and closing files will make you proficient in handling files effectively in your programs.

### Self Study

[Regular expression](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md)

[Date and time in Python](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/16_Day_Python_date_time/16_python_datetime.md)

[NumPy](https://github.com/Asabeneh/NumPy/blob/main/NumPy.ipynb)

[Pandas](https://asabeneh.github.io/Pandas/)

[Matplotlib(Data Visualization)](https://github.com/Asabeneh/matplotlib/blob/master/Visualizations.ipynb)

## Exercises

1. Load the [cats] (<https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/cats.json>) by reading it. Use list comprehension and functional programming alternatively, and you can check your result from this [website](https://cats-paradise-f994f218e0ee.herokuapp.com/stats).
   1. Count the number of cat breeds
   2. Which country has the largest number of cat breeds
   3. Filter cat breeds highers than 5 Killograms
   4. What is the average weight of cat across all breeds based on this data?
   5. What is the average life span of cat across all breeds on this data?
   6. The data includes descriptions for each cat breed. Find the 10 most common words used in these descriptions.
   7. Which countries have one or more breeds in this dataset?
2. Data Visualization
   1. Create a word frequency table or line graph based on the cat breed descriptions.
   2. Create a word cloud of the cat breed descriptions.
   3. Create a bar graph showing the number of cat breeds by country of origin.
   4. Create a pie chart showing the percentage of cat breeds by country.
3. Fetch the cat breeds data from this [API](https://api.thecatapi.com/v1/breeds) and answer Q1. Install ```requests``` package using ```pip install requests```. Then, use this function to fetch the data:

    ```py
    def fetch_data(url):
        import requests
        response = requests.get(url)
        if url.endswith('.txt'):
            return response.content
        else:
            data = response.json()
            return data
    ```

[<< WEEK 4](../WEEK-4/week-5.md.md) | [WEEK 7 >>](../WEEK-7/week-7.md)
