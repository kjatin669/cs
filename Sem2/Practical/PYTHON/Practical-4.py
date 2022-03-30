
import re
string = "Global Warning"
b = []
print("\n")
a = re.search("....$", string)
print("The last four Character of String is", a.group())


import re
string = "Global Warning"
b = []
print("\n")
a = re.search("....$", string)
for i in range(4, 8):
    a = string[i]
    b.append(a)
print(b)

import re
string = "Global Warning"
b = []
print("\n")
a = re.search("0", string)
if (a):
    print("String is AlphaNumeric")
else:
    print("String is Not Alphanumeric")

import re
string = "Global Warming"
b = []
print("\n")
a = re.search("....$", string)
print("\n")
a = re.search("....$", string)
print(string.replace(a.group(), ""))

import re
string = "Global Warming"
b = []
print("\n")
a = re.search("....$", string)
print("\n")
a = re.search("....", string)
print(string.replace(a.group(), ""))


import re
string = "Global Warming"
b = []
print("\n")
a = re.search("....$", string)
print("\n")
print("\n")
print(string.find("Wa"))


import re
string = "Global Warming"
b = []
a = re.search("....$", string)
print("\n")
print("\n")
print(string.upper())

import re
string = "Global Warming"
b = []
print("\n")
print("\n")
print(string)
a = string.istitle()
print(a)

import re
string = "Global Warming"
b = []
print("\n")
print("\n")
print(string.replace("a", "*"))
