
import re

import re

regex = r"(\d{4}(\s|-)?){4}"

test_str = "6666 6666 6666 6666, 6666-6666-6666-6666, 6666666666666666"

matches = re.finditer(regex, test_str, re.MULTILINE)

for i in matches:
    print(i)