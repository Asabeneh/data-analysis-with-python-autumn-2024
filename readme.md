### Introduction to Python Programming

Python is a versatile and beginner-friendly programming language known for its simplicity and readability. It's widely used in various fields, such as web development, data science, automation, and artificial intelligence. This guide will walk you through setting up Python, running an interactive shell, installing Visual Studio Code (VS Code), and writing your first Python program: `"Hello World!"`.

#### 1. Installing Python

Before writing any Python code, you need to install Python on your computer. Follow these steps:

- **Step 1:** Go to the [official Python website](https://www.python.org/).
- **Step 2:** Click on the **Downloads** section and choose the version for your operating system (Windows, macOS, or Linux).
- **Step 3:** Run the downloaded installer.
    - For Windows users, during installation, make sure to check the box labeled **"Add Python to PATH"**. This makes running Python from the command line easier.
- **Step 4:** Verify the installation by opening a terminal (Command Prompt for Windows, or Terminal for macOS/Linux) and typing:

  ```bash
  python --version
  ```

  You should see the installed Python version printed.

#### 2. Open the Interactive Python Shell

Python comes with an interactive shell that allows you to run Python commands immediately. Here's how to open it:

- **Step 1:** Open your terminal or command prompt.
- **Step 2:** Type `python` (or `python3` on some systems) and hit **Enter**. This will start the Python shell.
  
You’ll see a prompt like this:

```python
Python 3.x.x (default, Mar 18 2021, 13:41:09)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

This is the Python interactive shell, where you can run Python commands directly. Try typing:

```python
print('Hello World!')
```

It should print:

```python
Hello World!
```

You’ve just written your first Python program in the interactive shell!

#### 3. Installing Visual Studio Code (VS Code)

To write more complex Python programs, you’ll want to use a code editor like Visual Studio Code (VS Code). Follow these steps to install and set up VS Code:

- **Step 1:** Go to the [Visual Studio Code website](https://code.visualstudio.com/).
- **Step 2:** Download the appropriate version for your operating system (Windows, macOS, or Linux).
- **Step 3:** Run the installer and follow the setup instructions.
- **Step 4:** Once installed, open VS Code.

#### 4. Setting Up Python in Visual Studio Code

Now, let's set up Python in VS Code.

- **Step 1:** Install the Python extension for VS Code:
    - Open VS Code and click on the **Extensions** icon (on the left-hand toolbar).
    - Search for "Python" and install the official Python extension by Microsoft.

- **Step 2:** Ensure VS Code is using the correct Python interpreter:
    - Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (macOS) to open the Command Palette.
    - Type `Python: Select Interpreter` and choose the Python version you installed.

#### 5. Writing Your First Python Program in VS Code

Let’s write the same `"Hello World!"` program in VS Code.

- **Step 1:** Create a new file in VS Code by selecting **File > New File**.
- **Step 2:** Save the file with a `.py` extension (e.g., `hello.py`).
- **Step 3:** Write the following code in the file:

  ```python
  print('Hello World!')
  ```

- **Step 4:** Run the Python code:
    - You can run it directly within VS Code by pressing `Ctrl+F5` (Windows) or `Cmd+F5` (macOS).
    - Alternatively, open the terminal within VS Code (`Ctrl+` `) and type:
    
      ```bash
      python hello.py
      ```

You should see the output:

```bash
Hello World!
```

Congratulations! You've successfully set up Python, learned how to use the interactive shell, installed VS Code, and written your first Python program. This is just the beginning of your Python journey!

---
### Python Comments and the Print Function: Explanation and Documentation

In Python, comments are an essential part of writing clean and understandable code. Comments help both the programmer and others understand what the code is doing. Python supports two types of comments: **single-line comments** and **multiline comments**. In this document, we will explain these comment types and the `print()` function.

#### 1. Single-Line Comments

A **single-line comment** in Python begins with a hash symbol (`#`). Everything following the hash on that line is considered a comment and is ignored by the Python interpreter.

##### Example:
```python
# A hash symbol is a single line comment
# The purpose of a comment is to make our code readable and maintainable
```

In this example, both lines are comments and will not be executed. They exist to describe the purpose of the code that follows, helping the programmer understand what’s happening.

#### 2. The `print()` Function

