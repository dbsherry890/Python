greeting = "good day, sir!"
capitalized_greeting = greeting.capitalize()
print(capitalized_greeting)
# Output: "Good day, sir!"

shout = "hear ye, hear ye!".upper()
print(shout)
# Output: "HEAR YE, HEAR YE!"   opposite is .lower()   - islower() & isupper() True/False

headline = "the chronicles of python".title()
print(headline)
# Output: "The Chronicles Of Python"

message = "    Clean me up!    "
trimmed_message = message.strip()
print(trimmed_message)
# Output: "Clean me up!"   There's also 'lstrip' and 'rstrip'

message = "Greetings, fellow coders!"
is_greeting = message.startswith("Greetings")
print(is_greeting)
# Output: True   - opposite is .endswith

message = "Alteration is essential."
new_message = message.replace("essential", "vital")
print(new_message)
# Output: "Alteration is vital."

# https://medium.com/@ernestasena/python-string-methods-unveiled-part-two-4595cc22d90b

sentence = "To be or not to be."
words = sentence.split()
print(words)  # Output: ['To', 'be', 'or', 'not', 'to', 'be.']

words = ["Python", "is", "awesome!"]
sentence = " ".join(words)
print(sentence)
# Output: "Python is awesome!"

message = "A needle in a haystack."
index = message.find("in")
print(index)
# Output: 2   - .rfind finds the last occurrence of the argument

message = "In pursuit of knowledge."
index = message.index("knowledge")
print(index)
# Output: 14   - Same as .find() but returns an exception instead of -1 if argument is not found

message = "How many times does 'times' appear?"
count = message.count("times")
print(count)
# Output: 2

alphanumeric = "Python42"
is_alphanumeric = alphanumeric.isalnum()
print(is_alphanumeric)
# Output: True   - .isalpha() True if only letters   - .isdigit() True if only numbers
# - .isnumeric() same as .isdigit?

# https://medium.com/@ernestasena/python-string-methods-unveiled-part-three-633978031169
text = "A grand journey awaits."
starts_with_grand = text.startswith("grand", 2, 10)
print(starts_with_grand)
# Output: True   - .endswith()
