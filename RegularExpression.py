import re
pattern = r"^abc"
myString = "abcdef"
print(re.match(pattern, myString))

pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.])"
email = "abc@gmail.com"
print(re.match(pattern, email))

pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.])"
email = "abcgmail.com"
print(re.match(pattern, email))