The `print()` function is used to display output on the screen. It can take one or more arguments and print them, separated by spaces.

##### Example:
```python
print('Hello', 'World', 2024, 'Data Analysis with Python - Autumn 2024')
```

**Explanation:**
- This line of code prints four separate items: `'Hello'`, `'World'`, `2024`, and `'Data Analysis with Python - Autumn 2024'`.
- The `print()` function separates each of these inputs by a space and displays them in a single line:
  
  ```
  Hello World 2024 Data Analysis with Python - Autumn 2024
  ```

You can pass any combination of data types (strings, integers, etc.) to `print()`, and it will display them on the console.

#### 3. Multiline Comments (Docstrings)

In Python, you can create **multiline comments** by enclosing the comment text within triple quotes (`'''` or `"""`). These are often used for longer explanations or documentation. Multiline comments are sometimes referred to as **docstrings**, especially when used inside functions or classes to document their purpose.

##### Example:
```python
'''
A multiline comment allows us to write a comment
on several lines and
sometimes it can be used as good documentation
'''
```

or 

```python
"""
A multiline comment allows us to write a comment
on several lines and
sometimes it can be used as good documentation
"""
```

**Explanation:**
- Both single quotes (`'''`) and double quotes (`"""`) can be used to write multiline comments. The choice between them is a matter of preference and style.
- These multiline comments are helpful for providing detailed explanations of code or for documenting larger sections.

### Summary

- **Single-line comments** (`#`) are useful for short, concise comments.
- **Multiline comments** (`'''` or `"""`) are helpful for more extensive explanations or documentation.
- The `print()` function is a fundamental tool for displaying outputs, allowing multiple arguments separated by spaces to be printed in a single line.

By using comments effectively, you can make your code more readable and maintainable, while the `print()` function provides an easy way to output text and other data types during the execution of your Python programs.

---
### Python Built-in Functions: Explanation and Documentation

In Python, functions are a key tool for writing reusable and modular code. There are two main types of functions in Python: **built-in functions** and **custom functions**.

- **Built-in Functions**: Predefined functions that are available in Python without the need to import any external modules.
- **Custom Functions**: Functions defined by the user to solve specific problems or perform specific tasks.

This document focuses on various **built-in functions** in Python, including how to use them and what they do.

---

### 1. The `print()` Function

The `print()` function is one of the most commonly used built-in functions in Python. It displays the output of any data type (integers, strings, lists, etc.) on the screen.

```python
print(10, type(10))
print(9.81, type(9.81))
print('Asabeneh Yetayeh', 'Finland', 'Helsinki', 250, ['HTML', 'CSS', 'JS'], sep=', ')
```

**Explanation**:
- `print()` takes any number of arguments and prints them, separated by spaces by default. You can customize the separator using the `sep` parameter.
- `type()` shows the type of the data passed to it, like integer, float, string, etc.

Output:
```
10 <class 'int'>
9.81 <class 'float'>
Asabeneh Yetayeh, Finland, Helsinki, 250, ['HTML', 'CSS', 'JS']
```

---

### 2. The `len()` Function

The `len()` function returns the number of items in a sequence (like strings, lists, etc.).

```python
print(len('cat'))
print(len('Finland'))
```

**Explanation**:
- `len()` works on any sequence type such as strings, lists, tuples, etc., and returns the length.

Output:
```
3
7
```

---

### 3. The `type()` Function

The `type()` function returns the type of a given object.

```python
print(10, type(10))
print(1 + 4j, type(1 + 4j))
```

**Explanation**:
- `type()` shows the data type of any object, whether it's an integer, float, complex number, string, etc.

---

### 4. The `input()` Function

The `input()` function is used to take input from the user.

```python
name = input('Enter your name: ')
print('Hello, ' + name)
```

**Explanation**:
- `input()` takes a string as a prompt and waits for the user to input text. The input is always returned as a string.

---

### 5. The `range()` Function

The `range()` function generates a sequence of numbers, which can be converted into a list or iterated through.

```python
print(list(range(0, 10)))
print(list(range(0, 101, 2)))
```

**Explanation**:
- `range(start, end, step)` generates a sequence of numbers from `start` to `end-1`, with a step increment of `step`.
- You can convert a range object into a list using `list()`.

---

### 6. Data Types and Built-in Functions

