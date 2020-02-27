# Collection of commonly used Regex because I always forget
import re

################################################
# Email Addresses
################################################

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+    # username  
        @                   # @ symbol 
        [a-zA-Z0-9.-]+      # domain name 
        (\.[a-zA-Z]{2,4})   # dot-something 
        )''', re.VERBOSE)
if emailRegex.match("as12@github.com"):
    print("Matched")


################################################
# Telephone Number
################################################
"""
123-123-1234
333-333-3333 ext.12334 
123 123 1234 
"""

phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?              # area code
            (\s|-|\.)?                      # separator
            (\d{3})                         # first 3 digits
            (\s|-|\.)                       # separator
            (\d{4})                         # last 4 digits
            (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

if phoneRegex.match("123-123-1234"):
    print("Matched")

################################################
# StrongPassword Detection
################################################
strongPasswordRegex = re.compile(r'''
    ^                   # Prefix
    (?=.{8,})           # At least 8 char
    (?=.*[!@#$%^&*])    # Special Char
    (?=.*[0-9])         # Numerical
    (?=.*[A-Z])         # Capital
    (?=.*[a-z])         # Lower case
    .*                  # End
''', re.VERBOSE)

if strongPasswordRegex.match("ssdadwa3SDSAdd@12"):
    print("Matched")
