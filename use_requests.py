import requests

url = 'https://kontan.co.id'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! response = {response.status_code}')
        print(f'content {response.text}')
    else:
        print(f'whoops, ada kesalahan requests {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')