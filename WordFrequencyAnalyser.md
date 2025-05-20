## The problem covers (Strings, Lists, Tuples)
Write a Python function called **analyze_text(data: str)** that takes a string data as input and performs the following tasks:
1. Split the string into words. A word is defined as a sequence of alphabetic characters, and words should be considered case-insensitive (e.g., "Python" and "python" are the same).
2. Ignore all non-alphabetic characters.
3. Count the frequency of each unique word in the string.
4. Create a list of tuples where each tuple contains a word and its frequency, sorted in descending order of frequency. If two words have the same frequency, sort them alphabetically in ascending order.
5. Return the sorted list of tuples.

## Example
**Input**
`data = "Hello, world! Hello Python developers. Python is great, and hello to the world of Python!"`

**Output**
`[('hello', 3), ('python', 3), ('world', 2), ('and', 1),
    ('developers', 1), ('great', 1), ('is', 1), ('of', 1),
    ('the', 1), ('to', 1)]`

## Constraints:
1. The input string may contain punctuation and numbers, but only alphabetic words should be processed.
2. Words should be treated case-insensitively.