Python provides various built-in functions for working with data types like **lists**, **sets**, **dictionaries**, and **tuples**.

```python
print(set(['English', 'French', 'Finnish', 'Swedish', 'Finnish']))
print(dict(name='Asab', age=250))
```

**Explanation**:
- `set()` creates a set, removing duplicates.
- `dict()` creates a dictionary with key-value pairs.

---

### 7. The `abs()`, `min()`, `max()`, and `sum()` Functions

These built-in functions perform basic mathematical operations.

```python
print(abs(-5))
print(min(-2, 10, 5, 20))
print(max(-2, 10, 5, 20))
print(sum([1, 2, 3, 4, 5]))
```

**Explanation**:
- `abs()` returns the absolute value.
- `min()` and `max()` return the smallest and largest values, respectively.
- `sum()` adds up all elements in a list.

---

### 8. The `enumerate()` Function

The `enumerate()` function adds a counter to an iterable (like a list) and returns it as an enumerate object.

```python
countries = ['Finland', 'Sweden', 'Norway']
print(list(enumerate(countries)))
```

**Explanation**:
- `enumerate()` is useful when you need to iterate over a list while keeping track of the index.

---

### 9. The `dir()` Function

The `dir()` function returns a list of all attributes and methods available for an object.

```python
print(dir('hello'))
```

**Explanation**:
- `dir()` helps you explore the methods associated with a particular object, such as a string, list, or function.

---

### Summary

- Python's built-in functions like `print()`, `len()`, `input()`, and `range()` are powerful tools for solving common problems and tasks.
- Functions like `abs()`, `min()`, `max()`, `sum()`, and `enumerate()` are useful for working with numbers and sequences.
- Python's data types—lists, sets, dictionaries, and tuples—can be manipulated easily using functions like `list()`, `set()`, `dict()`, etc.

Understanding and effectively using these built-in functions is a fundamental part of programming in Python.
---
### Python Data Types: Explanation and Documentation

In Python, **data types** define the kind of data that can be stored and manipulated within a program. This document provides an overview of Python's common data types, along with examples to demonstrate their usage.

---

### 1. Data Types in Python

The major data types in Python include:
- **Numbers**: Integer (`int`), floating-point (`float`), and complex (`complex`).
- **Booleans**: Logical values representing `True` or `False`.
- **Strings**: Text or sequence of characters.
- **List**: Ordered and mutable collection of items.
- **Set**: Unordered collection of unique items.
- **Tuple**: Ordered and immutable collection of items.
- **Dictionary**: Collection of key-value pairs.

---

### 2. Numbers

Python supports three types of numbers: integers, floats, and complex numbers.

```python
# Integers and Floats
print(10, 100, -10, -5, 0)
print(9.81, 2.77, 3.14, 36.7)

# Complex Numbers
print(1 + 2j, 4 + 3j, 4 + 5j, 10j)
```

**Explanation**:
- **Integers** are whole numbers, positive or negative.
- **Floats** represent numbers with a decimal point.
- **Complex numbers** have both a real part and an imaginary part, denoted by `j` for the imaginary unit.

---

### 3. Booleans

Booleans in Python are represented by the two values `True` and `False`, and are often used in logical operations.

```python
# Boolean values
print(True, False)

# Boolean comparison
print(4 > 3, -1 < 0)
print(len('Finland') > len('Sweden'))
```

**Explanation**:
- Booleans can be used to evaluate expressions and are the result of comparison operators such as `>`, `<`, `==`, etc.
- `True` and `False` represent the two possible outcomes of a boolean expression.

---

### 4. Strings

A **string** in Python is a sequence of characters enclosed within single, double, or triple quotes. Strings are used to store text data.

```python
# String manipulations
course = 'Data analysis with Python'
print(len(course))
print(course.upper())
print(course.lower())
print(course.swapcase())
print(course.title())
print(course.split())
print(course.startswith('Data'))
print('Py' in course)
print('land' in 'Finland')
```

**Explanation**:
- **`len()`**: Returns the length of the string.
- **`upper()`, `lower()`, `swapcase()`, `title()`**: These methods change the casing of the string.
- **`split()`**: Splits the string into a list based on whitespace or specified delimiter.
- **`startswith()`**: Checks if the string starts with a specified prefix.
- **Membership operators** (`in`): Check if a substring exists in the string.

