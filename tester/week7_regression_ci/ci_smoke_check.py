import sys
import requests

URL = "https://the-internet.herokuapp.com/login"

try:
    response = requests.get(URL, timeout=10)
    ok = (
        response.status_code == 200
        and "Login Page" in response.text
    )
except requests.RequestException as exc:
    print(f"Smoke check error: {exc}")
    sys.exit(1)

if ok:
    print("PASS: login page is reachable.")
    sys.exit(0)

print(f"FAIL: unexpected response. Status={response.status_code}")
sys.exit(1)
