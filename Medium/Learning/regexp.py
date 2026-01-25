import re

text = "Another vital part of the first pattern. Another vital part of the first pattern"

# re.search
if re.search("vital", text):
    print("found vital")

# re.findall
pattern = r"\bp\w*\b" # snag every word that begins with p
print(re.findall(pattern, text))