---

### 5. String Formatting

Python provides various ways to format strings. One of the most common ways is by using **f-strings** for inline expressions.

```python
# Using f-strings for string formatting
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = f'{first_name} {last_name}'
print(full_name)

# Using f-strings for mathematical operations
a = 3 
b = 4
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ^ {b} = {a ** b}')
print(f'{a} // {b} = {a // b}')
```

**Explanation**:
- **f-strings**: Allow the inclusion of variables and expressions inside a string by using curly braces `{}`.
- They make string formatting more readable and concise compared to older methods like `format()`.

---

### 6. Indexing Strings

Strings in Python are **indexed**, meaning each character can be accessed by its position (starting from 0).

```python
country = 'Finland'
print(country[0])
```

**Explanation**:
- The **index** allows you to access specific characters within a string.
- In this example, `country[0]` returns `'F'`, the first letter of the string.

---

### Summary

- Python supports several basic **data types**, including **numbers** (int, float, complex), **booleans** (True, False), and **strings**.
- Strings are one of the most versatile data types in Python, and they come with a wide array of methods for manipulation (e.g., `upper()`, `split()`, `startswith()`).
- **Booleans** are useful for logical operations, and **f-strings** simplify string formatting.
- Understanding how to work with these data types is fundamental to Python programming.

---
### Python Data Types: Explanation and Documentation

In Python, **data types** define the kind of data that can be stored and manipulated within a program. This document provides an overview of Python's common data types, along with examples to demonstrate their usage.

---

### 1. Data Types in Python

The major data types in Python include:
- **Numbers**: Integer (`int`), floating-point (`float`), and complex (`complex`).
- **Booleans**: Logical values representing `True` or `False`.
- **Strings**: Text or sequence of characters.
- **List**: Ordered and mutable collection of items.
- **Set**: Unordered collection of unique items.
- **Tuple**: Ordered and immutable collection of items.
- **Dictionary**: Collection of key-value pairs.

---

### 2. Numbers

Python supports three types of numbers: integers, floats, and complex numbers.

```python
# Integers and Floats
print(10, 100, -10, -5, 0)
print(9.81, 2.77, 3.14, 36.7)

# Complex Numbers
print(1 + 2j, 4 + 3j, 4 + 5j, 10j)
```

**Explanation**:
- **Integers** are whole numbers, positive or negative.
- **Floats** represent numbers with a decimal point.
- **Complex numbers** have both a real part and an imaginary part, denoted by `j` for the imaginary unit.

---

### 3. Booleans

Booleans in Python are represented by the two values `True` and `False`, and are often used in logical operations.

```python
# Boolean values
print(True, False)

# Boolean comparison
print(4 > 3, -1 < 0)
print(len('Finland') > len('Sweden'))
```

**Explanation**:
- Booleans can be used to evaluate expressions and are the result of comparison operators such as `>`, `<`, `==`, etc.
- `True` and `False` represent the two possible outcomes of a boolean expression.

---

### 4. Strings

A **string** in Python is a sequence of characters enclosed within single, double, or triple quotes. Strings are used to store text data.

```python
# String manipulations
course = 'Data analysis with Python'
print(len(course))
print(course.upper())
print(course.lower())
print(course.swapcase())
print(course.title())
print(course.split())
print(course.startswith('Data'))
print('Py' in course)
print('land' in 'Finland')
```

**Explanation**:
- **`len()`**: Returns the length of the string.
- **`upper()`, `lower()`, `swapcase()`, `title()`**: These methods change the casing of the string.
- **`split()`**: Splits the string into a list based on whitespace or specified delimiter.
- **`startswith()`**: Checks if the string starts with a specified prefix.
- **Membership operators** (`in`): Check if a substring exists in the string.

---

### 5. String Formatting

Python provides various ways to format strings. One of the most common ways is by using **f-strings** for inline expressions.

```python
# Using f-strings for string formatting
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = f'{first_name} {last_name}'
print(full_name)

# Using f-strings for mathematical operations
a = 3 
b = 4
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ^ {b} = {a ** b}')
print(f'{a} // {b} = {a // b}')
```

