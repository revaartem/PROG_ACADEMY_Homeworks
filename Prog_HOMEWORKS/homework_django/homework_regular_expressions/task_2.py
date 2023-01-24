
import re

regex = r"^(\d{4}(\s|-)?){4}$"

test_str = "6666666666666666"
test_str_1 = "6666 6666 6666 6666"
test_str_2 = "6666-6666-6666-6666"

matches = re.search(regex, test_str)
matches_1 = re.search(regex, test_str_1)
matches_2 = re.search(regex, test_str_2)

print(matches)
print(matches_1)
print(matches_2)
