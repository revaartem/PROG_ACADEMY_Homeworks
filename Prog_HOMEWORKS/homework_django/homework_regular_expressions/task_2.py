
import re

regex = r"^(\d{4}(\s|-)?){4}$"

test_str = "6666666666666666"
test_str_1 = "6666 6666 6666 6666"
test_str_2 = "6666-6666-6666-6666"

matches = re.finditer(regex, test_str)
matches_1 = re.finditer(regex, test_str_1)
matches_2 = re.finditer(regex, test_str_2)

for i in matches:
    print(i)

for i in matches_1:
    print(i)

for i in matches_2:
    print(i)