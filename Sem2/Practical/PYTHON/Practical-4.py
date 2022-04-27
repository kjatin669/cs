
import re
string = "Global Warning"
a = re.search("....$", string)
print("The last four Character of String is", a.group())


import re
string = "Global Warning"
b = []
a = re.search("....$", string)
for i in range(4, 8):
    a = string[i]
    b.append(a)
print(b)

import re
string = "Global Warning"
a = re.search("0", string)
if (a):
    print("String is AlphaNumeric")
else:
    print("String is Not Alphanumeric")

import re
string = "Global Warming"
a = re.search("....$", string)
print(string.replace(a.group(), ""))

import re
string = "Global Warming"
a = re.search("....", string)
print(string.replace(a.group(), ""))

import re
string = "Global Warming"
print(string.find("Wa"))

import re
string = "Global Warming"
print(string.upper())

import re
string = "Global Warming"
a = string.istitle()
print(a)

import re
string = "Global Warming"
print(string.replace("a", "*"))
