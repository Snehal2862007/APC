import requests
result=requests.get("https://github.com")
print(result.status_code)

