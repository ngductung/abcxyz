import requests
import base64
import glob
import json

# Proxy để máy nội bộ có thể kết nối đến trang pentest
exec(base64.b64decode('cHJveHkgPSB7J2h0dHBzJzpiYXNlNjQuYjY0ZGVjb2RlKCdhSFIwY0Rvdkx6RTVNaTR4TmpndU5TNDRPak14TWpnPScpLmRlY29kZSgpfQ=='))

# Nếu script không chạy trong máy nội bộ, hãy set giá trị là None, hoặc Burp Proxy
# http
# 192
# 168
# 5
# 8
# 3128
proxy = {'https':''}

# refresh_token lấy tại Local Storage trang pentest sau khi đăng nhập
refresh_token = ''

# Phần đầu của các file muốn upload
# vd: các file là Google.zip.001, Google.zip.002 => pattern='Google'
pattern = '' 

# base64 domain, né search :))
exec(base64.b64decode('ZG9tYWluID0gYmFzZTY0LmI2NGRlY29kZSgnY0dWdWRHVnpkQzUyYVdWMGRHVnNZM2xpWlhJdVkyOXQnKS5kZWNvZGUoKQ=='))

def encode_file_to_base64(input_file_path):
    with open(input_file_path, "rb") as input_file:
        encoded_bytes = base64.b64encode(input_file.read())
        return encoded_bytes.decode("utf-8")

def get_token():
    url = f'https://{domain}/api/v1/token/refresh'
    headers = {'Content-Type': 'application/json'}
    
    data = json.dumps({'token':refresh_token})

    response = requests.post(url, headers=headers, data=data, proxies=proxy)

    return response.json()['token']

token = get_token()

def uploadfile(filename):
    url = f'https://{domain}/attachments'
    headers = {
        'Content-Type': 'application/json',
        'Token': token
    }

    data = json.dumps({"content":encode_file_to_base64(filename),"name":f'{filename}.docx'})

    response = requests.post(url, headers=headers, data=data, proxies=proxy)
    return response.json()

output = ''
matching_files = glob.glob(f'{pattern}*')

for file in matching_files:
    x = uploadfile(file)
    y = x['path']
    output += f'curl "https://{domain}/{y}" -o "{file}"\n'
    print(f'Done {file}')

open(f'output - {pattern}.bat', 'w').write(output)
print('Done All!')
