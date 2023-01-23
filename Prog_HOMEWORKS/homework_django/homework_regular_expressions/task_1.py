
import re

regex = r"R{1}b+r{1}"

test_str = "Rbr Rbbbbbbbr RbR rBr RBBR RbbR RbR Rbbbr"

matches = re.finditer(regex, test_str)

for i in matches:
    print(i)
