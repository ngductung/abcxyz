import re

with open('common.js', 'r') as file:
    content = file.read()

    # pattern = r'this\.http.(get|post|put|delete)\(\`(.*.\})(.*)`'
    pattern = r'Url\}(.*)`'
    matches = re.findall(pattern, content)

    with open('output.txt', 'w') as x:
        for match in matches:
            # print(match)
            x.write(match + "\n")
            # x.write(match[0] + " " + match[1] + match[2] + "\n")
