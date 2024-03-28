import re

with open('sitemap.html','r') as file:
    content = file.read()

    # Regular expression pattern to match <li>...</li>
    pattern = r'<li>http(.*?)</li>'

    # Find all matches
    matches = re.findall(pattern, content)

    # Print the matches
    with open('output.txt','w') as x:
        for match in matches:
            x.write(match + "\n")
