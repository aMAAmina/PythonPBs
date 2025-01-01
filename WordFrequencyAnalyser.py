import re
from collections import Counter

def test_analyse_text():
    data = "Hello, world! Hello Python developers. Python is great, and hello to the world of Python!"
    ListOfTuples = analyze_text(data)
    ExpectedOutput = [ ('hello', 3), ('python', 3), ('world', 2), ('and', 1),
    ('developers', 1), ('great', 1), ('is', 1), ('of', 1),
    ('the', 1), ('to', 1)]
    if ListOfTuples != ExpectedOutput:
        print("Test failed!")
        print("Expected Output:", ExpectedOutput)
        print("Actual Output:", ListOfTuples)
        raise SystemExit(1)
    else:
        print(ListOfTuples)

def analyze_text(data: str):
    # Use regex to find all words in lowercase
    Words = re.findall(r'\b[a-z]+\b', data.lower())
    # Use Counter Obj (Counter class is a sub class of dict) to count word frequencies
    word_counts = Counter(Words)
    # Convert to a list of tuples and sort by frequency (descending) and alphabetically
    WordTuples = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    return WordTuples

def main():
    test_analyse_text()

if __name__ == "__main__":
    main()
