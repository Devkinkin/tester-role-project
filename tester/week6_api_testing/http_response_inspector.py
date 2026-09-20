import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(URL, timeout=10)

print("REQUEST")
print(f"Method: {response.request.method}")
print(f"URL:    {response.request.url}")

print("\nRESPONSE")
print(f"Status: {response.status_code}")

print("\nSelected headers")
for header in ["content-type", "server", "date"]:
    if header in response.headers:
        print(f"{header}: {response.headers[header]}")

print("\nJSON body")
print(response.json())