**Explanation**:
- **f-strings**: Allow the inclusion of variables and expressions inside a string by using curly braces `{}`.
- They make string formatting more readable and concise compared to older methods like `format()`.

---

### 6. Indexing Strings

Strings in Python are **indexed**, meaning each character can be accessed by its position (starting from 0).

```python
country = 'Finland'
print(country[0])
```

**Explanation**:
- The **index** allows you to access specific characters within a string.
- In this example, `country[0]` returns `'F'`, the first letter of the string.

---

### Summary

- Python supports several basic **data types**, including **numbers** (int, float, complex), **booleans** (True, False), and **strings**.
- Strings are one of the most versatile data types in Python, and they come with a wide array of methods for manipulation (e.g., `upper()`, `split()`, `startswith()`).
- **Booleans** are useful for logical operations, and **f-strings** simplify string formatting.
- Understanding how to work with these data types is fundamental to Python programming.

---

### Python Conditional Statements and Pattern Matching

This Python code demonstrates basic conditional statements (`if`, `elif`, `else`) and introduces a newer pattern-matching approach (`match-case`) for handling specific conditions, often preferred in Python 3.10 and later.

#### Code Breakdown and Explanation

1. **Checking If a Number Is Positive, Negative, or Zero:**

```python
a = 5

if a > 0:
    print('The number is positive')
elif a < 0:
    print('The number is negative')
else:
    print('the number is zero')
```

**Explanation:**
- This block of code checks whether the variable `a` is positive, negative, or zero using `if`, `elif`, and `else` statements.
- The `if` condition checks if the number is greater than 0. If true, it prints `"The number is positive"`.
- If the number isn't positive, the `elif` condition checks if it's negative. If true, it prints `"The number is negative"`.
- If neither of the two conditions is true, the `else` statement is executed, printing `"The number is zero"`.

2. **Checking If It’s Raining:**

```python
is_raining = False 

if is_raining:
    print('Go out with an umbrella')
else:
    print('Go out freely it is a shinny day!')
```

**Explanation:**
- This section checks the Boolean value `is_raining`.
- If `is_raining` is `True`, it advises going out with an umbrella.
- If `is_raining` is `False`, it prints a message suggesting going out freely because it’s a sunny day.

3. **Weather Conditions Using `if-elif-else`:**

```python
weather = input('What is the weather today? ').lower()

if weather == 'rainy':
    print('Go with an unbrella or a raincoat')
elif weather == 'cloudy':
    print('It may rain and consider a raincoat')
elif weather == 'snowy':
    print('It may be slippery')
elif weather == 'foggy':
    print('Visiblity might be hindered')
elif weather == 'sunny':
    print('It is a great day to go to the beach')
else:
    print('No one knows about the weather')

print('test it')

```

**Explanation:**
- This commented-out section (enclosed in triple quotes) takes the user's input for the weather and performs multiple checks using `if-elif-else`.
- Based on the weather condition provided, it prints appropriate advice for going outside.

4. **Weather Conditions Using `match-case`:**

```python
weather = input('What is the weather today? ').lower()
match weather:
    case 'rainy':
        print('Go with an unbrella or a raincoat')
    case 'cloudy':
        print('It may rain and consider a raincoat')
    case 'snowy':
        print('It may be slippery')
    case 'foggy':
        print('Visiblity might be hindered')
    case 'sunny':
        print('It is a great day to go to the beach')
    case _:
        print('No one knows about the weather')
```

**Explanation:**
- This block uses the `match-case` structure, introduced in Python 3.10, which provides a more efficient and readable way to handle multiple conditions, replacing a chain of `if-elif-else` statements.
- The `match` keyword checks the value of the `weather` variable and matches it against specific cases (`'rainy'`, `'cloudy'`, etc.).
- If no match is found, the default case (`case _`) is executed, printing `"No one knows about the weather"`.

#### Key Takeaways:
- **Conditional Statements (`if-elif-else`)**: Useful for checking multiple conditions and executing different blocks of code based on those conditions.
- **Pattern Matching (`match-case`)**: A more modern and efficient way to handle conditions that involve multiple specific cases, improving readability, especially for many branches.

This code offers a foundational approach to handling conditional logic in Python, with examples using both traditional and modern constructs.

### String Operations Documentation

#### Overview:
- A string is a sequence of characters enclosed within single, double, or triple quotes.
- This documentation illustrates various string operations, slicing, methods, and formatting using Python.

