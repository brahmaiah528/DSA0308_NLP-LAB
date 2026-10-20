import re

text = "i will go mumbai from chennai on the flight aR192475"

print("Match:", re.match("i will", text).group())
print("Search:", re.search("mumbai", text).group())
print("Flight Number:", re.findall(r"[a-zA-Z]{2}\d+", text))
text = text.replace("mumbai","delhi")
print("new text:",text)
