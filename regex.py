import re


pattern = re.compile('^[a-zA-Z\s]+$') # start at beginning, small letters and caps and space one or more and to end of phrase.


pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")

print(re.search(pattern, "dgd569Fghhdfgh 76"))