#### Example: Basic String Declaration and Operations
```python
letter = 'a'
print(type(letter), len(letter))  # Output: <class 'str'> 1

alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets, len(alphabets))  # Output: 'abcdefghijklmnopqrstuvwxyz', 26
print(list(alphabets))  # Converts the string into a list of characters
```

#### String Indexing:
- Python strings support indexing, allowing access to individual characters by their position.

```python
lang = 'Python'
print(lang[0])  # Output: 'P'
print(lang[-1])  # Output: 'n'
```

#### String Slicing:
- Slicing allows for extracting a portion of the string.

```python
print(lang[0:2])  # Output: 'Py' (slices from index 0 to 2, not including index 2)
print(lang[-4:-1])  # Output: 'tho' (slices from index -4 to -1)
```

#### String Methods:
Python provides a variety of string methods for common tasks:

- **String Methods List**:
  - `'capitalize'`, `'upper'`, `'lower'`, `'title'`, `'strip'`, `'replace'`, `'find'`, `'split'`, `'join'`, `'startswith'`, `'endswith'` etc.

```python
txt = 'Python for everyone'
print(txt.upper())  # Output: 'PYTHON FOR EVERYONE'
print(txt.lower())  # Output: 'python for everyone'
print(txt.capitalize())  # Output: 'Python for everyone'
```

#### String Formatting:
- Python provides several ways to format strings:

1. **Using `+` operator**:
   ```python
   full_name = first_name + ' ' + last_name
   print(full_name)  # Concatenates strings
   ```

2. **Using `format()`**:
   ```python
   print('I am {} {}. I am {} years old.'.format(first_name, last_name, age))
   ```

3. **Using f-strings**:
   ```python
   formated_string = f'I am {first_name} {last_name}. I teach {language}.'
   print(formated_string)
   ```

#### Working with DNA Sequence (String Operations):
- Count the occurrences of specific characters in a DNA string and calculate their frequency.

```python
dna = '''CTAGCAAACTGCTGAT...'''  # (trimmed for brevity)
total = len(dna)
a = dna.count('A')
c = dna.count('C')
t = dna.count('T')
g = dna.count('G')
print(a / total, c / total, t / total, g / total)  # Output: Frequencies of A, C, T, G
```

#### Additional Examples:
- **String Replacement**:
   ```python
   print('I love people'.replace('love', 'like'))  # Output: 'I like people'
   ```

- **String Searching**:
   ```python
   txt = 'Python for everyone'
   print(txt.find('y'))  # Output: 1 (position of first 'y')
   print(txt.index('P'))  # Output: 0
   ```

#### Handling Large Texts:
- A sample speech from Donald Trump is processed by splitting it into words, converting them to lowercase, and removing punctuation.
- Then, unique words are identified using a set.

```python
donald_speech = '''Chief Justice Roberts, President...'''  # (trimmed for brevity)
words = donald_speech.lower().replace('–', ' ').replace('.', ' ').split()
unique_words = set(words)
print(len(unique_words))  # Output: Count of unique words
```

#### Conclusion:
This document covers the basics of string manipulation in Python, including indexing, slicing, methods, and formatting techniques. These concepts are essential for processing text data efficiently in Python.

# Working with Python Lists

This document explains basic operations and methods related to lists in Python, including list creation, accessing elements, and using built-in list methods.

## List Characteristics
- A list is a collection of items, which are **indexed** and **ordered**.
- Lists are **mutable**, meaning the elements can be changed after the list is created.

### 1. Creating an Empty List
You can create an empty list using the `list()` constructor.

```python
empty_list = list()
print(len(empty_list), empty_list)  # Outputs the length and the empty list
print(type(empty_list))  # Shows the type as <class 'list'>
print(dir(empty_list))  # Lists all methods available for the list object
```

### 2. Common List Methods
A list of some of the most common list methods in Python:

```python
lst_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### 3. Accessing List Elements
A list of numbers is created. You can access elements using their index.

```python
nums = [1, 2, 3, 4, 5]
print(nums, len(nums))  # Prints the list and its length
print(nums[0])  # Accesses the first element
print(nums[1])  # Accesses the second element
print(nums[4])  # Accesses the last element using its positive index

