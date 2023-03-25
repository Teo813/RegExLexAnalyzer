#Mateo's Lexical Analyzer

#Addition Operation +
#Subtraction Operation -
#Multiplication Operation *
#Division Operation /
#Modulo Operation %
#Left Grouping Symbol (
#Right Grouping Symbol )
#Assignment operation =
#Equals Operation ==
#Less than operation <
#Less than or equal to operation <=
#Greater than operation >
#Greater than or equal to operation <=
#Logical and operation &&
#Logical or operation ||
#Variable identifiers [a-zA-Z_][a-zA-Z0-9_]*
#integer literals \d+
#floating point literals \d+\.\d+

import re

# Define the token types
token_types = [
    ("ADD", r"\+"),
    ("SUB", r"-"),
    ("MUL", r"\*"),
    ("DIV", r"/"),
    ("MOD", r"%"),
    ("LPAR", r"\("),
    ("RPAR", r"\)"),
    ("ASSIGN", r"="),
    ("EQUALS", r"=="),
    ("LT", r"<"),
    ("LTE", r"<="),
    ("GT", r">"),
    ("GTE", r">="),
    ("AND", r"&&"),
    ("OR", r"\|\|"),
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("INT", r"\d+"),
    ("FLOAT", r"\d+\.\d+")
]

# Define the lexer
def lexer(text):
    tokens = []
    while text:
        # Ignore whitespace
        if text[0].isspace():
            text = text[1:]
            continue
        match = None
        for token_type, pattern in token_types:
            match = re.match(pattern, text)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                text = text[len(value):]
                break
        if not match:
            raise ValueError(f"Invalid character: {text[0]}")
    return tokens

# Read input from file
with open("sampleMath.txt") as f:
    text = f.read()

# Run the lexer on the input text
tokens = lexer(text)

# Print the resulting tokens
print(tokens)
