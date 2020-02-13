# import s (a string) and encode (a function)
from this import s
from codecs import encode

# decode s and assign to a variable called zen
zen = encode(s, "rot13")

# Explore string methods
zen.upper()
zen.lower()
zen.title()
zen.swapcase()

# Obtain a list of words and line from zen
word_list = zen.split()
line_list = zen.splitlines()

# Count characters, words, and lines
len(zen)
len(word_list)
len(line_list)

# Count a specific word (better) in zen 
zen.count("better")
word_list.count("better")

# Convert to uppercase, get the last word
zen.upper().split().pop()

(zen
 .upper()
 .split()
 .pop()
)