# Accessing the last element using negative indexing
print(nums[-1])

# Slicing the list
print(nums[1:4])  # Prints elements from index 1 to 3
print(nums[2:])  # Prints from index 2 to the end
print(nums[:3])  # Prints elements from the start to index 2
```

### 4. Modifying Lists
You can modify lists by adding, inserting, or removing elements.

#### Adding Elements
- **append()**: Adds an item to the end of the list.
- **extend()**: Adds multiple items to the list.
  
```python
# nums.append(6)
# nums.extend([7, 8, 9, 10])
```

#### Removing Elements
- **pop()**: Removes and returns an element at the given index. If no index is provided, it removes the last element.
- **del**: Deletes an element or a slice of the list.
  
```python
# nums.pop()  # Removes the last element
# nums.pop(0)  # Removes the first element
# del nums[4]  # Deletes the element at index 4
```

#### Inserting Elements
- **insert()**: Inserts an item at a given position.

```python
nums.insert(3, 333)  # Inserts 333 at index 3
nums.insert(6, 'the last item')  # Inserts a string at index 6
```

### 5. Counting and Reversing Elements
- **count()**: Returns the count of occurrences of a value in the list.
- **reverse()**: Reverses the order of the list.

```python
countries = ['Finland', 'Finland', 'Finland', 'Denmark', 'Norway', 'Finland', 'Finland', 'Sweden']
print(countries.count('Finland'))  # Counts how many times 'Finland' appears

copy_lst = nums.copy()  # Copies the list
copy_lst.reverse()  # Reverses the copied list
print(copy_lst)
```

### 6. Sorting Lists
Lists can be sorted in ascending or descending order.

- **sort()**: Sorts the list in place.
- **sorted()**: Returns a sorted copy of the list.

```python
new_num = [25, 20, 10, 3, 5, 0, 24]
print(sorted(new_num))  # Returns a sorted list in ascending order
print(sorted(new_num, reverse=False))  # Sorts without reversing
```

## Summary
This document covered the following list operations:
- Creating and accessing elements in lists.
- Adding, inserting, and removing elements.
- Counting and reversing elements.
- Sorting lists using `sorted()` and `sort()`.
```


# Repetitive Task Solver using Loops

In this script, we use loops to solve repetitive tasks such as iterating over lists of names and countries. This example demonstrates how to work with loops in Python.

## Code Overview

### 1. Generate a List of Numbers from 0 to 99
The first section generates and prints a list of numbers ranging from 0 to 99.

```python
print(list(range(100)))
```

### 2. Working with a List of Names
We have a list of names. The script prints the length of the list and identifies names with more than 6 characters.

```python
names = ['Diviya', 'Ankush', 'Gokul', 'Hannu', 'Diana', 'Markku', 'Riitta', 'Roope', 'Annika', 'Anna', 'Alzbetak', 'Asabeneh']
print(len(names))  # Prints the number of names in the list

for name in names:
    # Identifies and prints names with more than 6 characters
    if len(name) > 6:
        print('You got the longest name', name)
```

### 3. Working with a List of Countries
We have a list of countries. The script categorizes countries based on the presence of the word "land" and separates them into two lists.

#### List of Countries:

```python
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 
    'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 
    'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 
    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 
    'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 
    'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 
    'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 
    'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 
    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 
    'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 
    'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 
    'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 
    'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]
```

#### Filtering Countries Based on "land"

```python
countries_with_land = []
countries_without_land = []

for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
    else:
        countries_without_land.append(country)

# Prints countries containing "land"
print(countries_with_land)
# Prints countries without "land"
print(countries_without_land)
```

### Exercises
1. How can you find countries based on their initial letters from the [countries] (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) list? For each letter of the alphabet, how can you determine which countries start with that letter and count the total number of countries that begin with the specified letter?
2. Create a list of countries that consist of two or more words.
3. Find the middle country or countries from the country list
4. Create a list of sender emails from this [data](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/email_exchanges.txt)
5. Find the lexical(word) variety of this [text](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt). You also find the 10 most frequent words in the text, create word cloud, word frequencey bar graph or line graph.

```python
# Hint if letter is 'F' it will give Finland, Fiji and France
# 'F':['Finland', 'France', 'Fijie']
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(letter)
```
