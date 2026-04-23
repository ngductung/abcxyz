import re


excluded_extensions = ['.js', '.svg', '.css', '.png', '.jpg', '.ttf', '.ico', '.html', '.map']

with open('sitemap.html','r') as file:
    content = file.read()

    # Regular expression pattern to match <li>...</li>
    pattern = r'<li>(ht.*?)</li>'

    # Find all matches
    matches = re.findall(pattern, content)

    # Print the matches
    with open('output.txt','w') as x:
        for match in matches:
            if not any(match.endswith(ext) for ext in excluded_extensions):
                x.write(match + "\n")
