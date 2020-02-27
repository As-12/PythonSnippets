#! python3
# This is a sample project to search for phone number from a long string or text file


# Import re
# Create regex object using re.compile
# use regex object.search to find Match objects

import re

regex_phone = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
regex_obj = re.compile(regex_phone)

string = "John Telephone is 123-312-1123. Jane telephone is 312-123-1412. She lives on elm street"
string2 = "There's probably no match here"

match_obj = regex_obj.search(string)

# Match once
if match_obj is not None:
    print(match_obj.group())
else:
    print("There's no match")

# Match everything

numbers = regex_obj.findall(string)

print("Finding all matches")
for number in numbers:
    print(number)





