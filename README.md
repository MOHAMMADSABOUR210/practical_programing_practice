# Simple Python Problem Solutions

This repository contains solutions to three basic programming problems written in Python. Each file solves a different type of problem using string manipulation, number logic, or decoding techniques. These are excellent practice exercises for beginners.

## Problems and Files

### 1. `MAYDAY.py`
**Problem:**  
Given a string consisting of mixed words, letters, numbers (written as their English names), and dashes (also spelled out), decode it as follows:
- Words like "seven", "nine", or "dash" should be converted to their digit or character form.
- All other words are replaced by the first letter of the word.

**Example:**  
Input: `"zero dash one two apple"`  
Output: `"0-12a"`

### 2. `Dizzy.py`
**Problem:**  
Given a string with encoded characters like `"T4"`, decode it using a custom rule to recognize and translate those parts into the original string.

**Example:**  
Input: `"H2e3l1o"` (encoding rule applied)  
Output: `"Hello"` (depends on the defined logic in the solution)

### 3. `digit_3.py`
**Problem:**  
Find all three-digit numbers that:
- Are divisible by 3
- Are made using **only two different digits**

**Example Output:**  
A list like `[111, 112, 121, 122, ..., 999]` filtered to include only valid numbers.

## How to Run

Ensure Python 3 is installed, then run any of the scripts with:

```bash
python MAYDAY.py
python Dizzy.py
python digit_3.py
```

## Purpose

These problems are designed to strengthen your skills in:
- String processing
- Conditional logic
- Working with numbers and constraints

They’re perfect for beginners and intermediate coders looking to sharpen their problem-solving abilities.

## License

Free to use for learning and educational purposes.